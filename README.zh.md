## 目录比较脚本

该脚本比较两个目录并删除相同的文件。

### README 翻译版本

---

- [English](README.md)
- [中文](README.zh.md)

## 功能

- 使用 SHA3-256 哈希值比较两个目录中的文件。
- 删除两个目录中相同的文件。
- 比较完成后删除空文件夹。
- 支持多进程以加速比较过程。

## 安装

1. 克隆代码库：
    ```bash
    git clone https://github.com/Ranshen1209/directory_comparison.git
    cd directory_comparison
    ```

2. 确保已安装 Python 3.x。

3. 安装任何必要的依赖项（如果有的话）。

## 使用方法

1. 将要比较的目录放在脚本所在的同一目录下，并分别命名为 `file_a` 和 `file_b`。

2. 运行脚本：
    ```bash
    python directory_comparison.py
    ```

3. 脚本会比较 `file_a` 和 `file_b` 目录中的文件，删除相同的文件，并移除任何空文件夹。

## 函数

- `read_file_chunks(filename, chunk_size=8192)`: 以块的形式读取文件内容。
- `get_file_sha3(filename)`: 计算文件的 SHA3-256 哈希值。
- `get_all_files(path)`: 获取目录下所有文件的路径。
- `remove_empty_folders(directory)`: 删除目录中的空文件夹。
- `compare_and_collect(a_file, b_file, hash_cache)`: 比较两个文件，如果相同则返回文件路径。
- `delete_files(to_delete)`: 根据提供的列表删除文件。
- `dir_compare(a_path, b_path, hash_cache)`: 比较两个目录下的文件并删除相同的文件。
- `main()`: 执行脚本的主函数。

## 许可证

该项目采用 GPL-3.0 许可证 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。



