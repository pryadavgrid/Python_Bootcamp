import requests
import bs4

url = 'https://books.toscrape.com/catalogue/page-{}.html'
result  = requests.get(url)
# print(result)
result  = requests.get(url.format(1))
# print(result.status_code)
# if result.status_code == 200:
#     print('Success')
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# all_div = soup.select('.product_pod')

# # print(all_div)

# for cur_div in all_div:
#     star_rating = cur_div.select('.star-rating.Two')
#     if star_rating:
#         cur_h3 = cur_div.select('h3 a')
#         print(cur_h3[0]['title'])

my_count = 1
while True:
    result  = requests.get(url.format(my_count))
    if result.status_code == 200:
        print("-"*5, f' Page No : {my_count} ', "-"*5 )
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        all_div = soup.select('.product_pod')
        for cur_div in all_div:
            star_rating = cur_div.select('.star-rating.Two')
            if star_rating:
                cur_h3 = cur_div.select('h3 a')
                print(cur_h3[0]['title'])
        print()
        my_count = my_count + 1
        continue
    else:
        break

