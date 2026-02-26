# ===============================
# 1. append()
# ===============================

list1 = [1, 2, 3]

list1.append(4)
print("After append(4):", list1)
# [1, 2, 3, 4]


# ===============================
# 2. count()
# ===============================

print("Count of 10:", list1.count(10))  # 0
print("Count of 2:", list1.count(2))    # 1


# ===============================
# 3. extend() vs append()
# ===============================

x = [1, 2, 3]
x.append([4, 5])
print("append([4,5]):", x)
# [1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5])
print("extend([4,5]):", x)
# [1, 2, 3, 4, 5]

"""
Difference:
append() → Adds whole object as single element.
extend() → Adds each element separately.
"""


# ===============================
# 4. index()
# ===============================

list1 = [1, 2, 3, 4]

print("Index of 2:", list1.index(2))  # 1

# If element not found → ValueError
# list1.index(12)  # This will give error


# ===============================
# 5. insert()
# ===============================

list1.insert(2, 'inserted')
print("After insert:", list1)
# [1, 2, 'inserted', 3, 4]


# ===============================
# 6. pop()
# ===============================

ele = list1.pop(1)   # Remove index 1
print("After pop(1):", list1)
print("Popped element:", ele)


# ===============================
# 7. remove()
# ===============================

list1.remove('inserted')
print("After remove('inserted'):", list1)

list2 = [1, 2, 3, 4, 3]
list2.remove(3)
print("Remove first 3:", list2)
# Removes only first occurrence


# ===============================
# 8. reverse()
# ===============================

list2.reverse()
print("After reverse():", list2)


# ===============================
# 9. sort()
# ===============================

list2 = [3, 4, 2, 1]

list2.sort()
print("Sorted list:", list2)

list2.sort(reverse=True)
print("Reverse sorted list:", list2)


# ===============================
# 10. Important: In-Place Methods
# ===============================

"""
List methods like:
append(), extend(), remove(), reverse(), sort()
change the list in-place.

They return None.
"""

x = [1, 2, 3]
y = x.append(4)

print("y after append:", y)  # None
print("x after append:", x)  # [1,2,3,4]


# Correct way using copy()

x = [1, 2, 3]
y = x.copy()

y.append(4)

print("Original x:", x)
print("Modified y:", y)

