from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_found = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return list(
        (news_found["title"], news_found["url"]) for news_found in news_found
    )


# Requisito 8
def search_by_date(date):
    try:
        datetime.fromisoformat(date)

        news_found = db.news.find(
            {
                "timestamp": datetime.strptime(date, "%Y-%m-%d").strftime(
                    "%d/%m/%Y"
                )
            }
        )
        return list(
            (news_found["title"], news_found["url"])
            for news_found in news_found
        )
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news_found = db.news.find(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return list(
        (news_found["title"], news_found["url"]) for news_found in news_found
    )
