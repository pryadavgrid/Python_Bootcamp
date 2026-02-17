

# Python Functions

## 📌 What is a Function?

A **function** is a block of code that runs when we call it.

We use functions to:

* Avoid repeating code
* Make code clean and organized
* Reuse logic many times

---

## 🧩 Basic Function Syntax

```python
def function_name():
    print("Hello World")
```

### ▶ Calling the function

```python
function_name()
```

---

## 📥 Function With Parameters

Parameters are inputs to a function.

```python
def greet(name):
    print(f"Hello {name}")
```

### Call:

```python
greet("Prateek")
```

---

## 📤 Function With Return Value

A function can return a result using `return`.

```python
def add(a, b):
    return a + b
```

### Call:

```python
result = add(5, 3)
print(result)
```

---

## 🔁 Default Parameters

We can give default values.

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

---

## ⭐ Generator Function (Important)

### 📌 What is a Generator?

A **generator** is a special function that:

* Uses the `yield` keyword
* Returns values one by one
* Does NOT store all values in memory

It is useful when working with:

* Large data
* Loops
* Memory saving programs

---

## 🔹 Normal Function vs Generator

### Normal Function

```python
def numbers():
    return [1, 2, 3]
```

It returns everything at once.

---

### Generator Function

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

It gives one value at a time.

---

## ▶ Using a Generator

```python
for num in numbers():
    print(num)
```

---

## 🧠 Simple Meaning of Generator

👉 A generator is like a machine that gives one item at a time
instead of giving all items together.

It saves memory and is good for large data.

---

## 📌 When to Use Generator?

Use generator when:

* You have a large loop
* You don't want to store all values
* You want better performance

---

## 🚀 Summary

| Type               | Uses                      | Memory           |
| ------------------ | ------------------------- | ---------------- |
| Normal Function    | Returns full result       | Uses more memory |
| Generator Function | Gives one value at a time | Uses less memory |

---

# 📦 Why Generator Saves Memory?

Example:

```python
def big_list():
    return [x for x in range(1000000)]
```

This creates 1 million numbers in memory.

Now generator:

```python
def big_generator():
    for x in range(1000000):
        yield x
```

This creates only one number at a time.

👉 Very memory efficient
👉 Very useful for large data

---

# 🏭 Real-Life Example

Think like:

🏭 Factory machine

* Normal function → gives 1000 bottles at once
* Generator → gives one bottle when you ask

Generator works only when needed.

---

# 🔹 Generator Expression (Short Form)

Like list comprehension:

```python
nums = (x for x in range(5))
```


# 🔁 What is a Recursive Function?

A **recursive function** is a function that **calls itself**.

👉 It repeats itself until a condition becomes false.

---

# 🧠 Important Rule

Every recursive function must have:

1. ✅ **Base Case** → Condition to stop recursion
2. ✅ **Recursive Case** → Function calling itself

Without base case ❌
It will run forever (infinite recursion).

---

# 🔹 Simple Example – Countdown

```python
def countdown(n):
    if n == 0:          # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)   # Recursive call
```

### Call:

```python
countdown(5)
```

### Output:

```
5
4
3
2
1
Done!
```

---

# 🏗 Real-Life Example

Think like:

🪞 Mirror facing mirror

Each mirror shows another mirror
Until there is no mirror (base case)

---
