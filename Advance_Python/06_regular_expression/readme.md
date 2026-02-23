# 📘 Regular Expressions (Regex) in Python

## 📌 Introduction

Regular Expression (Regex) is a special pattern used to search, match, and manipulate text.

In Python, we use the built-in module:

```
re
```

Regex is useful when:

* Checking email format
* Validating phone numbers
* Searching words in text
* Replacing text
* Extracting specific data

---

# 📦 Importing re Module

```python
import re
```

---

# 🔹 Most Common Functions in re Module

---

## 1️⃣ re.match()

### 👉 What it does:

Checks for a match **only at the beginning** of the string.

### ✅ Syntax:

```python
re.match(pattern, string)
```

### ✅ Example:

```python
import re

text = "Hello World"

result = re.match("Hello", text)

if result:
    print("Matched!")
```

✔ It matches because "Hello" is at the start.

❌ It will NOT match if pattern is not at the beginning.

---

## 2️⃣ re.search()

### 👉 What it does:

Searches the entire string and returns the **first match**.

### ✅ Syntax:

```python
re.search(pattern, string)
```

### ✅ Example:

```python
import re

text = "My email is test@gmail.com"

result = re.search("gmail", text)

if result:
    print("Found!")
```

✔ It finds "gmail" anywhere in the string.

---

## 3️⃣ re.findall()

### 👉 What it does:

Returns **all matches** as a list.

### ✅ Syntax:

```python
re.findall(pattern, string)
```

### ✅ Example:

```python
import re

text = "My numbers are 10, 20 and 30"

numbers = re.findall(r"\d+", text)

print(numbers)
```

### 🔎 Output:

```
['10', '20', '30']
```

✔ `\d+` means:

* `\d` → digit
* `+` → one or more

---

## 4️⃣ re.finditer()

### 👉 What it does:

Returns an iterator of match objects.

### ✅ Example:

```python
import re

text = "Price is 100 and 200"

for match in re.finditer(r"\d+", text):
    print(match.group(), "at position", match.start())
```

✔ Useful when you need position of match.

---

## 5️⃣ re.sub()

### 👉 What it does:

Replaces matched pattern with new text.

### ✅ Syntax:

```python
re.sub(pattern, replacement, string)
```

### ✅ Example:

```python
import re

text = "I love cats"

new_text = re.sub("cats", "dogs", text)

print(new_text)
```

### 🔎 Output:

```
I love dogs
```

---

## 6️⃣ re.split()

### 👉 What it does:

Splits string using a pattern.

### ✅ Example:

```python
import re

text = "apple,banana;orange"

result = re.split(r"[;,]", text)

print(result)
```

### 🔎 Output:

```
['apple', 'banana', 'orange']
```

✔ `[;,]` means split on comma OR semicolon.

---

# 🔤 Most Common Regex Patterns

---

## 🔹 1. Basic Characters

| Pattern | Meaning                      |
| ------- | ---------------------------- |
| `.`     | Any character except newline |
| `^`     | Start of string              |
| `$`     | End of string                |

---

## 🔹 2. Character Classes

| Pattern | Meaning                           |
| ------- | --------------------------------- |
| `\d`    | Digit (0–9)                       |
| `\D`    | Not a digit                       |
| `\w`    | Word character (a-z, A-Z, 0-9, _) |
| `\W`    | Not word character                |
| `\s`    | Whitespace                        |
| `\S`    | Not whitespace                    |

---

## 🔹 3. Quantifiers

| Pattern | Meaning               |
| ------- | --------------------- |
| `*`     | 0 or more             |
| `+`     | 1 or more             |
| `?`     | 0 or 1                |
| `{n}`   | Exactly n times       |
| `{n,m}` | Between n and m times |

---

## 🔹 4. Groups

### 🔸 Parentheses `()`

Used to create groups.

Example:

```python
import re

text = "My number is 9876543210"

match = re.search(r"(\d{10})", text)

print(match.group())
```

---

## 🔹 5. OR Operator `|`

```python
import re

text = "cat"

result = re.search("cat|dog", text)

print(result.group())
```

✔ Matches either "cat" OR "dog"

---

# 📧 Example: Email Validation

```python
import re

email = "test@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
```

---

# 📱 Example: Phone Number (10 digits)

```python
import re

phone = "9876543210"

if re.match(r"^\d{10}$", phone):
    print("Valid phone number")
```

---

# 🧠 Match Object Methods

When using `match()` or `search()`:

| Method    | Meaning                |
| --------- | ---------------------- |
| `group()` | Returns matched text   |
| `start()` | Start index            |
| `end()`   | End index              |
| `span()`  | Start and end position |

Example:

```python
import re

text = "Python is fun"

match = re.search("fun", text)

print(match.group())
print(match.start())
print(match.end())
```

---

# 🚀 Why Use Raw String (r"")

Always write patterns like this:

```
r"\d+"
```

Because:

* `\` is special in Python
* `r""` treats it as raw string

---

# 🎯 Summary

Regular Expressions help you:

✔ Search text
✔ Validate input
✔ Extract data
✔ Replace text
✔ Clean data

Most Common Functions:

* `re.match()`
* `re.search()`
* `re.findall()`
* `re.finditer()`
* `re.sub()`
* `re.split()`

---

| Function        | Meaning                           | Returns                   |
| --------------- | --------------------------------- | ------------------------- |
| `re.match()`    | Match at beginning only           | Match object or None      |
| `re.search()`   | Search whole string (first match) | Match object or None      |
| `re.findall()`  | Find all matches                  | List                      |
| `re.finditer()` | Find all matches with position    | Iterator of Match objects |
| `re.sub()`      | Replace pattern                   | New string                |
| `re.split()`    | Split string                      | List                      |


