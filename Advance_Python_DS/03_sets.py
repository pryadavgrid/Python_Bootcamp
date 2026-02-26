# ===============================
# 1. add()
# ===============================

s = set()

s.add(1)
s.add(2)
s.add(2)  # Duplicate, will not be added

print("After add():", s)   # {1, 2}


# ===============================
# 2. clear()
# ===============================

s.clear()
print("After clear():", s)  # set()


# ===============================
# 3. copy()
# ===============================

s = {1, 2, 3}
sc = s.copy()

print("Original set:", s)
print("Copied set:", sc)

s.add(4)

print("After adding 4 to original:")
print("Original set:", s)   # {1,2,3,4}
print("Copied set:", sc)    # {1,2,3}


# ===============================
# 4. difference()
# ===============================

print("difference():", s.difference(sc))
# Elements in s but not in sc → {4}


# ===============================
# 5. difference_update()
# ===============================

s1 = {1, 2, 3}
s2 = {1, 4, 5}

s1.difference_update(s2)

print("difference_update():", s1)
# Removed common elements → {2,3}


# ===============================
# 6. discard()
# ===============================

s = {1, 2, 3, 4}
s.discard(2)

print("After discard(2):", s)  # {1,3,4}

s.discard(10)  # No error if element not present


# ===============================
# 7. intersection()
# ===============================

s1 = {1, 2, 3}
s2 = {1, 2, 4}

print("intersection():", s1.intersection(s2))
# Common elements → {1,2}

print("s1 remains unchanged:", s1)


# ===============================
# 8. intersection_update()
# ===============================

s1.intersection_update(s2)
print("intersection_update():", s1)
# s1 becomes {1,2}


# ===============================
# 9. isdisjoint()
# ===============================

s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print("s1.isdisjoint(s2):", s1.isdisjoint(s2))  # False
print("s1.isdisjoint(s3):", s1.isdisjoint(s3))  # True


# ===============================
# 10. issubset()
# ===============================

print("issubset():", s1.issubset(s2))  # True


# ===============================
# 11. issuperset()
# ===============================

print("issuperset():", s2.issuperset(s1))  # True
print("issuperset():", s1.issuperset(s2))  # False


# ===============================
# 12. symmetric_difference()
# ===============================

s1 = {1, 2}
s2 = {1, 2, 4}

print("symmetric_difference():", s1.symmetric_difference(s2))
# Elements in only one set → {4}


# ===============================
# 13. union()
# ===============================

print("union():", s1.union(s2))
# All elements → {1,2,4}


# ===============================
# 14. update()
# ===============================

s1.update(s2)
print("update():", s1)
# s1 becomes {1,2,4}
