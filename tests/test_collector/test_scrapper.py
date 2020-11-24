from tech_news.collector.scrapper import fetch_content


def test_sera_validado_que_fetch_retorna_requisicao_com_sucesso():
    assert 'content=\"Aprenda a programar com uma formação de alta' \
           ' qualidade e só comece a pagar quando conseguir um bom' \
           ' trabalho.\"' in fetch_content('https://app.betrybe.com/')


def test_sera_validado_fetch_com_tempo_de_resposta_maior_que_3():
    assert "" == fetch_content('https://httpbin.org/delay/10')


def test_sera_validado_resposta_fetch_com_status_diferente_de_200():
    assert "" == fetch_content('https://httpbin.org/status/404')

# Requisito 2 scrapper
# - Por padrão deve-se raspar apenas as notícias da primeira página
# - Um número de páginas para serem raspadas pode ser passado para a função.
# - Caso o número de páginas seja definido,
# - deve-se raspar os dados das N primeiras páginas;
# - A função deve retornar uma lista com cada notícia em no seguinte formato.
