# Código feito pelo Gleison <3
import re
from datetime import datetime
from tech_news.database import get_collection


def search_by_title(title):
    results = get_collection().find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    results = get_collection().find(
        {"timestamp": {"$regex": re.compile(date)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]


def search_by_source(source):
    results = get_collection().find(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]


def search_by_category(category):
    results = get_collection().find(
        {"categories": {"$regex": re.compile(category, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]
