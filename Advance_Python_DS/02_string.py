# ===============================
# 1. Changing Case
# ===============================

s = 'hello world'

# Capitalize first letter
print("capitalize():", s.capitalize())   # Hello world

# Convert to uppercase
print("upper():", s.upper())             # HELLO WORLD

# Convert to lowercase
print("lower():", s.lower())             # hello world

# Original string is unchanged
print("Original string:", s)

# Reassignment (to change the string permanently)
s = s.upper()
print("After reassignment:", s)

s = s.lower()
print("Back to lowercase:", s)


# ===============================
# 2. Location and Counting
# ===============================

s = 'hello world'

# Count occurrences (no overlapping)
print("count('o'):", s.count('o'))   # 2

# Find first index of character
print("find('o'):", s.find('o'))     # 4


# ===============================
# 3. Formatting Methods
# ===============================

# center() method
print("center(20,'z'):", s.center(20, 'z'))
# Output: zzzzhello worldzzzzz

# expandtabs()
print("expandtabs():", 'hello\thi'.expandtabs())


# ===============================
# 4. Check Methods (Boolean)
# ===============================

s = 'hello'

# Check if all characters are alphanumeric
print("isalnum():", s.isalnum())     # True

# Check if all characters are alphabet
print("isalpha():", s.isalpha())     # True

# Check if lowercase
print("islower():", s.islower())     # True

# Check if only whitespace
print("isspace():", s.isspace())     # False

# Check if title case
print("istitle():", s.istitle())     # False

# Check if uppercase
print("isupper():", s.isupper())     # False

# endswith()
print("endswith('o'):", s.endswith('o'))  # True


# ===============================
# 5. Built-in Regular Expression Like Methods
# ===============================

s = 'hello'

# split() - returns list
print("split('e'):", s.split('e'))   # ['h', 'llo']

# partition() - returns tuple
print("partition('l'):", s.partition('l'))
# ('he', 'l', 'lo')
