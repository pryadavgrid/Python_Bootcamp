# 📘 Advanced Python Objects – Summary Notes

Author: Prateek Yadav
Level: Beginner Friendly
Language: Simple English

---

# 🔢 1. Advanced Numbers

Python provides built-in functions to work with numbers.

## ✅ hex()

* Converts integer to hexadecimal.
* Output starts with `0x`.

Example:

```python
hex(512)   # 0x200
```

---

## ✅ bin()

* Converts integer to binary.
* Output starts with `0b`.

Example:

```python
bin(128)   # 0b10000000
```

---

## ✅ pow()

* `pow(x, y)` → x raised to power y
* `pow(x, y, z)` → (x^y) % z

Example:

```python
pow(3,4)      # 81
pow(3,4,5)    # 1
```

---

## ✅ abs()

* Returns absolute (positive) value.

```python
abs(-3.14)   # 3.14
```

---

## ✅ round()

* Rounds number to given decimal places.

```python
round(3.14159,2)  # 3.14
round(395,-2)     # 400
```

---

# 🔤 2. Advanced Strings

Strings are **immutable** (cannot change directly).

## ✅ Case Methods

* `capitalize()`
* `upper()`
* `lower()`

These return new strings.

---

## ✅ Searching Methods

* `count()` → Count occurrences
* `find()` → Find first index
* `endswith()` → Check last character

---

## ✅ Check Methods (Return True/False)

* `isalnum()`
* `isalpha()`
* `islower()`
* `isupper()`
* `isspace()`
* `istitle()`

---

## ✅ Formatting

* `center()`
* `expandtabs()`

---

## ✅ Split & Partition

* `split()` → Returns LIST
* `partition()` → Returns TUPLE

---

# 📚 3. Advanced Lists

Lists are:

* Ordered
* Mutable
* Allow duplicates

---

## ✅ Adding Elements

* `append()` → Add one element
* `extend()` → Add multiple elements
* `insert()` → Insert at position

Difference:

* `append([4,5])` → Adds as one element
* `extend([4,5])` → Adds 4 and 5 separately

---

## ✅ Removing Elements

* `pop()` → Remove by index
* `remove()` → Remove by value
* `clear()` → Remove all

---

## ✅ Other Methods

* `count()` → Count occurrences
* `index()` → Find position
* `reverse()` → Reverse list
* `sort()` → Sort list

⚠ Important:
Most list methods change the list in-place and return `None`.

---

# 🧩 4. Advanced Sets

Sets:

* No duplicates
* Unordered
* Mutable

---

## ✅ Basic Methods

* `add()`
* `clear()`
* `copy()`
* `discard()`

---

## ✅ Set Operations

* `difference()`
* `difference_update()`
* `intersection()`
* `intersection_update()`
* `symmetric_difference()`
* `union()`
* `update()`

---

## ✅ Comparison Methods

* `isdisjoint()` → No common elements?
* `issubset()` → Inside another set?
* `issuperset()` → Contains another set?

---

# 📖 5. Advanced Dictionaries

Dictionaries:

* Key : Value pairs
* Keys must be unique
* Mutable

---

## ✅ Dictionary Comprehension

Create dictionary in one line:

```python
{x: x**3 for x in range(5)}
```

---

## ✅ Iteration

* `keys()`
* `values()`
* `items()`

---

## ✅ View Objects

`keys()`, `values()`, `items()` return view objects.

They update automatically if dictionary changes.
