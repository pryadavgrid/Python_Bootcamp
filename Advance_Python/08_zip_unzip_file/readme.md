Here is your **README.md** file content.
# 📦 ZIP and UNZIP Files in Python

## 📌 Introduction

In Python, we can **compress (zip)** files and **extract (unzip)** files using built-in modules.

Main modules used:

* `zipfile` → Work with ZIP files
* `shutil` → Create and extract archives easily
* `os` → Work with file paths

---

# 🗂 1️⃣ zipfile Module

The `zipfile` module is used to:

* Create ZIP files
* Add files to ZIP
* Extract ZIP files
* Read ZIP content

It is a built-in module. No need to install.

```python
import zipfile
```

---

# 🧾 2️⃣ Create a ZIP File

## ✅ Example: Zip a Single File

```python
import zipfile

with zipfile.ZipFile("myzipfile.zip", "w") as zipf:
    zipf.write("example.txt")

print("File zipped successfully!")
```

### 🔎 Explanation

* `"myzipfile.zip"` → Name of zip file
* `"w"` → Write mode
* `zipf.write("example.txt")` → Add file to zip

---

## ✅ Example: Zip Multiple Files

```python
import zipfile

files = ["file1.txt", "file2.txt", "file3.txt"]

with zipfile.ZipFile("allfiles.zip", "w") as zipf:
    for file in files:
        zipf.write(file)

print("All files zipped!")
```

---

# 📂 3️⃣ Extract (Unzip) Files

## ✅ Extract All Files

```python
import zipfile

with zipfile.ZipFile("allfiles.zip", "r") as zipf:
    zipf.extractall("output_folder")

print("Files extracted!")
```

### 🔎 Explanation

* `"r"` → Read mode
* `extractall()` → Extract all files
* `"output_folder"` → Folder where files will be saved

---

## ✅ Extract a Single File

```python
with zipfile.ZipFile("allfiles.zip", "r") as zipf:
    zipf.extract("file1.txt", "output_folder")
```

---

# 📜 4️⃣ List Files Inside ZIP

```python
with zipfile.ZipFile("allfiles.zip", "r") as zipf:
    print(zipf.namelist())
```

### Output:

```
['file1.txt', 'file2.txt', 'file3.txt']
```

---

# 📖 5️⃣ Read a File Inside ZIP Without Extracting

```python
with zipfile.ZipFile("allfiles.zip", "r") as zipf:
    with zipf.open("file1.txt") as file:
        content = file.read()
        print(content.decode())
```

---

# ⚙️ 6️⃣ ZIP a Folder

```python
import zipfile
import os

folder_path = "myfolder"

with zipfile.ZipFile("folder.zip", "w") as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            zipf.write(os.path.join(root, file))

print("Folder zipped!")
```

---

# 🚀 7️⃣ Using shutil Module (Easy Method)

The `shutil` module gives simple functions.

```python
import shutil
```

---

## ✅ Create ZIP Using shutil

```python
import shutil

shutil.make_archive("myarchive", "zip", "myfolder")

print("Archive created!")
```

### 🔎 Explanation

* `"myarchive"` → Zip file name (without .zip)
* `"zip"` → Archive format
* `"myfolder"` → Folder to zip

---

## ✅ Extract ZIP Using shutil

```python
import shutil

shutil.unpack_archive("myarchive.zip", "output_folder")

print("Archive extracted!")
```

---

# 🆚 zipfile vs shutil

| zipfile               | shutil                |
| --------------------- | --------------------- |
| More control          | Simple and easy       |
| Can read inside ZIP   | Mainly create/extract |
| Good for advanced use | Good for quick use    |

---

# 📌 Important Modes in zipfile

| Mode  | Meaning                 |
| ----- | ----------------------- |
| `"w"` | Write (create new zip)  |
| `"r"` | Read zip                |
| `"a"` | Append (add more files) |

---

# 🎯 Real Life Example

Example: Backup project folder

```python
import shutil

shutil.make_archive("project_backup", "zip", "my_project")
```

Now you have:

```
project_backup.zip
```

---

# ✅ Summary

✔ `zipfile` → Full control
✔ `shutil` → Easy method
✔ `extractall()` → Extract all files
✔ `write()` → Add file
✔ `namelist()` → See files inside zip

---
