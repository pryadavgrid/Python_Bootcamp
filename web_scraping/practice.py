import requests
import bs4

result = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(result.text, 'lxml')
author_name_set = set({})
list_of_quote = []
# list_of_all_quote = soup.select('.quote')
# print(list_of_all_quote('span')[1].text)
# for quote in list_of_all_quote:
#     author_name = quote.select('span')[1].text.split('\n')[0].replace('by','').strip()
#     author_name_set.add(author_name)

    # quote_text = quote.select('span')[0].text.strip()
    # list_of_quote.append(quote_text)



# print(author_name_set)
# print(list_of_quote)

# top_10_tags = soup.select('.tag-item')
# for tags in top_10_tags:
#     print(tags.text)


page = 1
while True:
    result = requests.get(f'https://quotes.toscrape.com/page/{page}/')
    if result.status_code == 200:
        print(f"{'*'*5} Page : {page} {'*'*5}")
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        list_of_all_quote = soup.select('.quote')
        if list_of_all_quote == []:
            break
        # print(list_of_all_quote('span')[1].text)
        for quote in list_of_all_quote:
            author_name = quote.select('span')[1].text.split('\n')[0].replace('by','').strip()
            author_name_set.add(author_name)

        print()
        page = page + 1
        continue
    else:
        break

print(author_name_set)