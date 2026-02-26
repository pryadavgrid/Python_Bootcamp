# 📂 Working with CSV and PDF Files in Python

This guide will help you understand how to work with:

* 📊 **CSV files** using:

  * `pandas` library
  * `csv` module

* 📄 **PDF files** using:

  * `pypdf` library

Everything is explained in **simple English** with examples.

---

# 📊 PART 1: Working with CSV Files

## ✅ What is a CSV File?

CSV means **Comma Separated Values**.

It is a simple text file used to store table data like this:

```
name,age,city
John,25,Delhi
Sara,30,Mumbai
```

Each value is separated by a comma.

---

# 🔹 Method 1: Using `csv` Module (Built-in Module)

The `csv` module is already available in Python.

## 📌 Reading a CSV File

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### 👉 What happens here?

* `open()` → opens the file
* `"r"` → read mode
* `csv.reader()` → reads file line by line
* `row` → each row is a list

Output:

```
['name', 'age', 'city']
['John', '25', 'Delhi']
['Sara', '30', 'Mumbai']
```

---

## 📌 Writing to a CSV File

```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Amit", 22, "Jaipur"])
```

### 👉 Important:

* `"w"` → write mode
* `newline=""` → prevents extra blank lines
* `writerow()` → writes one row

---

# 🔹 Method 2: Using `pandas` Library (Very Powerful)

## ✅ What is pandas?

`pandas` is a very popular Python library for data analysis.

First install it:

```
pip install pandas
```

---

## 📌 Reading CSV using pandas

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df)
```

### 👉 What is `df`?

`df` means **DataFrame**.
DataFrame is like a table (rows and columns).

Output:

```
   name  age    city
0  John   25   Delhi
1  Sara   30  Mumbai
```

---

## 📌 Writing CSV using pandas

```python
import pandas as pd

data = {
    "name": ["Rahul", "Priya"],
    "age": [28, 24],
    "city": ["Delhi", "Pune"]
}

df = pd.DataFrame(data)
df.to_csv("new_data.csv", index=False)
```

### 👉 Important:

* `index=False` → removes row numbers from file

---

# 📄 PART 2: Working with PDF Files

We will use **pypdf** library.

## ✅ What is pypdf?

`pypdf` is a Python library used to:

* Read PDF
* Extract text
* Merge PDF
* Split PDF

Install it:

```
pip install pypdf
```

---

# 📌 Reading a PDF File

```python
from pypdf import PdfReader

reader = PdfReader("sample.pdf")

print("Total Pages:", len(reader.pages))

page = reader.pages[0]
text = page.extract_text()

print(text)
```

### 👉 Explanation:

* `PdfReader()` → opens PDF
* `reader.pages` → list of all pages
* `extract_text()` → gets text from page

---

# 📌 Writing / Creating a PDF

```python
from pypdf import PdfWriter

writer = PdfWriter()

writer.add_blank_page(width=300, height=400)

with open("new_file.pdf", "wb") as file:
    writer.write(file)
```

### 👉 Explanation:

* `PdfWriter()` → creates new PDF
* `add_blank_page()` → adds empty page
* `"wb"` → write binary mode

---

# 📌 Merging Two PDF Files

```python
from pypdf import PdfMerger

merger = PdfMerger()

merger.append("file1.pdf")
merger.append("file2.pdf")

merger.write("merged.pdf")
merger.close()
```

---

# 📌 Extracting All Text from PDF

```python
from pypdf import PdfReader

reader = PdfReader("sample.pdf")

for page in reader.pages:
    print(page.extract_text())
```

---

# 🆚 csv vs pandas

| csv module          | pandas            |
| ------------------- | ----------------- |
| Simple              | Powerful          |
| Basic read/write    | Data analysis     |
| Returns list        | Returns DataFrame |
| Good for small work | Good for big data |

---

# 🆚 CSV vs PDF

| CSV               | PDF                  |
| ----------------- | -------------------- |
| Stores table data | Stores document data |
| Easy to edit      | Hard to edit         |
| Used for data     | Used for reports     |

---

# 🎯 When to Use What?

✅ Use `csv` module → simple file reading/writing
✅ Use `pandas` → data analysis and large data
✅ Use `pypdf` → working with PDF files

---

# 📌 Final Summary

In this guide you learned:

* How to read and write CSV using `csv`
* How to read and write CSV using `pandas`
* How to read, create, merge PDF using `pypdf`

Now you can work with both **data files (CSV)** and **document files (PDF)** in Python easily 🚀
