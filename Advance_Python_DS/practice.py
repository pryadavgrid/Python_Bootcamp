# ===============================
# Advanced Numbers
# ===============================

# Problem 1:
# Convert 1024 to binary and hexadecimal

print("Binary of 1024:", bin(1024))
print("Hexadecimal of 1024:", hex(1024))

"""
Answer:
Binary → 0b10000000000
Hex    → 0x400
"""


# Problem 2:
# Round 5.23222 to two decimal places

print("Rounded value:", round(5.23222, 2))

"""
Answer:
5.23
round(number, digits)
"""


# ===============================
# Advanced Strings
# ===============================

# Problem 3:
# Check if all letters are lowercase

s = 'hello how are you Mary, are you feeling okay?'

print("Is lower case?:", s.islower())

"""
Answer:
False
Because 'Mary' contains uppercase 'M'
"""


# Problem 4:
# Count how many times 'w' appears

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print("Count of 'w':", s.count('w'))

"""
Answer:
12
"""


# ===============================
# Advanced Sets
# ===============================

set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}

# Problem 5:
# Elements in set1 but not in set2

print("Difference:", set1.difference(set2))

"""
Answer:
{2}
"""


# Problem 6:
# Elements in either set

print("Union:", set1.union(set2))

"""
Answer:
{1, 2, 3, 5, 6, 7, 8}
"""


# ===============================
# Advanced Dictionaries
# ===============================

# Problem 7:
# Create dictionary using comprehension

cube_dict = {x: x**3 for x in range(5)}

print("Cube Dictionary:", cube_dict)

"""
Answer:
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
"""


# ===============================
# Advanced Lists
# ===============================

# Problem 8:
# Reverse the list

list1 = [1, 2, 3, 4]
list1.reverse()

print("Reversed List:", list1)

"""
Answer:
[4, 3, 2, 1]
"""


# Problem 9:
# Sort the list

list2 = [3, 4, 2, 5, 1]
list2.sort()

print("Sorted List:", list2)

"""
Answer:
[1, 2, 3, 4, 5]
"""
