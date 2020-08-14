# Boas vindas ao repositório do projeto de Tech News!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

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

- `python3 -m pip install -r requirements.txt`

4. Crie uma branch a partir da branch `master`

- Verifique que você está na branch `master`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `master`
  - Exemplo: `git checkout master`
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

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-tech-news/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-tech-news/pulls) e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos `news_importer.py`, `news_exporter.py`, `news_scrapper.py`, `news_search_engine.py`, `news_analyser.py`, `test_news_importer.py`, `test_news_exporter.py`, `test_news_scrapper.py`, `test_news_search_engine.py`, `test_news_analyser.py`, que conterão seu código `Python` e seus testes, respectivamente.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

Para fixar o conteúdo sobre Python visto até agora, você fará um projeto que tem como principal objetivo criar um banco de dados de notícias sobre tecnologia e realizar algumas consultas nas notícias registradas.

Essas notícias podem ser obtidas de diferentes formas. Sendo elas:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- E através da raspagem das [últimas notícias do TecMundo](https://www.tecmundo.com.br/novidades).

Além de importar ou raspar as notícias, também deve ser possível exportá-las e realizar buscas ou análises nas notícias coletadas. **Ou seja: desenvolva um sistema capaz de importar _e_ exportar notícias via JSON e CSV; e que faça raspagem e preenchimento de um banco de dados com notícias.**

Legal, não é?

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── README.md
├── requirements.txt
├── setup.cfg
├── tech_news_app
│   ├── news_analyser.py
│   └── news_search_engine.py
├── tech_news_data_collector
│   ├── news_exporter.py
│   ├── news_importer.py
│   └── news_scrapper.py
├── tests
│   ├── test_news_analyser.py
│   ├── test_news_exporter.py
│   ├── test_news_importer.py
│   ├── test_news_scrapper.py
│   └── test_news_search_engine.py
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as funções quanto os testes. Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

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

### Importação e exportação de JSON

Os arquivos JSON devem seguir o seguinte modelo:

```json
[
  {
    "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155348-alemanha-trabalha-regulamentacao-carros-autonomos.htm",
    "title": "Alemanha já trabalha na regulamentação de carros autônomos",
    "timestamp": "2020-07-20T15:30:00",
    "writer": "Reinaldo Zaruvni",
    "shares_count": 0,
    "comments_count": 0,
    "summary": "Recentemente, a Alemanha fez a Tesla “pisar no freio” quanto ao uso de termos comerciais relacionados a carros autônomos, mas quem pensa que esse é um sinal de resistência à introdução de novas tecnologias se engana. Isso porque, de acordo o Automotive News Europe, o país está se preparando para se tornar o primeiro do mundo a criar uma ampla estrutura para regulamentar tais veículos de nível 4.",
    "sources": ["The Next Web", "The Next Web", "Automotive News Europe"],
    "categories": [
      "Mobilidade Urbana/Smart Cities",
      "Veículos autônomos",
      "Carro",
      "Política"
    ]
  }
]
```

### Raspagem de notícias

As notícias a serem raspadas estarão disponíveis na aba de últimas notícias do TecMundo: https://www.tecmundo.com.br/novidades.

Essas notícias devem ser salvas no banco de dados, utilizando os mesmos atributos já descritos nas importações/exportações citadas anteriormente.

### MongoDB

Para a realização desse projeto, **sugere-se** que você crie um banco de dados, chamado `tech_news`, para a aplicação e um banco de dados separado, chamado `tech_news_test`, para o ambiente de testes. Dessa forma, ambos os ambientes estarão isolados, o que garante que os testes não poluirão sua base de dados.

Para garantir que os dados gerados para um teste não influencie em outro teste, você deve popular e deletar as coleções ao início e ao fim de cada teste, respectivamente.

_Dica:_ Utilize a função `drop` do mongo no final do teste.

---

## Requisitos obrigatórios:

### Pacote `tech_news_data_collector`

#### 1 - Deve haver uma função `scrape` dentro do módulo `news_scrapper` capaz de raspar as últimas notícias das N primeiras páginas, armazenando suas informações no banco de dados.

> Observação: Utilizar os seguintes atributos: `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`. Notícias que já existirem no banco de dados devem ser atualizadas (verifique pela URL).

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

- O scrapper deve ser capaz de tratar um erro de `status 404` ao acessar uma notícia. Devemos considerar que é possível que haja alguma notícia com link quebrado;

- Todas as notícias devem conter obrigatóriamente os atributos `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`;

- Caso a notícia já exista no banco de dados, ela deve ser atualizada;

- Ao finalizar o scrapping, deve-se exibir a mensagem "Raspagem de notícias finalizada".

#### 2 - Deve haver uma função `csv_importer` dentro do módulo `news_importer` capaz de importar notícias a partir de um arquivo CSV, utilizando ";" como separador. Todas as mensagens de erro devem ir para a `stderr`.

##### As seguintes verificações serão feitas:

- Caso o arquivo CSV não exista, deve ser exibida a mensagem "Arquivo {path/to/file.csv} não encontrado";

- Caso a extensão do arquivo seja diferente de `.csv`, deve ser exibida uma mensagem "Formato inválido";

- O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`. Caso contrário, deve ser exibida uma mensagem "Cabeçalho inválido";

- Todos as informações devem ser obrigatórias. Caso haja alguma informação faltando, deve ser exibida uma mensagem "Erro na notícia {numero-da-linha}";

- Como não sabemos se a notícia importada está na versão mais atual, não deve ser possível adicionar notícias com URLs duplicadas. Em caso de erro, exiba a mensagem "Notícia {numero-da-linha} duplicada";

- Em caso de erros, a importação deve ser interrompida e nenhuma notícia deve ser salva;

- Em caso de sucesso, todas as notícias devem ser salvas no banco de dados e a mensagem "Importação realizada com sucesso" deve ser exibida na `stdout`.

#### 3 - Deve haver uma função `csv_exporter` dentro do módulo `news_exporter` capaz de exportar todas as notícias do banco de dados para um arquivo CSV, utilizando ";" como separador.

##### As seguintes verificações serão feitas:

- O arquivo exportado deve possuir o formato CSV. Caso contrário, deve ser exibida uma mensagem de erro "Formato inválido" na `stderr`;

- O arquivo deve ser criado na raiz do projeto;

- Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

- O arquivo CSV deve possuir um cabeçalho contendo `url`, `title`, `timestamp`, `writer`, `shares_count`, `comments_count`, `summary`, `sources` e `categories`;

- Todas as notícias salvas no banco de dados devem ser exportadas. Em caso de sucesso na exportação, a mensagem "Exportação realizada com sucesso" deve ser exibida na `stdout`.

#### 4 - Deve haver uma função `json_importer` dentro do módulo `news_importer` capaz de importar notícias a partir de um arquivo JSON. Todas as mensagens de erro devem ir para a `stderr`.

> Observação: considere o número da notícia como índice da lista + 1.

##### As seguintes verificações serão feitas:

- Caso o arquivo não exista, deve ser exibida a mensagem "Arquivo {path/to/file.json} não encontrado";

- Caso a extensão do arquivo seja diferente de `.json`, deve ser exibida a mensagem "Formato inválido";

- Caso o JSON seja inválido por qualquer erro no arquivo, deve ser exibida a mensagem "JSON inválido";

- Todas as informações devem ser obrigatórias. Caso haja alguma informação faltando, deve ser exibida a mensagem "Erro na notícia {numero-da-notícia}";

- Não deve ser possível adicionar notícias com URLs duplicadas, exibindo a mensagem "Notícia {numero-da-notícia} duplicada" em caso de erro;

- Em caso de erros, a importação deve ser interrompida e nenhuma notícia deve ser salva;

- Em caso de sucesso, todas as notícias devem ser salvas no banco de dados e a mensagem "Importação realizada com sucesso" deve ser exibida na `stdout`.

#### 5 - Deve haver uma função `json_exporter` dentro do módulo `news_exporter` capaz de exportar todas as notícias do banco de dados para um arquivo JSON.

##### As seguintes verificações serão feitas:

- O arquivo exportado deve possuir o formato `.json`. Caso contrário, deve ser exibida a mensagem de erro "Formato inválido" na `stderr`;

- O arquivo deve ser criado na raiz do projeto;

- Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

- Todas as notícias salvas no banco de dados devem ser exportadas e a mensagem "Exportação realizada com sucesso" deve ser exibida na `stdout`.

### Pacote `tech_news_app`

#### 6 - Deve haver uma função `search_by_title` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por título (parcial ou completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 7 - Deve haver uma função `search_by_date` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por data e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

- A data deve estar no formato "aaaa-mm-dd" e deve ser válida. Caso seja inválida, deve-se exibir a mensagem "Data inválida";

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 8 - Deve haver uma função `search_by_source` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por fonte (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 9 - Deve haver uma função `search_by_category` dentro do módulo `news_search_engine`, que busque as notícias do banco de dados por categoria (apenas uma por vez e com nome completo) e exiba uma lista de notícias encontradas. Para cada notícia encontrada, deve-se listar seu título e link.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista de notícias no formato `["- {title}: {url}"]`;

- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

#### 10 - Deve haver uma função `top_5_news` dentro do módulo `news_analyser`, que liste as cinco notícias com a maior soma de compartilhamentos e comentários do banco de dados. As notícias devem ser ordenadas pela popularidade. Em caso de empate, o desempate deve ser por ordem alfabética de título.

##### As seguintes verificações serão feitas:

- As top 5 notícias da análise devem ser retornadas em uma lista de notícias no formato `["- {title}: {url}"]`;

- Caso haja menos de cinco notícias, no banco de dados, deve-se retornar todas as notícias existentes;

- Caso não haja notícias disponíveis, deve-se retornar uma lista vazia.

#### 11 - Deve haver uma função `top_5_categories` dentro do módulo `news_analyser`, que liste as cinco categorias com maior ocorrência no banco de dados. As categorias devem ser ordenadas por ordem alfabética.

##### As seguintes verificações serão feitas:

- As top 5 categorias da análise devem ser retornadas em uma lista de categorias no formato `["- {category}"]`;

- Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;

- Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

---

## Requisitos bônus:

### Pacote `tech_news_data_collector`

#### 12 - A cobertura de testes unitários do pacote deve ser de no mínimo 90%.

##### As seguintes verificações serão feitas:

- Todos os testes que envolvem mensagens na saída padrão ou de erro, devem ter sua saída redirecionada para _Fakes_ com `StringIO`;

- Todos os testes que envolvem manipulação de arquivos criam _Fakes_ com `StringIO`;

- Todas as requisições externas utilizam _Mocks_;

- A cobertura de testes é de no mínimo 90%.

#### 13 - Crie um módulo `news_data_collector_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação. O texto exibido pelo menu deve ser exatamente:

**Dica**: Utilize o `__main__`.

```md
Selecione uma das opções a seguir:

1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Importar notícias a partir de um arquivo JSON;
4 - Exportar notícias para JSON;
5 - Raspar notícias online;
6 - Sair.
```

##### As seguintes verificações serão feitas:

- A mensagem de menu deve ser exibida corretamente;

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o path do arquivo CSV a ser importado:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo CSV a ser exportado:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite o path do arquivo JSON a ser importado:";

- Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite o nome do arquivo JSON a ser exportado:";

- Caso a opção `5` seja selecionada, deve-se exibir a mensagem "Digite a quantidade de páginas a serem raspadas:";

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

#### 14 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada.

##### As seguintes verificações serão feitas:

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando função `csv_importer`;

- Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando função `csv_exporter`;

- Caso a opção `3` seja selecionada, a importação deve ser feita utilizando função `json_importer`;

- Caso a opção `4` seja selecionada, exportação deve ser feita utilizando função `json_exporter`;

- Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando função `scrape`;

- Caso a opção `6` seja selecionada, deve-se encerrar a execução do script (dica: verifique o `exit code`);

- Após finalizar a execução de uma ação, deve-se encerrar a execução do script (dica: verifique o `exit code`).

### Pacote `tech_news_app`

#### 15 - A cobertura de testes unitários do pacote deve ser de no mínimo 90%.

#### 16 - Crie um módulo `news_app_menu` que deve ser utilizado como um menu de opções, em que cada opção pede as informações necessárias disparar uma ação. O texto exibido pelo menu deve ser exatamente:

**Dica**: Utilize o `__main__`.

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

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a data:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a fonte:";

- Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite a categoria:";

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

#### 17 - Ao selecionar uma opção do menu de opções e inserir as informações necessárias, a ação adequada deve ser disparada e seu resultado deve ser exibido.

##### As seguintes verificações serão feitas:

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando a função `search_by_title` e seu resultado deve ser impresso em tela;

- Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando a função `search_by_date` e seu resultado deve ser impresso em tela;

- Caso a opção `3` seja selecionada, a importação deve ser feita utilizando a função `search_by_source` e seu resultado deve ser impresso em tela;

- Caso a opção `4` seja selecionada, a exportação deve ser feita utilizando a função `search_by_category` e seu resultado deve ser impresso em tela;

- Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_news` e seu resultado deve ser impresso em tela;

- Caso a opção `6` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_categories` e seu resultado deve ser impresso em tela;

- Caso a opção `7` seja selecionada, deve-se encerrar a execução do script.

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
