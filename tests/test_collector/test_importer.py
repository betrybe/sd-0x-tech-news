import pytest
from tech_news.collector.importer import csv_importer
from collections import OrderedDict

ORDERER_DICT = [OrderedDict(
    [('url', 'https://www.tecmundo.com.br/mobilidade-urbana.htm'),
        ('title', 'Alemanha já trabalha na regulamentação de carros'),
        ('timestamp', '2020-07-20T15:30:00'),
        ('writer', 'Reinaldo Zaruvni'),
        ('shares_count', '0'),
        ('comments_count', '0'),
        ('summary', 'Recentemente, a Alemanha fez a Tesla pisar no freio'),
        ('sources', 'AutomotiveNewsEurope'),
        ('categories', 'carros')])]


def test_sera_validado_importar_arquivo_invalido_ira_mostrar_erro():
    with pytest.raises(ValueError) as error:
        assert csv_importer('tests/file_incorrect.json')
    assert str(error.value) == 'Formato invalido'


def test_sera_validado_importar_arquivo_inexistente_ira_mostrar_erro():
    with pytest.raises(ValueError) as error:
        assert csv_importer('tests/file_not_exist.csv')
    assert str(error.value) == 'Arquivo file_not_exist.csv não encontrado'


def test_sera_validado_importar_arquivo_com_sucesso():
    assert csv_importer('tests/correct.csv') == ORDERER_DICT
