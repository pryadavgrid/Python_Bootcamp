import re


# re.match()
# It checks the pattern only at the beginning of the string.
# It does NOT check the full string.
# It only checks from position 0.

# If match found → returns a Match object
# If not found → returns None

text = "Hello World"
result = re.match("Hello", text)
print(result)




# re.search()
# Searches the entire string for the first match.
# If found → Match object

# If not found → None

text = "My name is Prateek"
result = re.search("Prateek", text)
print(result)




# re.findall()
# Finds all matches in the string.

# Returns a list
# If no match → returns empty list []


text = "My numbers are 10 and 20"
result = re.findall(r"\d+", text)
print(result)




# re.finditer()
# Finds all matches (like findall)
# But returns match objects one by one.

# Returns an iterator
# Each item is a Match object

text = "Price 100 and 200"
result = re.finditer(r"\d+", text)
for match in result:
    print(match.group(), match.start())





# re.sub()
# Replaces matched pattern with new text.

# Returns a new modified string

text = "I love cats"
result = re.sub("cats", "dogs", text)
print(result)





# re.split()
# Splits string using a regex pattern.

# Returns a list

text = "apple,banana;orange"
result = re.split(r"[;,]", text)
print(result)