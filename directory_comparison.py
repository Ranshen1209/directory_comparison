import os
import hashlib
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

# 以块的形式读取文件内容
def read_file_chunks(filename, chunk_size=8192):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# 计算文件的 SHA3-256 哈希值
def get_file_sha3(filename):
    sha_hash = hashlib.sha256()
    for chunk in read_file_chunks(filename):
        sha_hash.update(chunk)
    return sha_hash.hexdigest()

# 获取目录下所有文件的路径
def get_all_files(path):
    file_list = []
    for root, _, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# 删除空文件夹
def remove_empty_folders(directory):
    for root, dirs, _ in os.walk(directory, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)
                except OSError as e:
                    print(f"Error: {dir_path} : {e.strerror}")

# 比较两个文件的哈希值，如果相同则返回文件路径，否则返回 None
def compare_and_collect(a_file, b_file, hash_cache):
    if os.path.getsize(a_file) != os.path.getsize(b_file):
        return None
    
    a_mtime = os.path.getmtime(a_file)
    b_mtime = os.path.getmtime(b_file)
    
    if (a_file in hash_cache and hash_cache[a_file][1] == a_mtime):
        a_sha3 = hash_cache[a_file][0]
    else:
        a_sha3 = get_file_sha3(a_file)
        hash_cache[a_file] = (a_sha3, a_mtime)
    
    if (b_file in hash_cache and hash_cache[b_file][1] == b_mtime):
        b_sha3 = hash_cache[b_file][0]
    else:
        b_sha3 = get_file_sha3(b_file)
        hash_cache[b_file] = (b_sha3, b_mtime)

    if a_sha3 == b_sha3:
        return a_file, b_file
    else:
        return None

# 删除文件
def delete_files(to_delete):
    for file_pair in to_delete:
        if file_pair:
            a_file, b_file = file_pair
            try:
                if os.path.exists(a_file):
                    os.remove(a_file)
                if os.path.exists(b_file):
                    os.remove(b_file)
            except OSError as e:
                print(f"Error deleting {a_file} or {b_file}: {e}")
            except Exception as e:
                print(f"Exception deleting {a_file} or {b_file}: {type(e).__name__} - {e}")

# 比较两个目录下的文件，如果相同则删除
def dir_compare(a_path, b_path, hash_cache):
    a_files = get_all_files(a_path)
    b_files = get_all_files(b_path)

    setA = {os.path.basename(f): f for f in a_files}
    setB = {os.path.basename(f): f for f in b_files}

    common_files = setA.keys() & setB.keys()

    to_delete = []

    print("Comparing and deleting identical files...")

    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        future_to_file = {executor.submit(compare_and_collect, setA[f], setB[f], hash_cache): f for f in common_files}
        for future in as_completed(future_to_file):
            try:
                result = future.result()
                if result:
                    to_delete.append(result)
            except Exception as exc:
                print(f"Exception processing {future_to_file[future]}: {exc}")

    delete_files(to_delete)
    return len(to_delete)

# 主函数
def main():
    manager = multiprocessing.Manager()
    hash_cache = manager.dict()

    try:
        start_time = time.perf_counter()
        while True:
            num_deleted = dir_compare(os.path.abspath("file_a"), os.path.abspath("file_b"), hash_cache)
            if num_deleted == 0:
                break
        remove_empty_folders(os.path.abspath("file_a"))
        remove_empty_folders(os.path.abspath("file_b"))
        end_time = time.perf_counter()
        print(f"Synchronization complete. Time elapsed: {end_time - start_time:.2f} s.")
    except Exception as e:
        print(f"Error during execution: {e}")
    finally:
        # 保证执行结束后让用户看到输出
        input("Press Enter to exit...")

# 程序入口
if __name__ == '__main__':
    main()
