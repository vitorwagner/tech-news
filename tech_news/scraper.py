# Requisito 1
import requests
import time
from bs4 import BeautifulSoup


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.exceptions.Timeout:
        return None
    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    posts = []
    for post in soup.find_all("article", class_="entry-preview"):
        posts.append(post.find("a").get("href"))
    return posts


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", class_="next page-numbers")
    if next_page:
        return next_page.get("href")
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
