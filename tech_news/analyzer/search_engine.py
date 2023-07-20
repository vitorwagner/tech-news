from tech_news.database import db


# Requisito 7
def search_by_title(title):
    news_found = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return list(
        (news_found["title"], news_found["url"]) for news_found in news_found
    )


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
