## 1️⃣ What is **pylint**?

### 👉 Simple meaning

**pylint** is a tool that **checks your Python code** and tells you:

* Is your code written in a good way?
* Are there mistakes?
* Are variable names, spacing, and style correct?

👉 Think of **pylint as a “code teacher”** 👨‍🏫
It does **not run your program**, it only **checks your code quality**.

---

### 🔍 What pylint checks

pylint checks many things, for example:

1. **Syntax errors**

```python
print("Hello"
```

➡️ Missing `)` → pylint will warn you

2. **Bad variable names**

```python
a = 10
```

➡️ pylint may say: variable name is not clear

3. **Unused variables**

```python
x = 5
print("Hi")
```

➡️ `x` is never used

4. **Coding style (PEP 8)**

* Line length
* Spaces
* Indentation
* Function names

---

### 🛠 Example of pylint

#### File: `sample.py`

```python
def add(a,b):
    return a+b
```

Run pylint:

```bash
pylint sample.py
```

pylint may say:

* Missing space after comma
* Function name is OK
* Code score: **7/10**

---

### ⭐ Why we use pylint

* Write **clean code**
* Find **bugs early**
* Follow **Python standards**
* Used in **companies & interviews**

---

## 2️⃣ What is **unittest**?

### 👉 Simple meaning

**unittest** is used to **test your code**.

👉 Think of **unittest as an exam** 📝 for your Python functions.

It checks:

* Is your function giving the **correct output**?
* Does it break in some cases?

---

### 🔍 What unittest does

* Runs your function
* Compares **expected result** with **actual result**
* Tells **PASS ✅ or FAIL ❌**

---

### 🧠 Real life example

You write a calculator.
Before giving it to users, you test:

* 2 + 2 = 4?
* 5 − 3 = 2?

That testing is done using **unittest**.

---

### 🧪 Simple unittest example

#### File: `math_utils.py`

```python
def add(a, b):
    return a + b
```

#### Test file: `test_math_utils.py`

```python
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

Run test:

```bash
python test_math_utils.py
```

Output:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

➡️ `OK` means test passed ✅

---

### 🧰 Common unittest methods

| Method                | Meaning             |
| --------------------- | ------------------- |
| `assertEqual(a, b)`   | a == b              |
| `assertTrue(x)`       | x is True           |
| `assertFalse(x)`      | x is False          |
| `assertIsNone(x)`     | x is None           |
| `assertRaises(Error)` | error should happen |

---

### ⭐ Why we use unittest

* Find bugs **before production**
* Safe code changes
* Used in **real projects**
* Very important for **jobs**

---

## 🔁 Difference between pylint and unittest

| pylint                          | unittest                |
| ------------------------------- | ----------------------- |
| Checks code **style & quality** | Checks **code logic**   |
| Does NOT run code               | Runs code               |
| Finds bad practices             | Finds wrong results     |
| Used while writing code         | Used after writing code |

---

## 🧠 Easy summary

* ✅ **pylint** → *How good is my code?*
* ✅ **unittest** → *Is my code correct?*

---
