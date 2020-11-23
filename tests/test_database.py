from tech_news.database import insert_or_update
from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news

NEW_NOTICE = {'url': 'https://www.tecmundo.com.br/voxel/'
              '207137-yakuza-like-dragon-beat-'
              'up-brincadeira-levada-serio.htm',
              'title': 'Yakuza Like a Dragon era beat em up,'
              ' mas brincadeira foi levada a sério',
              'timestamp': '2020-11-23T11:00:01',
              'writer': ' André Luis Dias Custodio ',
              'shares_count': 0, 'comments_count': 0, 'summary': '0',
              'sources': [' ResetEra '],
              'categories': [' Voxel ', ' Jogos ', ' Plataformas ',
                             ' PC ', ' Console ', ' Xbox Series S ',
                             ' Xbox Series X ', ' PS5 ', ' PS4 ']}

NEW_UPDATE_NOTICE = {'url': 'https://www.tecmundo.com.br/mercado/207153'
                     '-realme-quer-fabricar-celulares-brasil.htm',
                     'title': 'Realme quer fabricar celulares no Brasil',
                     'timestamp': '2020-11-23T10:49:41',
                     'writer': ' Mateus Mognon ', 'shares_count': 0,
                     'comments_count': 0, 'summary': '0',
                     'sources': [' Mobile Time '],
                     'categories': [' Mercado ', ' Realme ',
                                    ' Celular ']}


def test_sera_valiado_que_e_possivel_inserir_noticia_no_banco_com_sucesso():
    db.news.delete_many({})
    assert True is insert_or_update(NEW_NOTICE)


def test_sera_valiado_que_e_possivel_atualizar_noticia_no_banco_com_sucesso():
    db.news.delete_many({})
    insert_or_update(NEW_NOTICE)
    assert True is insert_or_update(NEW_UPDATE_NOTICE)

def test_sera_valiado_que_e_nao_possivel_inserir_a_mesma_noticia():
    db.news.delete_many({})
    insert_or_update(NEW_NOTICE)
    assert False is insert_or_update(NEW_NOTICE)
