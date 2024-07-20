## Directory Comparison Script

This script compares two directories and deletes identical files.

### README Translated Versions

---

- [English](README.md)
- [中文](README.zh.md)

## Features

- Compare files in two directories using SHA3-256 hash values.
- Delete identical files in both directories.
- Remove empty folders after comparison.
- Supports multiprocessing to speed up the comparison process.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ranshen1209/directory_comparison.git
   cd directory_comparison

2. Ensure you have Python 3.x installed.

3. Install any necessary dependencies (if applicable).

## Usage

1. Place the directories you want to compare in the same directory as the script and name them `file_a` and `file_b`.

2. Run the script:

   ```bash
   python directory_comparison.py
   ```

3. The script will compare files in `file_a` and `file_b`, delete identical files, and remove any empty folders.

## Functions

- `read_file_chunks(filename, chunk_size=8192)`: Reads file contents in chunks.
- `get_file_sha3(filename)`: Calculates the SHA3-256 hash value of a file.
- `get_all_files(path)`: Retrieves all file paths in a directory.
- `remove_empty_folders(directory)`: Removes empty folders in a directory.
- `compare_and_collect(a_file, b_file, hash_cache)`: Compares two files and returns the paths if they are identical.
- `delete_files(to_delete)`: Deletes files based on the provided list.
- `dir_compare(a_path, b_path, hash_cache)`: Compares files in two directories and deletes identical files.
- `main()`: The main function to execute the script.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.