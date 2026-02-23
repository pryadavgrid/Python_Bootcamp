# ⏱️ Measuring Function Execution Time in Python

Using `time` Module and `timeit` Module

---

# 📌 Why Measure Time?

Sometimes we want to know:

* How fast our function runs
* Which code is faster
* How to optimize performance

Python gives us two main modules:

* `time` → Simple timing
* `timeit` → Accurate timing (Best for benchmarking)

---

# 1️⃣ Using `time` Module

## 📦 Import

```python
import time
```

---

## 🔹 Method: `time.time()`

### 📖 What it does?

* Returns current time in **seconds**
* Time is counted from **January 1, 1970 (UTC)**

---

## ✅ Example

```python
import time

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

start = time.time()      # Start time
my_function()
end = time.time()        # End time

print("Execution Time:", end - start)
```

---

## 🧠 How it works?

| Step                  | Meaning          |
| --------------------- | ---------------- |
| `start = time.time()` | Save start time  |
| `end = time.time()`   | Save end time    |
| `end - start`         | Total time taken |

---

## ⚠️ Problem with `time` Module

* Not very accurate
* Result changes every time
* System processes can affect timing

👉 Good for simple timing
👉 Not best for performance comparison

---

# 2️⃣ Using `timeit` Module (Recommended ✅)

`timeit` is made specially for measuring execution time.

It runs your code many times and gives **average time**.

---

## 📦 Import

```python
import timeit
```

---

# 🔹 Method: `timeit.timeit()`

---

## 🧾 Syntax

```python
timeit.timeit(stmt, setup, timer, number, globals)
```

Now we explain every parameter in simple English 👇

---

# 📘 Parameters Explanation

---

## 1️⃣ `stmt` (Statement)

🔹 What is it?

* The code you want to measure
* Must be given as **string**

Example:

```python
stmt = "my_function()"
```

---

## 2️⃣ `setup`

🔹 What is it?

* Code that runs **before timing starts**
* Used for importing modules or defining functions

Example:

```python
setup = "from __main__ import my_function"
```

If not needed → default is `"pass"`

---

## 3️⃣ `timer`

🔹 What is it?

* Function used for timing
* Default: `time.perf_counter()`
* Very accurate timer

👉 Normally you do NOT change this.

---

## 4️⃣ `number`

🔹 What is it?

* How many times the code will run
* Default: 1,000,000 times (if not given in CLI)
* In function default is 1

Example:

```python
number=1000
```

Means: run code 1000 times.

---

## 5️⃣ `globals`

🔹 What is it?

* Used to pass global variables
* Needed when your function is already defined

Example:

```python
globals=globals()
```

---

# ✅ Full Example Using `timeit`

```python
import timeit

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

execution_time = timeit.timeit(
    stmt="my_function()",
    setup="from __main__ import my_function",
    number=100
)

print("Execution Time:", execution_time)
```

---

# 🧠 Another Better Way (Using lambda)

You can avoid strings:

```python
import timeit

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

execution_time = timeit.timeit(
    lambda: my_function(),
    number=100
)

print("Execution Time:", execution_time)
```

👉 This is cleaner and safer.

---

# 🔥 Using `timeit` from Command Line

```bash
python -m timeit "sum(range(100))"
```

---

# 📊 Comparison: `time` vs `timeit`

| Feature                      | `time` Module   | `timeit` Module |
| ---------------------------- | --------------- | --------------- |
| Easy to use                  | ✅ Yes           | ✅ Yes           |
| Accuracy                     | ❌ Less accurate | ✅ Very accurate |
| Runs multiple times          | ❌ No            | ✅ Yes           |
| Best for benchmarking        | ❌ No            | ✅ Yes           |
| Affected by system processes | Yes             | Less            |

---

# 🎯 When to Use What?

### ✅ Use `time` when:

* Just want rough idea
* Simple debugging

### ✅ Use `timeit` when:

* Comparing two functions
* Measuring performance
* Optimization

---

# 📌 Example: Compare Two Methods

```python
import timeit

code1 = "sum([i for i in range(1000)])"
code2 = "sum(range(1000))"

t1 = timeit.timeit(code1, number=10000)
t2 = timeit.timeit(code2, number=10000)

print("List comprehension:", t1)
print("Range directly:", t2)
```

👉 You will see `sum(range())` is faster.

---

# 🏁 Final Conclusion

* `time` → Simple stopwatch ⏱️
* `timeit` → Professional benchmarking tool 🚀

For learning and performance testing →
✅ Always prefer **timeit**

---