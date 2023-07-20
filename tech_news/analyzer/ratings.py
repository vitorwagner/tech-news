from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()
    categories = {}
    for item in news:
        categories[item["category"]] = categories.get(item["category"], 0) + 1
    categories = sorted(categories.items(), key=lambda x: (-x[1], x[0]))
    return [category[0] for category in categories[:5]]
