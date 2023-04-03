# !/usr/bin/env python3

# scrape the titles and URLs of the latest articles on the TechCrunch website.

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored

URL: str = "https://techcrunch.com/"


def main() -> None:
    """Goes trough the TechCrunch website and gets
    the title and link of the recent news"""

    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all(
        # Define the thing it's looking for
        name="header",
        attrs={"class": "post-block__header"},
    )

    titles = [
        article.find("a", class_="post-block__title__link").text.strip()
        for article in articles
    ]
    urls = [
        article.find("a", class_="post-block__title__link")["href"]
        for article in articles
    ]

    print_colored(titles, urls)


def print_table(titles: list[str], urls: list[str]) -> None:
    """Prints the titles and urls scrapped in table format

    #### Args:
        - titles (list[str]): Titles scrapped from the URL
        - urls (list[str]): Urls for the articles
    """
    table = zip(titles, urls)
    print(tabulate(table, headers=["Title", "URL"], tablefmt="fancy_grid"))


def print_colored(titles: list[str], urls: list[str]) -> None:
    """Prints the titles and urls scrapped in colored in the terminal

    #### Args:
        - titles (list[str]): Titles scrapped from the URL
        - urls (list[str]): Urls for the articles
    """
    for title, url in zip(titles, urls):
        title = colored(title, "green", attrs=["bold"])
        url = colored(url, "light_blue", attrs=["underline"])

        print(f"- {title}: {url}")


if __name__ == "__main__":
    main()
