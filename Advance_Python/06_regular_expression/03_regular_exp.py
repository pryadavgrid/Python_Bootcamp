import re

my_text = "I have a cat"
# | it is or operator  it serch id VALUE_1|VALUE_2 if one value is present then return object
result  = re.search(r'dog|cat', my_text)
print(result)

#  "." (wildcard) is use for when we want what character exsist before match value

result = re.findall(r'.at', 'I have a cat hat and sat')
result = re.findall(r'...at', 'I have a cat and hat and sat')
print(result)

# ^\d return [] number if any string start with a number otherwise return empty []
result = re.findall('^\d', '1 is a number')
result = re.findall('^\d', 'one 1 is a number')
print(result)

result = re.findall('\d$', 'one a number 1')
print(result)

my_str = "One 1, Two 2, Three 3, Four 4"
# whatever we want to exclude, what we want to skip [^\d] mean digit skip
pattern = r'[^\d]'
# return a list of all character and skip digit
print(re.findall(pattern, my_str))

# Give me text that does NOT contain a digit
pattern = r'[^\d]+'
print(re.findall(pattern, my_str))

# Give me text that does NOT contain ! . , ?
# it mean split the string where ! . , ? 
print(re.findall(r'[^!.,?]+', 'One 1 ! two 2 . three 3 ? four ,'))

clear_punc = re.findall(r'[^!,? ]+', 'My name is prateek yadav! and your?')
print(clear_punc)
print(" ".join(clear_punc))


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'

# it mean find the group where \w (mean alphanumeric word) + (mean one or more) - (mean after alphanumeric contain a -) and again \w+
# Mean find a - with contain one or more alphanumeric value and group
# pattern = r'[\w]+-[\w]+'
pattern = r'\w+-\w+'
print(re.findall(pattern, text))


# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

pattern = r'cat\w+'
pattern = r'cat(fish|nap|claw)'

print(re.findall(pattern, text))
# print(re.search(pattern, text))
print(re.findall(pattern, texttwo))
print(re.findall(pattern, textthree))