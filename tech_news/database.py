from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def insert_or_update(notice):
    """Seu código deve vir aqui"""


def check_duplicates(news):
    """Seu código deve vir aqui"""
