import pytest

from unittest.mock import patch
from unittest.mock import Mock

from tech_news.collector.scrapper import ( fetch_content, scrape)
from tech_news.database import insert_or_update

def test_validar_fetch_com_sucesso():
    assert 'content=\"Aprenda a programar com uma formação de alta qualidade e só comece a pagar quando conseguir um bom trabalho.\"' in fetch_content('https://app.betrybe.com/')

def test_validar_fetch_com_tempo_maximo_maior_que_3():
    assert "" == fetch_content('https://httpbin.org/delay/10')

def test_validar_fetch_com_status_diferente_de_200():
    assert "" == fetch_content('https://httpbin.org/status/404')

def test_database():
    assert True == insert_or_update({'url': 'https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/206992-2-acidentes-fatais-boeing-737-max-voltar-voar.htm', 'title': 'Após 2 acidentes fatais, Boeing 737 Max já pode voltar a voar', 'timestamp': '2020-11-19T12:00:01', 'writer': ' Nilton Kleina ', 'shares_count': 0, 'comments_count': 0, 'summary': '0', 'sources': [' Anac ', ' Digital Trends '], 'categories': [' Mobilidade Urbana/Smart Cities ', ' Avião ', ' Transporte ']})
