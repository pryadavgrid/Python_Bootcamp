## 📌 What is a Decorator in Python?

A **decorator** is a function that adds extra behavior to another function **without changing its original code**.

In simple words:

> A decorator wraps another function and adds extra rules or features.

---

## 🧠 Why We Use Decorators?

We use decorators when we want to:

* Add validation (like age check ✅)
* Add logging (print extra information)
* Add security checks
* Run extra code before or after a function


## 🏗 Structure of a Decorator

Basic structure:

```python
def decorator_name(function):
    def wrapper(*args, **kwargs):
        # extra code
        result = function(*args, **kwargs)
        return result
    return wrapper
```

---

## 🚀 What You Learned

* Functions can be passed as arguments.
* Decorators wrap functions.
* `*args` and `**kwargs` allow flexible arguments.
* `@decorator_name` is syntactic sugar.

