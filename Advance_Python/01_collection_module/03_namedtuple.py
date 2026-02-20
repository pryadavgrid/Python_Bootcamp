from collections import namedtuple

my_tuple = (1, 2, 'Three', 'Four')
# print(my_tuple[0])
# print(my_tuple[2])

# namedtuple creates a tuple where we can access values using names instead of index.
my_collection_tuple = namedtuple('Users', ['Name', 'Age', 'City'])
# print(my_collection_tuple)

user1 = my_collection_tuple('Prateek', 25 , 'Kanpur')
user2 = my_collection_tuple('Tripathi', 22 , 'Noida')

print(user1)

# Also we can access value using index
print(user1[0])
print(user1.Name)

print(user2)
print(user2.Name)

