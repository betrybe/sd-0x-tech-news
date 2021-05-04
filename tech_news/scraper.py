import requests
from requests.exceptions import ReadTimeout
from tech_news.database import create_news
import parsel
import time
import json


URL_NOVIDADES = "https://www.tecmundo.com.br/novidades"


# Req.1
def fetch(url: str) -> str:
    time.sleep(3)
    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0"
                ")Gecko/20100101 Firefox/87.0",
                "Accept": "text/html",
                "Accept-Encoding": "identity",  # Precisa disso senão buga tudo
                "Accept-Language": "en-US",
                "Referer": "http://www.google.com/",
            },
            timeout=2,
        )
    except ReadTimeout:
        return
    if response.ok:
        return response.text


#  # Use esta função de fetch se estiver testando localmente.
#  # Este mock é o mesmo utilizado pelos testes.
# def fetch(url):
#     path = (
#         "tests/assets/tecmundo_pages/"
#         + url.split('https://www.tecmundo.com.br/')[1].replace('/', '|')
#         + '.html'
#     )
#     with open(path) as f:
#         html_content = f.read()
#     return html_content


# Req.2
def scrape_noticia(html_content: str) -> str:
    selector = parsel.Selector(html_content)

    # url
    scripts = selector.css("script").getall()
    jstring = (
        scripts[-4]
        .split('<script type="application/ld+json">\n    ')[1]
        .split("\n  </script>")[0]
    )
    url = json.loads(jstring)["mainEntityOfPage"]["@id"]

    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    if writer:
        writer = writer.strip()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d+")
    summary = ''.join(selector.css(
        ".tec--article__body p:first-child *::text"
        ).getall())
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count or "0"),
        "comments_count": int(comments_count or "0"),
        "summary": summary,
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }


# Req.3
def scrape_novidades(html_content: str) -> str:
    selector = parsel.Selector(html_content)
    news_urls = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return news_urls


# Req.4
def scrape_next_page_link(html_content: str) -> str:
    selector = parsel.Selector(html_content)
    next_page_url = selector.css(".tec--btn::attr(href)").get()
    # Isto também pode ser feito manualmente alterando a URL;
    # A paginação é feita por um parâmetro de query.
    if next_page_url:
        return next_page_url


# Req.5
def get_tech_news(amount):
    amount = int(amount)
    noticias = []
    next_page = URL_NOVIDADES
    while len(noticias) < amount:
        html_novidades = fetch(next_page)
        lista_de_urls = scrape_novidades(html_novidades)
        if not lista_de_urls:
            raise Exception("Couldnt find anything in there.")
        for url_de_noticia in lista_de_urls:
            if len(noticias) < amount:
                html_noticia = fetch(url_de_noticia)
                dict_noticia = scrape_noticia(html_noticia)
                noticias.append(dict_noticia)
            else:
                break
        next_page = scrape_next_page_link(html_novidades)

    create_news(noticias)
    return noticias
