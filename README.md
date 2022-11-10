# Projeto - BHub API CRUD

Mini projeto desenvolvido na seleção de candidatos na BHub## Como executar

## Como executar

### 1. Utilizando Docker

Depois de instalar o [Docker](https://docs.docker.com/engine/install/ubuntu/), execute no terminal:

```
    docker compose up --build
```

E pronto! Tanto a API e o frontend estarão disponíveis em `localhost:8001` e `localhost:8000` respectivamente.

### 2. Sem utilizar Docker

#### API

Para executar a API você vai precisar do [Python 3.10](https://www.python.org/downloads/) e do [pip](https://pip.pypa.io/en/stable/installation/) instalado. Com isso pronto, para instalar os pacotes necessários, execute na raíz do projeto:

```
    pip install -r requirements.txt
```

Com os pacotes instalados, para executar a API execute, também na raíz do projeto:

```
    uvicorn app:app --reload
```

#### Front End

Já para executar o Front End será necessário instalar o [NodeJS (versão 18.12.1)](https://nodejs.org/en/download/). Para instalar os pacotes necessários, execute na raíz do projeto:

```
    npm install
```

Com os pacotes instalados, para executar o Front End execute, também na raíz do projeto:

```
    npm run dev
```
## Executando testes

Os testes são executados utilizando o pacote `pytest`. Dessa forma basta executar no seu terminal (após já ter instalado os pacotes como descrito na seção `Como executar`):

```bash
  pytest
```
