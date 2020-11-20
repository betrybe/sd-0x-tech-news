# Boas vindas ao repositório do projeto de Tech News!

Você já usa o _GitHub_ diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone git@github.com:tryber/sd-0x-tech-news.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-tech-news`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

4. Crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-tech-news`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto tech-news'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no _GitHub_](https://github.com/tryber/sd-0x-tech-news/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-tech-news/pulls) e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter o diretório `tech_news` e o diretório `tests` com seus respectivos arquivos, que conterão seu código `Python` e seus testes, respectivamente.

### 🚨 É importante que seus arquivos tenham exatamente estes nomes!

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [_Git & GitHub_](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

Para fixar o conteúdo sobre Python visto até agora, você fará um projeto que tem como principal objetivo criar um banco de dados de notícias sobre tecnologia e realizar algumas consultas nas notícias registradas.

Essas notícias podem ser obtidas de diferentes formas. Sendo elas:

- Através da importação de um arquivo `CSV`;

- E através da raspagem das [últimas notícias do _TecMundo_](https://www.tecmundo.com.br/novidades).

Além de importar ou raspar as notícias, também deve ser possível exportá-las e realizar buscas ou análises nas notícias coletadas. **Ou seja: desenvolva um sistema capaz de importar, exportar notícias e que faça raspagem e preenchimento de um banco de dados com notícias.**

Legal, não é?

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── dev-requirements.txt
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
├── tech_news
│   ├── analyzer
│   │   ├── ratings.py
│   │   └── search_engine.py
│   ├── collector
│   │   ├── exporter.py
│   │   ├── importer.py
│   │   └── scrapper.py
│   ├── database.py
│   └── menu.py
└── tests
    ├── __init__.py
    ├── test_analyzer
    │   ├── test_ratings.py
    │   └── test_search_engine.py
    ├── test_collector
    │   ├── test_exporter.py
    │   ├── test_importer.py
    │   └── test_scrapper.py
    └── test_menu.py
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar as funções. Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

O arquivo `dev-requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```
---

## Dados

### Importação e exportação de CSV

Os arquivos CSV devem seguir o modelo abaixo, utilizando ponto e vírgula (`;`) como separador:

```csv
url;title;timestamp;writer;shares_count;comments_count;summary;sources;categories
https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155348-alemanha-trabalha-regulamentacao-carros-autonomos.htm;Alemanha já trabalha na regulamentação de carros autônomos;2020-07-20T15:30:00;Reinaldo Zaruvni;0;0;Recentemente, a Alemanha fez a Tesla “pisar no freio” quanto ao uso de termos comerciais relacionados a carros autônomos, mas quem pensa que esse é um sinal de resistência à introdução de novas tecnologias se engana. Isso porque, de acordo o Automotive News Europe, o país está se preparando para se tornar o primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos de nível 4.;The Next Web,The Next Web,Automotive News Europe;Mobilidade Urbana/Smart Cities,Veículos autônomos,Carro,Política
```
📌 Fique atento à maneira que os dados estão dispostos, como por exemplo, `sources` e `categories` serão armazenados separados por `,` e `comments_count` e `shares_count` são numéricos.

### Raspagem de notícias

As notícias a serem raspadas estarão disponíveis na aba de últimas notícias do _TecMundo_: https://www.tecmundo.com.br/novidades.

Essas notícias devem ser salvas no banco de dados, utilizando os mesmos atributos já descritos na importação/exportação citada anteriormente.

### MongoDB

Para a realização deste projeto utilizaremos um banco de dados chamado `tech_news` e as notícias serão armazenadas em uma coleção chamada `news`.

---

## Requisitos obrigatórios:

### Pacote `tech_news/collector`

#### 1- Deve haver uma função chamada `fetch_content` no arquivo `tech_news/collector/scrapper.py` capaz de realizar uma requisição HTTP e retornar o conteúdo como resposta.

##### As seguintes verificações serão feitas:

- Caso a resposta tenha o código de status diferente de `200`, deve-se retornar uma `str` vazia;

- O tempo máximo de resposta do servidor deve ser configurado como parâmetro e por padrão será `3` segundos;

- Para evitar um problema de [Rate Limit](https://app.betrybe.com/course/computer-science/python/raspagem-dados#alguns-problemas) faça um sleep com tempo obtido por parâmetro, mas que por padrão seja `0.5` segundos;

- Caso a requisição seja bem sucedida retorne seu conteúdo de texto;

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/collector/scrapper.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `fetch_content("https://app.betrybe.com/")`.

#### 2 - Deve haver uma função `scrape` dentro do módulo `tech_news/collector/scrapper.py` capaz de raspar as últimas notícias das N primeiras páginas.

Utilizar os seguintes atributos:

* `url` - link para acesso da notícia. Ex: "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"

* `title` - título da notícia. Ex: "Musk: Tesla está muito perto de carros totalmente autônomos"

* `timestamp` - data e hora da notícia. Ex: "2020-07-09T11:00:00"

* `writer` - autor da notícia. Ex: "Nilton Kleina"

* `shares_count` - número de compartilhamento da notícia. Ex: 61

* `comments_count` - número de comentários que a notícia recebeu. Ex: 26

* `summary` - o primeiro parágrafo da notícia. Ex:"O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado."

* `sources` - fontes da notícia. Ex: ["Venture Beat"]

* `categories` - categorias que classificam a notícia. Ex: ["Mobilidade Urbana/Smart Cities", "Veículos autônomos", "Tesla", "Elon Musk"]

**Dica:** Caso uma tag possua outras tags aninhadas, para obter todos os textos da tag ancestral e de suas tags descendentes, utilize `*::text` no seletor.

**Exemplo:**

```html
<p>
  Recentemente, a Alemanha fez a
  <a
    href="https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    rel="noopener noreferrer"
    target="_blank"
    >Tesla</a
  >
  “pisar no freio” quanto ao uso de termos comerciais relacionados a carros
  autônomos, mas quem pensa que esse é um sinal de resistência à introdução de
  novas tecnologias se engana. Isso porque, de acordo o
  <em>Automotive News Europe</em>, o país está se preparando para se tornar o
  primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos
  de nível 4.
</p>
```

Repare que no exemplo dentro da tag _p_ encontram-se duas outras tags. Esse é um caso onde a tag _p_ é um ancestral e as tags _a_ e _em_ são as descendentes. Para obter todo o texto do exemplo, utiliza-se `*::text` no seletor.

##### As seguintes verificações serão feitas:

- Por padrão deve-se raspar apenas as notícias da primeira página;

- Um número de páginas para serem raspadas pode ser passado para a função. Caso o número de páginas seja definido, deve-se raspar os dados das N primeiras páginas;

- A função deve retornar uma lista com cada notícia em no seguinte formato.

```json
[{
    "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm",
    "title": "Musk: Tesla está muito perto de carros totalmente autônomos",
    "timestamp": "2020-07-09T11:00:00",
    "writer": "Nilton Kleina",
    "shares_count": 61,
    "comments_count": 26,
    "summary": "O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado.",
    "sources": ["Venture Beat"],
    "categories": [
      "Mobilidade Urbana/Smart Cities",
      "Veículos autônomos",
      "Tesla",
      "Elon Musk"
    ]
  }]
```

📌 Muita atenção aos tipos dos campos, por exemplo, `sources` e `categories` são listas, assim como `shares_count` e `comments_count` são numéricos.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/collector/scrapper.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `scrape(fetcher=fetch_content, pages=2)`.

#### 3 - Deve haver uma função `insert_or_update` dentro do módulo `tech_news/database.py` que deve receber uma notícia e a insira na coleção, mas se a mesma já existir deve apenas atualizá-la.

##### As seguintes verificações serão feitas:

- Insira uma notícia no banco;

- Caso a notícia já exista no banco de dados, ela deve ser atualizada;

- Deve retornar `True` caso a notícia seja inserida senão `False`.

📌 Não esqueça de ter o banco de dados configurado e rodando.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/database.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `insert_or_update({"url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm", ...})`.


#### 4 - Deve haver uma função `csv_importer` dentro do módulo `tech_news/collector/importer.py` capaz de importar notícias a partir de um arquivo CSV, utilizando ";" como separador.

##### As seguintes verificações serão feitas:

- Caso a extensão do arquivo seja diferente de `.csv`, uma exceção deve ser lançada;

- Caso o arquivo CSV não exista, uma exceção deve ser lançada;

Obs: Caso o arquivo não exista e tenha extensão inválida, a exceção lançada dever ser a de formato inválido.

- O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`. Caso contrário, uma exceção deve ser lançada;

- A função deve retornar uma lista com cada notícia em no seguinte formato.

```json
[{
    "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm",
    "title": "Musk: Tesla está muito perto de carros totalmente autônomos",
    "timestamp": "2020-07-09T11:00:00",
    "writer": "Nilton Kleina",
    "shares_count": 61,
    "comments_count": 27,
    "summary": "Recentemente, a Alemanha fez a Tesla “pisar no freio” quanto ao uso de termos comerciais relacionados a carros autônomos, mas quem pensa que esse é um sinal de resistência à introdução de novas tecnologias se engana. Isso porque, de acordo o Automotive News Europe, o país está se preparando para se tornar o primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos de nível 4.",
    "sources": ["Venture Beat"],
    "categories": [
      "Mobilidade Urbana/Smart Cities",
      "Veículos autônomos",
      "Tesla",
      "Elon Musk"
    ]
  }]
```

📌Um exemplo de arquivo `CSV` pode ser encontrado na seção de [dados](#dados).

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/collector/importer.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `csv_importer("testdata.csv")`.

#### 5 - Deve haver uma função `csv_exporter` dentro do módulo `tech_news/collector/exporter.py` capaz de exportar todas as notícias do banco de dados para um arquivo CSV, utilizando ";" como separador.

##### As seguintes verificações serão feitas:

- O arquivo exportado deve possuir o formato CSV. Caso contrário, uma exceção deve ser lançada;

- Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

- O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`;

- Todas as notícias salvas no banco de dados devem ser exportadas.

📌 Um exemplo de arquivo `CSV` pode ser encontrado na seção de [dados](#dados).

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/collector/exporter.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `csv_exporter("output.csv")`.

### Pacote `tech_news/analyzer`

#### 6 - Deve haver uma função `search_by_title` dentro do módulo `tech_news/analyzer/search_engine.py`, que busque as notícias do banco de dados por título (parcial ou completo) e retorne uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de lista de tuplas `[("title", "url")]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_title("Musk")`.

#### 7 - Deve haver uma função `search_by_date` dentro do módulo `tech_news/analyzer/search_engine.py`, que busque as notícias do banco de dados por data e retorne uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve retornar uma lista de tuplas `[("title", "url")]`;

- A data deve estar no formato "aaaa-mm-dd" e deve ser válida. Caso seja inválida, uma exceção deve ser lançada.

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_date("2020-11-11")`.

#### 8 - Deve haver uma função `search_by_source` dentro do módulo `tech_news/analyzer/search_engine.py`, que busque as notícias do banco de dados por fonte (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de tuplas `[("title", "url")]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_source("Venture Beat")`.

#### 9 - Deve haver uma função `search_by_category` dentro do módulo `tech_news/analyzer/search_engine.py`, que busque as notícias do banco de dados por categoria (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de tuplas `[("title", "url")]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_category("Tesla")`.


#### 10 - Deve haver uma função `top_5_news` dentro do módulo `tech_news/analyzer/ratings.py`, que liste as cinco notícias com a maior soma de compartilhamentos e comentários do banco de dados. As notícias devem ser ordenadas pela popularidade. Em caso de empate, o desempate deve ser por ordem alfabética de título.

##### As seguintes verificações serão feitas:

- As top 5 notícias da análise devem ser retornadas em uma lista de tuplas `[("title", "url")]`;

- Caso haja menos de cinco notícias, no banco de dados, deve-se retornar todas as notícias existentes;

- Caso não haja notícias disponíveis, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/ratings.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `top_5_news()`.


#### 11 - Deve haver uma função `top_5_categories` dentro do módulo `tech_news/analyzer/ratings.py`, que liste as cinco categorias com maior ocorrência no banco de dados. As categorias devem ser ordenadas por ordem alfabética.

##### As seguintes verificações serão feitas:

- As top 5 categorias da análise devem ser retornadas em uma lista no formato `["category"]`;

- Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;

- Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

📌 Para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`, ou crie uma função no arquivo `database.py` e a utilize aqui. Lembre-se que a coleção se chama `news`.

✍️  Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/ratings.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `top_5_categories()`.

---

## Requisitos bônus:

### Pacote `tech_news`

#### 12 - Preencha a função `collector_menu`  que se encontra no módulo `tech_news/menu.py` como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação. O texto exibido pelo menu deve ser exatamente:

```md
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo CSV a ser importado:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo CSV a ser exportado:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a quantidade de páginas a serem raspadas:";

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

📌 A função `input` deve ser utilizada para receber a entrada de dados da pessoa usuária.

✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-collector`, o menu deve ser exibido. Isto acontece pois durante a configuração inicial do projeto já configuramos para que a função seja corretamente chamada quando este comando seja invocado.


#### 13 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada.

##### As seguintes verificações serão feitas:

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando a função `csv_importer`;

- Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando a função `csv_exporter`;

- Caso a opção `3` seja selecionada, a raspagem deve ser feita utilizando a função `scrape`;

- Caso a opção `4` seja selecionada, deve-se encerrar a execução do script;

- Caso alguma exceção seja lançada, a mesma deve ser capturada e sua mensagem deve ser exibida na saída padrão de erros (`stderr`).

✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-collector`, assim você conseguirá interagir com o menu.

#### 14 - Preencha a função `analyzer_menu`  que se encontra no módulo `tech_news/menu.py` como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação. O texto exibido pelo menu deve ser exatamente:

```md
Selecione uma das opções a seguir:

1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por fonte;
4 - Buscar notícias por categoria;
5 - Listar top 5 notícias;
6 - Listar top 5 categorias;
7 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o título:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a data no formato aaaa-mm-dd:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a fonte:";

- Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite a categoria:";

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

📌 A função `input` deve ser utilizada para receber a entrada de dados da pessoa usuária.

✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-analyzer`, o menu deve ser exibido. Isto acontece pois durante a configuração inicial do projeto já configuramos para que a função seja corretamente chamada quando este comando seja invocado.

#### 15 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada e seu resultado deve ser exibido.

##### As seguintes verificações serão feitas:

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando a função `search_by_title` e seu resultado deve ser impresso em tela;

- Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando a função `search_by_date` e seu resultado deve ser impresso em tela;

- Caso a opção `3` seja selecionada, a importação deve ser feita utilizando a função `search_by_source` e seu resultado deve ser impresso em tela;

- Caso a opção `4` seja selecionada, a exportação deve ser feita utilizando a função `search_by_category` e seu resultado deve ser impresso em tela;

- Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_news` e seu resultado deve ser impresso em tela;

- Caso a opção `6` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_categories` e seu resultado deve ser impresso em tela;

- Caso a opção `7` seja selecionada, deve-se encerrar a execução do script;

- Caso alguma exceção seja lançada, a mesma deve ser capturada e sua mensagem deve ser exibida na saída padrão de erros (`stderr`).


✍️  Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-analyzer`, assim você conseguirá interagir com o menu.

---

### DURANTE O DESENVOLVIMENTO

- Faça `commits` das alterações que você fizer no código regularmente

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

- Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

---

### DEPOIS DE TERMINAR O DESENVOLVIMENTO (OPCIONAL)

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ dos seus colegas, faça o seguinte:

- Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

  - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`.

Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

---

### REVISANDO UM PULL REQUEST

Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

#VQV 🚀