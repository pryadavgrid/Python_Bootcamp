import requests
import bs4
import lxml 

my_url = 'http://example.com'
result = requests.get(my_url)

# return class 
# print(type(result))

# return status code
# print(result)

# return the result as text format
# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'html.parser')
# print(soup)

# select title tag and return a list
print(soup.select('title'))
print(soup.select('p'))

# For get text from first p tag
p_text = soup.select('p')[0].get_text()
print(p_text)
