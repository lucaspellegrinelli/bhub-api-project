# Projeto - BHub API CRUD

Mini projeto desenvolvido na seleção de candidatos na BHub

## Features

- [x] API CRUD
  - [x] Modelagem dos dados utilizando [Pydantic](https://pydantic-docs.helpmanual.io/)
  - [x] Criação da API utilizando [FastAPI](https://fastapi.tiangolo.com/)
  - [x] Conexão com banco de dados utilizando [SQLAlchemy](https://www.sqlalchemy.org/)
- [x] Documentação utilizando [Swagger](https://swagger.io/)
- [x] Testes
  - [x] Unitários utilizando [Pytest](https://pytest.org/) (testando a modelagem de dados)
  - [x] Funcionais utilizando [Pytest](https://pytest.org/) (testando as rotas da API e seus resultados)
  - [x] De API utilizando [Postman](https://www.postman.com/) (testando a API online)
  - [x] Mock do banco de dados durante os testes
- [x] Hosteamento da aplicação no AWS EC2 - [bhub.lucaspellegrinelli.com](https://bhub.lucaspellegrinelli.com/)
- [x] Utilização do [Docker](https://www.docker.com/) para distribuição
- [x] [Github Actions](https://github.com/features/actions)
  - [x] Linting utilizando o [flake8](https://flake8.pycqa.org/)
  - [x] Execução automática dos testes do Pytest e Postman
  - [x] Deploy automático para servidor AWS EC2
- [x] Hosteamento do banco de dados na núvem
  - [x] AWS Relational Database Service (RDS)
  - [x] Railway (melhor para a visualização das tarefas na explicação da arquitetura)

## Como executar

### 1. Utilizando Docker

Depois de instalar o [Docker](https://docs.docker.com/engine/install/ubuntu/), execute no terminal:

```
  docker compose up --build
```

E pronto! A API estará disponível em `localhost:8000`.

### 2. Sem utilizar Docker

Para executar a API você vai precisar do [Python 3.10](https://www.python.org/downloads/) e do [pip](https://pip.pypa.io/en/stable/installation/) instalado. Com isso pronto, para instalar os pacotes necessários, execute na raíz do projeto:

```
  pip install -r requirements.txt
```

Com os pacotes instalados, para executar a API execute, também na raíz do projeto:

```
  uvicorn app:app --reload
```

O servidor estará disponível em `localhost:8000`.

## Executando testes

Os testes são executados utilizando o pacote `pytest`. Dessa forma basta executar no seu terminal (após já ter instalado os pacotes como descrito na seção `Como executar`):

```bash
  python -m pytest
```
