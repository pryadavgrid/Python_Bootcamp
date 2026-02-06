## What is `try / except / else / finally`?

They are used to **handle errors** (exceptions) in Python.

### Meaning in simple words:

* **try** → write code that *may* cause an error
* **except** → runs **if an error happens**
* **else** → runs **if NO error happens**
* **finally** → runs **always** (error or no error)

---

### How this works:

* If user enters **wrong input** → `except` runs
* If everything is **correct** → `else` runs
* **finally always runs**, no matter what

---


### Explanation:

* **try** → try to open and read file
* **except** → file not found error
* **else** → runs if file is opened successfully
* **finally** → closes the file (always runs)

---

## Short Real-Life Example (Easy to Remember)

Think like this 👇

```
try      → Try to open the door
except   → Door is locked
else     → Door opened successfully
finally  → Leave the place
```

---

## Important Notes (Beginner Friendly)

* `else` runs **only if try succeeds**
* `finally` runs **every time**
* File closing is best done in `finally`

---