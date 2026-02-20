from collections import Counter

# Counter is used to count how many times items appear in a list or string.
# It returns a dictionary-like object.

my_list = [1,2,1,4,1,3,1,3,2,4,2,4,3,1]

my_counter_obj = Counter(my_list)

# print(my_counter_obj)

# for key, val in my_counter_obj.items():
#     print(key, val)

my_str = 'abaabaabcabaa'
my_str_counter = Counter(my_str)
print(my_str_counter)
# print(Counter(my_str).most_common()) # return the pair or (key,value) of most common
# print(Counter(my_str).most_common(2)) #  return the pair or (key,value) of 2 most common 

# print(sum(my_str_counter.values())) # Total Of All Count

# my_str_counter.clear() # Reset all Count
# print(my_str_counter)

# print(list(my_str_counter)) # Create a list of unique keys
# print(set(my_str_counter)) # Create a set of keys
# print(dict(my_str_counter)) # convert counter object into dict
my_str_counter_list = my_str_counter.items() # convert to list of  (key,value) pairs
# print(my_str_counter_list)
# print(Counter(dict(my_str_counter_list))) # return a counter object 
# print(my_str_counter.most_common()[ : : -1]) # return reverse most common (key,value) pair




# my_sent = 'How many time does each word show up in this sentence with a word'
# print(Counter(my_sent.split()))



