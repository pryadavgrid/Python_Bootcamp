# 🐍 Python Basics – Main Guide

Welcome to **Python Basics**.
This folder contains all the important basic concepts of Python.

This README gives a simple overview of each topic.
Each topic has its own detailed README file inside its folder.

---

## 📌 1. Basics (Numbers, List, Dict, Tuple, etc.)

This section covers the most important basic data types in Python.

### 🔢 Numbers

* Integer → `10`
* Float → `10.5`
* Complex → `2 + 3j`

Basic operations:

```python
a = 10
b = 5
print(a + b)
```

---

### 📋 List

* Ordered
* Changeable (Mutable)
* Allows duplicate values

```python
my_list = [1, 2, 3, 4]
my_list.append(5)
```

---

### 📦 Tuple

* Ordered
* Not changeable (Immutable)

```python
my_tuple = (1, 2, 3)
```

---

### 📚 Dictionary

* Key and Value pair
* Changeable

```python
my_dict = {"name": "Prateek", "age": 25}
print(my_dict["name"])
```

---

### 🔹 Other Basic Types

* String → `"Hello"`
* Boolean → `True / False`
* Set → `{1, 2, 3}`

---

## 📌 2. Functions

A function is a block of reusable code.

```python
def greet(name):
    return "Hello " + name

print(greet("Prateek"))
```

### Why use functions?

* Code reuse
* Clean code
* Easy to manage

---

## 📌 3. OOP (Object Oriented Programming)

OOP means creating objects using classes.

### Class Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p1 = Person("Prateek")
p1.greet()
```

### OOP Concepts:

* Class
* Object
* Inheritance
* Encapsulation
* Polymorphism

---

## 📌 4. Modules and Packages

### Module

A Python file with functions or variables.

Example:

```python
import math
print(math.sqrt(25))
```

---

### Package

A folder that contains multiple Python files.

Structure:

```
mypackage/
    __init__.py
    file1.py
    file2.py
```

---

## 📌 5. Error Handling

Error handling helps prevent program crashes.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Important Blocks:

* `try`
* `except`
* `else`
* `finally`

---

## 📌 6. Testing

Testing checks if your code works correctly.

### Simple Example:

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

You can also use:

* `unittest`
* `pytest`

Testing helps:

* Find bugs
* Improve code quality
* Build confidence

---

## 📌 7. Decorators

Decorator is a function that modifies another function.

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

Decorator is used for:

* Logging
* Authentication
* Timing functions
