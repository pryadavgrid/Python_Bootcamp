# 📦 Module and Package in Python

## 📘 1. What is a Module?

A **module** is a single Python file.
It contains Python code like:

* Functions
* Variables
* Classes

👉 Simply:
**One `.py` file = One Module**

### ✅ Example

Create a file:

```
math_utils.py
```

Inside this file:

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

Now `math_utils.py` is a **module**.

---

## 📘 2. What is a Package?

A **package** is a folder that contains many modules.

👉 Simply:
**Folder + Python files = Package**

### ✅ Example Folder Structure

```
my_package/
│
├── __init__.py
├── math_utils.py
├── string_utils.py
```

* `my_package` → Package
* `math_utils.py` → Module
* `string_utils.py` → Module

📌 `__init__.py`
This file tells Python that this folder is a package.
(It can be empty.)

---

# 📥 How to Import One File into Another File

There are different ways to import.

---

## ✅ 1. Import Full Module

File structure:

```
main.py
math_utils.py
```

### 🔹 main.py

```python
import math_utils

print(math_utils.add(10, 5))
```

### ✔ Output

```
15
```

👉 Here we use:
`module_name.function_name`

---

## ✅ 2. Import Only One Function

```python
from math_utils import add

print(add(10, 5))
```

👉 Now no need to write `math_utils.add()`

---

## ✅ 3. Import Multiple Functions

```python
from math_utils import add, sub
```

---

## ✅ 4. Import Everything (Not Recommended)

```python
from math_utils import *
```

⚠ Not recommended because it can create confusion if many functions have same name.

---

## 📦 Import from Package

Folder structure:

```
my_package/
│
├── __init__.py
├── math_utils.py

main.py
```

### 🔹 main.py

```python
from my_package import math_utils

print(math_utils.add(5, 3))
```

OR

```python
from my_package.math_utils import add

print(add(5, 3))
```

---

# 📂 Important Rule

✔ Files must be in same folder
OR
✔ Package must be properly structured

Otherwise Python will show:

```
ModuleNotFoundError
```

---

# 🧠 Why We Use Modules and Packages?

* To organize code
* To reuse code
* To make project clean
* To avoid writing same code again

---

# 🔥 Real Example

Python built-in modules:

```python
import math
import random
```

These are already available in Python.

---

# 📌 Summary

| Term    | Meaning                            |
| ------- | ---------------------------------- |
| Module  | One Python file                    |
| Package | Folder containing modules          |
| import  | Used to use code from another file |

