import pytest
import time
from unittest.mock import patch
from unittest.mock import Mock

from tech_news.collector.scrapper import ( fetch_content, scrape)

from tests.test_collector.faker import RESPONSE
# Caso a requisição seja bem sucedida retorne seu conteúdo de texto;
def test_validar_metodo_fetch_content_quando_status_200():
    teste = fetch_content('https://app.betrybe.com/') 

    assert "Aprenda a programar com uma formação de alta qualidade e só comece a pagar quando conseguir um bom trabalho." in teste

# O tempo máximo de resposta do servidor deve ser configurado como parâmetro e por padrão será 3 segundos;
def test_validar_fetch_retorna_vazio_quando_status_diferente_de_200():
    teste = scrape(fetcher=fetch_content, pages=1) 
    ##print(type(teste))
    print(teste)
    assert RESPONSE == teste, 'deu erro ferrou'

#Caso a resposta tenha o código de status diferente de 200, deve-se retornar uma str vazia;