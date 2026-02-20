# Python `math` and `random` Modules

This guide explains how to use Python's built-in **`math`** and **`random`** modules. These modules help you do mathematical calculations and generate random numbers easily.

---

## 📌 1. Math Module

The `math` module provides many functions to perform **mathematical operations**.

### 🔹 How to Use:

```python
import math
```

### 🔹 Important Functions:

1. **math.sqrt(x)** – Returns the square root of `x`.

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

2. **math.pow(x, y)** – Returns `x` raised to the power of `y`.

```python
print(math.pow(2, 3))  # Output: 8.0
```

3. **math.factorial(x)** – Returns the factorial of `x`.

```python
print(math.factorial(5))  # Output: 120
```

4. **math.ceil(x)** – Rounds `x` up to the nearest integer.

```python
print(math.ceil(4.2))  # Output: 5
```

5. **math.floor(x)** – Rounds `x` down to the nearest integer.

```python
print(math.floor(4.8))  # Output: 4
```

6. **math.gcd(a, b)** – Returns the greatest common divisor of `a` and `b`.

```python
print(math.gcd(12, 18))  # Output: 6
```

7. **math.sin(x), math.cos(x), math.tan(x)** – Trigonometric functions (x in radians).

```python
print(math.sin(math.pi/2))  # Output: 1.0
```

8. **math.log(x, base)** – Returns logarithm of `x` with the given base (default is natural log).

```python
print(math.log(100, 10))  # Output: 2.0
```

---

## 📌 2. Random Module

The `random` module helps you **generate random numbers or select random items**.

### 🔹 How to Use:

```python
import random
```

### 🔹 Important Functions:

1. **random.random()** – Returns a random float number between 0 and 1.

```python
print(random.random())  # Output: 0.374 (example)
```

2. **random.randint(a, b)** – Returns a random integer between `a` and `b` (both inclusive).

```python
print(random.randint(1, 10))  # Output: 7 (example)
```

3. **random.choice(sequence)** – Returns a random element from a list, tuple, or string.

```python
colors = ['red', 'blue', 'green']
print(random.choice(colors))  # Output: 'green' (example)
```

4. **random.shuffle(sequence)** – Shuffles the elements of a list in place.

```python
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: [3, 1, 5, 2, 4] (example)
```

5. **random.sample(sequence, k)** – Returns `k` unique random elements from a sequence.

```python
numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))  # Output: [2, 5, 3] (example)
```

6. **random.uniform(a, b)** – Returns a random float between `a` and `b`.

```python
print(random.uniform(1, 5))  # Output: 3.74 (example)
```

---

## 🔹 Summary

| Module   | Purpose                                                                  |
| -------- | ------------------------------------------------------------------------ |
| `math`   | Performs mathematical operations like sqrt, factorial, trigonometry, log |
| `random` | Generates random numbers, selects random items, shuffles sequences       |

### Example Using Both Modules:

```python
import math
import random

# Random integer between 1 and 10
num = random.randint(1, 10)
print(f"Random Number: {num}")

# Square root using math
sqrt_num = math.sqrt(num)
print(f"Square Root: {sqrt_num}")

# Random choice and factorial
nums = [1, 2, 3, 4, 5]
choice_num = random.choice(nums)
print(f"Random Choice: {choice_num}")
print(f"Factorial: {math.factorial(choice_num)}")
```

Output (example):

```
Random Number: 7
Square Root: 2.6457513110645907
Random Choice: 4
Factorial: 24
```
