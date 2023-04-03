# !/usr/bin/env python3

# scrape the titles and URLs of the latest articles on the TechCrunch website.

import requests
from bs4 import BeautifulSoup

URL: str = "https://techcrunch.com/"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
articles = soup.find_all(
    # define the thing it's looking for
    name="header",
    attrs={
        "class": "post-block__header"
    }
)

for article in articles:
    title = article.find("a", class_="post-block__title__link").text.strip()
    url = article.find("a", class_="post-block__title__link")["href"]
    print(title)
    print(url)
