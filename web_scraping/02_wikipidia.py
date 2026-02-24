import requests
import bs4

my_url = 'https://en.wikipedia.org/wiki/Swami_Vivekananda'
headers = {
    "User-Agent": "MyPythonApp/1.0 (myemail@example.com)"
}
result = requests.get(my_url, headers=headers)
soup = bs4.BeautifulSoup(result.text, 'lxml')

# select all heading using '.mw-heading' class
# all_heading = soup.select('.mw-heading')
# for heading in all_heading:
#     print(heading.get_text())



image_select_using_class_name = soup.select('.mw-file-description img')
# print(image_select_using_class_name)
no_image = 1
for imges in image_select_using_class_name:
    image_source = f'https:{imges['src']}'
    # print(image_source)
    headers = {
    "User-Agent": "PrateekScraper/1.0 (your_email@example.com)"
}
    image_date = requests.get(image_source, headers=headers)
    # print(image_date)
    with open(f'image_{no_image}.jpg', 'wb') as f:
        f.write(image_date.content)

    no_image = no_image + 1

