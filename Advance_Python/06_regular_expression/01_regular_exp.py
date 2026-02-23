import re

my_text = "This is phone number 9876543210, you can call me"

my_patterrn = "phone"


result = re.search(my_patterrn, my_text) # return only first match data
print(result)
# <re.Match object; span=(8, 13), match='phone'> 

print(result.span()) # retrun a tuple of find index value 
print(result.start()) # return a start index value
print(result.end()) # return a end index value

my_text = "Phone One, Phone Two, Phone Three"
my_patterrn = "Phone"
result = re.findall(my_patterrn, my_text) # it return a list how many PATTERN Match
print(result) # ['Phone', 'Phone', 'Phone']

# re.finditer('PATTERN', 'STRING') return a list of match object 
for i in re.finditer(my_patterrn, my_text):
    print(i)

second_pattern = "My"
print(re.search(second_pattern, my_text)) # Return None if Pattern Dose not match