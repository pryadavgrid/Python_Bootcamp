# 🌐 Web Scraping in Python (Beginner Friendly Guide)

This README will help you learn **Web Scraping** in simple English.

We will use these libraries:

- `requests` → To get website data
- `lxml` → Fast HTML parser
- `bs4 (BeautifulSoup)` → Easy HTML parser

---

# 📌 What is Web Scraping?

Web scraping means:

👉 Taking data from a website using Python.

Example:
- Get title of a page
- Get all headings
- Get images
- Get product prices

---

# 1️⃣ Setting Up Web Scraping Libraries

## 🔹 Install Libraries

Open terminal and run:

```bash
pip install requests
pip install lxml
pip install beautifulsoup4
````

Or install together:

```bash
pip install requests lxml beautifulsoup4
```

---

## 🔹 Import Libraries

```python
import requests
from bs4 import BeautifulSoup
```

---

# 2️⃣ Python Web Scraping – Grabbing a Title

Let’s grab the title of a webpage.

Example: [https://example.com](https://example.com)

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

print(soup.title)
print(soup.title.text)
```

### 🔎 Explanation

* `requests.get(url)` → Sends request to website
* `response.text` → Gets HTML code
* `BeautifulSoup(..., "lxml")` → Parses HTML
* `soup.title` → Gets title tag
* `.text` → Gets only text

---

# 3️⃣ Important Note on Wikipedia Classes

If you inspect Wikipedia page (Right Click → Inspect),

You will see many classes like:

```html
<div class="mw-parser-output">
```

⚠️ Important:

* Wikipedia classes may change
* Always inspect website before scraping
* Never hardcode without checking HTML

To inspect:

1. Right Click
2. Click Inspect
3. Check tag name and class

---

# 4️⃣ Python Web Scraping – Grabbing a Class

Example: Grab all paragraphs from Wikipedia.

```python
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

content = soup.find("div", class_="mw-parser-output")

paragraphs = content.find_all("p")

for p in paragraphs[:5]:
    print(p.text)
```

### 🔎 Explanation

* `find()` → Finds first matching tag
* `find_all()` → Finds all matching tags
* `class_=` → Used because `class` is Python keyword

---

# 5️⃣ Important Note on How to Grab an Image

Images are inside `<img>` tag.

Example:

```html
<img src="image.jpg">
```

⚠️ Important:

* Sometimes image URL is relative
* Example: `/images/pic.jpg`
* You must add main website URL

Example:

```python
image_url = "https://example.com" + "/images/pic.jpg"
```

---

# 6️⃣ Python Web Scraping – Grabbing an Image

Example: Download image

```python
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

image = soup.find("img")

image_url = image["src"]

if image_url.startswith("//"):
    image_url = "https:" + image_url

img_data = requests.get(image_url).content

with open("image.jpg", "wb") as f:
    f.write(img_data)

print("Image downloaded successfully!")
```

---

# 7️⃣ Python Web Scraping – Book Examples Part One

We will scrape books from:

[http://books.toscrape.com](http://books.toscrape.com)

This website is made for practice.

## 🔹 Get Book Titles

```python
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

books = soup.select(".product_pod h3 a")

for book in books:
    print(book["title"])
```

### 🔎 Explanation

* `.select()` → Uses CSS selector
* `.product_pod` → Class name
* `a["title"]` → Gets title attribute

---

# 8️⃣ Python Web Scraping – Book Examples Part Two

## 🔹 Get Book Price

```python
prices = soup.select(".product_price .price_color")

for price in prices:
    print(price.text)
```

## 🔹 Get Book Rating

Ratings are inside class:

```html
<p class="star-rating Three">
```

```python
ratings = soup.select(".star-rating")

for rating in ratings:
    print(rating["class"])
```

You will get:

```
['star-rating', 'Three']
```

Second value is rating.

---

# 9️⃣ Python Web Scraping – Exercise Overview

Practice:

1. Get all book titles
2. Get books with rating "Five"
3. Download one book image
4. Save titles into a text file
5. Loop through all pages

---

# 🔟 Python Web Scraping – Complete Example

```python
import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 3):

    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    books = soup.select(".product_pod")

    for book in books:

        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        rating = book.p["class"][1]

        print("Title:", title)
        print("Price:", price)
        print("Rating:", rating)
        print("-" * 20)
```

---

# ⚠️ Important Rules for Web Scraping

1. Always check `robots.txt`
2. Do not send too many requests quickly
3. Respect website rules
4. Do not scrape private data
5. Use `time.sleep()` if needed

---

# 📌 Difference Between Libraries

| Library       | Work             |
| ------------- | ---------------- |
| requests      | Get webpage      |
| lxml          | Fast parser      |
| BeautifulSoup | Easy HTML search |

---

# 🎯 Final Summary

Web Scraping Steps:

1. Send request using `requests`
2. Get HTML
3. Parse using `BeautifulSoup`
4. Find tags using `find()` or `select()`
5. Extract data
6. Save data

---

# 🚀 You Learned

✔ How to get title
✔ How to get class content
✔ How to download image
✔ How to scrape books
✔ How to use CSS selectors

