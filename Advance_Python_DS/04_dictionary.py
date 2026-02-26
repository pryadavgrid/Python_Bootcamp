# ===============================
# 1. Dictionary Comprehension
# ===============================

# Create dictionary where:
# key = number
# value = square of number

squares = {x: x**2 for x in range(10)}

print("Dictionary Comprehension Result:")
print(squares)

# Output:
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}


# ===============================
# 2. Iteration over keys, values, items
# ===============================

d = {'k1': 1, 'k2': 2}

print("\nIterating over keys:")
for k in d.keys():
    print(k)

print("\nIterating over values:")
for v in d.values():
    print(v)

print("\nIterating over items (key, value pair):")
for item in d.items():
    print(item)


# ===============================
# 3. Viewing keys(), values(), items()
# ===============================

key_view = d.keys()

print("\nKeys view object:")
print(key_view)

# Add new key
d['k3'] = 3

print("\nDictionary after adding new key:")
print(d)

print("\nKeys view object after modification:")
print(key_view)
