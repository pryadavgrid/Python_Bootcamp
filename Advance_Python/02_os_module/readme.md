# Working with Files and Folders in Python (`os` & `shutil`)

## Description

This project shows how to **work with files and folders** in Python using the **`os`** and **`shutil`** modules.

* **`os` module**: Helps you interact with the operating system. You can list files, check if a file exists, and navigate folders.
* **`shutil` module**: Helps you perform **high-level file operations** like copying, moving, deleting, and making archives.

These modules are **built into Python**, so no installation is needed.

---

## Installation

Python comes with `os` and `shutil` by default. Just check your Python version:

```bash
python --version
```

---

## Using `os` Module

### 1. Import the module

```python
import os
```

### 2. List files and folders

```python
print(os.listdir('.'))  # List all files and folders in current directory
```

### 3. Check if a file/folder exists

```python
if os.path.exists('example.txt'):
    print("File exists")
```

### 4. Get current working directory

```python
print(os.getcwd())
```

### 5. Change directory

```python
os.chdir('/path/to/folder')
print(os.getcwd())
```

---

## Using `shutil` Module

### 1. Import the module

```python
import shutil
```

### 2. Copy files

```python
shutil.copy('source.txt', 'destination.txt')   # Copy file
shutil.copy2('source.txt', 'destination.txt')  # Copy file with metadata
```

### 3. Move or rename files/folders

```python
shutil.move('old_folder', 'new_folder')  # Move or rename
```

### 4. Delete folders

```python
shutil.rmtree('folder_name')  # Delete folder and all its content
```

### 5. Create archives

```python
shutil.make_archive('backup', 'zip', 'folder_to_zip')  # Make zip archive
```

### 6. Disk usage

```python
total, used, free = shutil.disk_usage('/')
print(total, used, free)
```

---

## Example: Using `os` + `shutil`

```python
import os
import shutil

# List files
files = os.listdir('.')
print("Files:", files)

# Copy a file if it exists
if 'example.txt' in files:
    shutil.copy('example.txt', 'backup_example.txt')

# Move a folder
if os.path.exists('old_folder'):
    shutil.move('old_folder', 'new_folder')
```

---

## Difference Between `os` and `shutil`

| Feature      | `os` Module                                   | `shutil` Module                           |
| ------------ | --------------------------------------------- | ----------------------------------------- |
| Main purpose | Interact with OS (folders, paths)             | High-level file/folder operations         |
| Examples     | List files, check existence, change directory | Copy, move, delete, archive files/folders |
| Level        | Low-level (basic operations)                  | High-level (complex operations)           |
| Works on     | Files, folders, paths                         | Files and folders                         |

**Analogy:**

* `os` → Checking what’s in a room, opening doors.
* `shutil` → Moving furniture, copying items, cleaning the room.

---

## Notes

* Always close files if using `open()` without `with`.
* Use `os.path` functions to handle paths safely.
* Combine `os` + `shutil` for complete file and folder management.

---
