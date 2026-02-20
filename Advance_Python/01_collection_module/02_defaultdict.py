from collections import defaultdict

my_dict = {'a' : 1, 'b': 2}
print(my_dict['a'])
print(my_dict['b'])
# print(my_dict['c']) # it gives a error because key 'c' is not present in my_dict

def set_default_value():
    return 'Default Value'

my_collection_dict = defaultdict(set_default_value)
my_collection_dict['b'] = 'B'
my_collection_dict['c'] = 'C'

print(my_collection_dict['b'])
print(my_collection_dict['c'])

# if a key does not exist, it gives a default value instead of error.
print(my_collection_dict['a'])