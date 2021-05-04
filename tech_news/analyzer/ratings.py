# Código feito pelo Gleison <3
from tech_news.database import get_collection


def top_5_news():
    top_5 = get_collection().aggregate(
        [
            {
                "$addFields": {
                    "total_shares_and_comments": {
                        "$sum": ["$shares_count", "$comments_count"]
                    }
                },
            },
            {"$sort": {"total_shares_and_comments": -1, "title": 1}},
            {"$limit": 5},
            {"$project": {"_id": False, "title": True, "url": True}},
        ]
    )
    return [(category["title"], category["url"]) for category in top_5]


def top_5_categories():
    top_5 = get_collection().aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "quantity": {"$sum": 1}}},
            {"$sort": {"quantity": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    return [category["_id"] for category in top_5]
