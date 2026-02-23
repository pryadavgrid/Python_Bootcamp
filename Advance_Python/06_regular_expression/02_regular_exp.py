import re

my_text = "My Phone Number Is 987-654-3210"
result = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', my_text)

print(result) # return match data as object

print(result.group()) # return the match string/number

using_quantifire = re.search(r'\d{3}-\d{3}-\d{4}', my_text)
print(using_quantifire.group())

using_compile = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # create a compile object
result_compile = re.search(using_compile,my_text)
print(result_compile.group())
print(result_compile.group(1)) # return a first indexing value of group
print(result_compile.groups()) # return a tuple of group

