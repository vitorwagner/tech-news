# Requisito 1
import requests
import time
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
    except requests.exceptions.Timeout:
        return None
    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    return [
        post.find("a").get("href")
        for post in soup.find_all("article", class_="entry-preview")
    ]


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", class_="next page-numbers")
    if next_page:
        return next_page.get("href")
    return None


# Requisito 4
def scrape_news(html_content):
    news_data = {}
    soup = BeautifulSoup(html_content, "html.parser")
    news_data["url"] = soup.find("link", rel="canonical").get("href")
    news_data["title"] = (
        soup.find("h1", class_="entry-title").get_text().strip(" \xa0")
    )
    news_data["timestamp"] = soup.find("li", class_="meta-date").get_text()
    news_data["writer"] = soup.find("a", class_="url fn n").get_text()
    news_data["summary"] = soup.find("p").get_text().strip(" \xa0")
    news_data["category"] = soup.find("span", class_="label").get_text()

    read_time = soup.find("li", class_="meta-reading-time").get_text()

    news_data["reading_time"] = int(re.findall("[0-9]+", read_time)[0])

    return news_data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []
    while len(news) < amount:
        html_content = fetch(url)
        updates = scrape_updates(html_content)
        news.extend(updates)
        url = scrape_next_page_link(html_content)

    scraped_news = []

    for item in news[:amount]:
        html_content = fetch(item)
        scraped_news.append(scrape_news(html_content))

    create_news(scraped_news)

    return scraped_news
