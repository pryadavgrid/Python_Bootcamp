# 🐞 Python Debugger (`pdb`) Module

## 📌 Introduction

`pdb` is the **Python Debugger**.
It helps you:

* Find errors (bugs)
* Check variable values
* Run code step by step
* Understand how your program works

`pdb` is built-in module in Python.
You do NOT need to install it.

---

## 📦 Importing `pdb`

```python
import pdb
```

---

# 🚀 Why We Use `pdb`?

Sometimes:

* Program gives wrong output
* Program crashes
* Logic is not working
* We want to see what is happening inside code

`pdb` helps us stop the program and check everything.

---

# 🛑 Method 1: Using `pdb.set_trace()`

This is the most common way.

## ✅ Example

```python
import pdb

def add_numbers(a, b):
    pdb.set_trace()   # Debugger will stop here
    result = a + b
    return result

add_numbers(5, 3)
```

When Python runs this:

* Program will stop at `set_trace()`
* You can type commands in terminal

---

# 🧭 Important `pdb` Commands

| Command      | Meaning              |
| ------------ | -------------------- |
| `n`          | Next line            |
| `s`          | Step inside function |
| `c`          | Continue execution   |
| `q`          | Quit debugger        |
| `l`          | Show code            |
| `p variable` | Print variable value |
| `h`          | Help                 |

---

## 🔍 Example Session

When debugger stops:

```
(Pdb)
```

Now you can type:

```
(Pdb) p a
5

(Pdb) p b
3

(Pdb) n
```

---

# 🛠 Method 2: Run Entire Script with Debugger

You can run your file using:

```bash
python -m pdb filename.py
```

Example:

```bash
python -m pdb test.py
```

It will start debugging from first line.

---

# 🔁 Step by Step Example

## Example Code

```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```

This gives error:

```
ZeroDivisionError
```

Now debug it:

```bash
python -m pdb test.py
```

Then check values step by step.

---

# 🧠 What Happens Inside `pdb`?

When debugger runs:

1. Code pauses
2. You control execution
3. You inspect variables
4. You find problem
5. You fix the bug

---

# 💡 Best Practice

✔ Use `pdb.set_trace()` where you think problem exists
✔ Remove debugger after fixing bug
✔ Do not leave debugger in production code

---

# 🔄 Difference: `print()` vs `pdb`

| print()       | pdb                    |
| ------------- | ---------------------- |
| Shows value   | Full control           |
| Simple        | Powerful               |
| Manual checks | Step-by-step debugging |

`pdb` is more powerful than `print()` debugging.

---

# 🎯 When Should You Use `pdb`?

* When logic is complex
* When loop is not working
* When function returns wrong value
* When error is hard to find

---