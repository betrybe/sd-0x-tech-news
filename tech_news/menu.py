import sys

# from tech_news.collector.importer import csv_importer
# from tech_news.collector.exporter import csv_exporter
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories


from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

message_collector = (
    "Selecione uma das opções a seguir:\n "
    + "1 - Importar notícias a partir de um arquivo CSV;\n "
    + "2 - Exportar notícias para CSV;\n "
    + "3 - Raspar notícias online;\n "
    + "4 - Sair.\n"
)

message_analyzer = (
    "Selecione uma das opções a seguir:\n "
    + "0 - Popular o banco com notícias;\n "
    + "1 - Buscar notícias por título;\n "
    + "2 - Buscar notícias por data;\n "
    + "3 - Buscar notícias por fonte;\n "
    + "4 - Buscar notícias por categoria;\n "
    + "5 - Listar top 5 notícias;\n "
    + "6 - Listar top 5 categorias;\n "
    + "7 - Sair."
)


def wrapper(*messages, func):
    return func(*[input(message) for message in messages])


# def collector_menu():
#     answer = input(message_collector)
#     result = "Opção inválida"
#     if answer == "1":
#         filepath = input("Coloque o caminho do arquivo: ")
#         result = csv_importer(filepath)
#         create_news(result)
#     elif answer == "2":
#         filepath = input("Coloque o caminho do arquivo: ")
#         csv_exporter(filepath)
#         result = "Exportado"
#     elif answer == "3":
#         result = scrape(fetcher=fetch_content, pages=1)
#         create_news(result)
#     elif answer == "4":
#         result = "Encerrando script"
#     else:
#         print(result, file=sys.stderr)
#     print(result)


menu_of_analyzer = {
    "0": lambda: wrapper(
        "Digite a quantidade de notícias:", func=get_tech_news
    ),
    "1": lambda: wrapper("Digite o título:", func=search_by_title),
    "2": lambda: wrapper(
        "Digite a data no formato aaaa-mm-dd:", func=search_by_date
    ),
    "3": lambda: wrapper("Digite a fonte:", func=search_by_source),
    "4": lambda: wrapper("Digite a categoria:", func=search_by_category),
    "5": lambda: top_5_news(),
    "6": lambda: top_5_categories(),
    "7": lambda: "Encerrando script",
}


def analyzer_menu():
    answer = input(message_analyzer)
    result = "Opção inválida"
    if answer in menu_of_analyzer.keys():
        result = menu_of_analyzer[answer]()
    else:
        print(result, file=sys.stderr)
    print(result)
