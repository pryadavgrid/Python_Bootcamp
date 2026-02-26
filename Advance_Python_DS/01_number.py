# ===============================
# 1. Hexadecimal
# ===============================

print("Hex of 246:", hex(246))   # 0xf6
print("Hex of 512:", hex(512))   # 0x200

"""
hex(number)
- Converts integer to hexadecimal format
- Output starts with '0x'
"""


# ===============================
# 2. Binary
# ===============================

print("Binary of 1234:", bin(1234))   # 0b10011010010
print("Binary of 128:", bin(128))     # 0b10000000
print("Binary of 512:", bin(512))     # 0b1000000000

"""
bin(number)
- Converts integer to binary format
- Output starts with '0b'
"""


# ===============================
# 3. Exponentials (Power)
# ===============================

print("3^4:", pow(3, 4))        # 81
print("(3^4) % 5:", pow(3, 4, 5))  # 1

"""
pow(x, y)
- Returns x raised to power y

pow(x, y, z)
- Returns (x^y) % z
- More efficient for large numbers
"""


# ===============================
# 4. Absolute Value
# ===============================

print("Absolute of -3.14:", abs(-3.14))  # 3.14
print("Absolute of 3:", abs(3))          # 3

"""
abs(number)
- Returns positive value
- Works with int and float
"""


# ===============================
# 5. Round
# ===============================

print("round(3,2):", round(3, 2))  # 3
print("round(395,-2):", round(395, -2))  # 400
print("round(3.1415926535,2):", round(3.1415926535, 2))  # 3.14

"""
round(number, digits)

digits:
- Positive → decimal places
- 0 (default) → nearest integer
- Negative → round to tens, hundreds, etc.

Example:
round(395, -2)
→ Rounds to nearest 100
→ 400
"""


# ===============================
# Extra Note: math module
# ===============================

"""
Python also has a built-in math module.

Example:
import math
math.sqrt(16)
math.factorial(5)
math.pi

Use it when you need advanced mathematical operations.
"""
