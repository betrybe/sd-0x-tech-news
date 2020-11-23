import pytest
from tech_news.collector.exporter import csv_exporter
from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news

NEW_NOTICE = {'url': 'https://www.tecmundo.com.br/brincadeira-levada-serio.htm',
              'title': 'Yakuza Like a Dragon era beat em up',
              'timestamp': '2020-11-23T11:00:01',
              'writer': 'André Luis Dias Custodio',
              'shares_count': 0,
              'comments_count': 0,
              'summary': '0',
              'sources': ['ResetEra'],
              'categories': ['Plataformas','PC', 'Console']}

NEW_NOTICE_UPDATE = {'url': 'https://www.tecmundo.com.br/vamos.htm',
                     'title': 'Vamoscomtudo',
                     'timestamp': '2020-11-23T11:00:01',
                     'writer': 'Leonardo',
                     'shares_count': 1,
                     'comments_count': 1,
                     'summary': '0',
                     'sources': ['ResetEra2'],
                     'categories': ['PC', 'Console']}

FILE_CSV = ['url;title;timestamp;writer;shares_count;comments_count;summary;sources;categories\n', 'https://www.tecmundo.com.br/brincadeira-levada-serio.htm;Yakuza Like a Dragon era beat em up;2020-11-23T11:00:01;André Luis Dias Custodio;0;0;0;ResetEra;Plataformas,PC,Console\n']
FILE_CSV_UPDATE = ['url;title;timestamp;writer;shares_count;comments_count;summary;sources;categories\n', 'https://www.tecmundo.com.br/vamos.htm;Vamoscomtudo;2020-11-23T11:00:01;Leonardo;1;1;0;ResetEra2;PC,Console\n']


def test_sera_validado_exportar_arquivo_invalido_ira_mostrar_erro():
    with pytest.raises(ValueError) as error:
        assert csv_exporter('file_incorrect.json')
    assert str(error.value) == 'Formato invalido'
    
    
def test_sera_validado_exportar_arquivo_com_sucesso():
    db.news.delete_many({})
    db.news.insert_one(NEW_NOTICE)
    csv_exporter('export_correct.csv')
    filename = "export_correct.csv"
    with open(filename) as f:
        content = f.readlines()
    assert content == FILE_CSV


def test_sera_validado_atualizar_arquivo_com_mesmo_nome_com_sucesso():
    db.news.delete_many({})
    db.news.insert_one(NEW_NOTICE_UPDATE)
    csv_exporter('export_correct.csv')
    filename = "export_correct.csv"
    with open(filename) as f:
        content = f.readlines()
    assert content == FILE_CSV_UPDATE
