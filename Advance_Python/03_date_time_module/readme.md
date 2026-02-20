# 📅 Python `datetime` Module

The **`datetime` module** in Python is used to work with **dates and times**. It provides classes for **date**, **time**, **datetime**, and **timedelta** to handle operations like getting the current date/time, formatting, arithmetic, and more.

---

## 🔹 Importing the Module

```python
import datetime
```

Or import specific classes:

```python
from datetime import date, time, datetime, timedelta
```

---

## 🔹 Main Classes

### 1. `date` – Represents a calendar date

**Syntax:**

```python
date(year, month, day)
```

**Example:**

```python
from datetime import date

today = date.today()
print("Today's date:", today)

specific_date = date(2025, 12, 25)
print("Specific date:", specific_date)
```

**Output:**

```
Today's date: 2026-02-19
Specific date: 2025-12-25
```

---

### 2. `time` – Represents time of day

**Syntax:**

```python
time(hour=0, minute=0, second=0, microsecond=0)
```

**Example:**

```python
from datetime import time

t = time(14, 30, 15)  # 2:30:15 PM
print("Time:", t)
```

**Output:**

```
Time: 14:30:15
```

---

### 3. `datetime` – Combines date and time

**Syntax:**

```python
datetime(year, month, day, hour=0, minute=0, second=0)
```

**Example:**

```python
from datetime import datetime

now = datetime.now()
print("Current datetime:", now)

specific_dt = datetime(2025, 12, 25, 10, 30)
print("Specific datetime:", specific_dt)
```

**Output:**

```
Current datetime: 2026-02-19 06:45:32.123456
Specific datetime: 2025-12-25 10:30:00
```

---

### 4. `timedelta` – Represents difference between two dates or times

**Example:**

```python
from datetime import datetime, timedelta

today = datetime.today()
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Last week:", last_week)
```

**Output:**

```
Today: 2026-02-19 06:45:32.123456
Tomorrow: 2026-02-20 06:45:32.123456
Last week: 2026-02-12 06:45:32.123456
```

---

## 🔹 Formatting Dates and Times

Use **`strftime`** to format date/time as string and **`strptime`** to parse string into date/time.

**Example:**

```python
from datetime import datetime

now = datetime.now()

# Formatting
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted datetime:", formatted)

# Parsing
dt_string = "25-12-2025 10:30:00"
parsed_dt = datetime.strptime(dt_string, "%d-%m-%Y %H:%M:%S")
print("Parsed datetime:", parsed_dt)
```

**Output:**

```
Formatted datetime: 19-02-2026 06:45:32
Parsed datetime: 2025-12-25 10:30:00
```

**Common `strftime` directives:**

| Directive | Meaning         | Example |
| --------- | --------------- | ------- |
| `%Y`      | Year (4 digits) | 2026    |
| `%m`      | Month (01-12)   | 02      |
| `%d`      | Day (01-31)     | 19      |
| `%H`      | Hour (24-hour)  | 06      |
| `%I`      | Hour (12-hour)  | 06      |
| `%M`      | Minute (00-59)  | 45      |
| `%S`      | Second (00-59)  | 32      |
| `%p`      | AM/PM           | AM      |

---

## 🔹 Comparison and Operations

You can compare dates or do arithmetic:

```python
from datetime import date, timedelta

d1 = date(2026, 2, 19)
d2 = date(2026, 3, 1)

print("d1 < d2:", d1 < d2)

diff = d2 - d1
print("Difference in days:", diff.days)
```

**Output:**

```
d1 < d2: True
Difference in days: 10
```

---

## 🔹 Summary

* **`date`** → Only date (year, month, day)
* **`time`** → Only time (hour, minute, second)
* **`datetime`** → Date + Time
* **`timedelta`** → Difference between two dates/times
* **Formatting** → `strftime` and `strptime`

**Use Cases:**

* Logging timestamps
* Scheduling events
* Calculating deadlines
* Date arithmetic in apps

---

This `README.md` can be directly used for documentation in your project.

---
