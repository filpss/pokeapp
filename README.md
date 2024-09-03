<p align="center">
  <img align="center" alt="Lipe-Node" height="50" width="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original.svg"/> &nbsp;
  <img align="center" alt="Lipe-Node" height="50" width="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"/> &nbsp;
  <img align="center" height="45" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg"/> &nbsp;
  <img align="center" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg"/> &nbsp;
  <br>
  <img align="center" alt="Lipe-Node" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg"/> &nbsp;
  <img align="center" alt="Lipe-Node" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/poetry/poetry-original.svg"/> &nbsp;
  <img align="center" alt="Lipe-Node" height="70" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg"/> &nbsp;
  <img align="center" alt="Lipe-Node" height="70" width="70" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg"/> &nbsp;
</p>

<p align="center">
  <a href="https://angular.dev/"><img src="https://img.shields.io/badge/Vue-3-42b883.svg?style=flat-square"/></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/Python-3.11-yellow.svg?style=flat-square"/></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/PostgreSQL-16-336791.svg?style=flat-square"/></a>
  <a href="https://sass-lang.com/"><img src="https://img.shields.io/badge/Docker-26-28B8EB.svg?style=flat-square"/></a>
  <img src="https://img.shields.io/badge/Aplicação Web-purple.svg?style=flat-square"alt="Platforms">
</p>

# PokeApp

Esta é uma aplicação web que permite visualizar uma galeria de pokemons usando uma interface frontend em Vue.js, um backend em FastAPI e armazenando os dados em um banco de dados PostgreSQL. 
A aplicação é toda containerizada usando Docker, o que facilitar a configuração e a execução.

## Tecnologias Utilizadas

- **Frontend:** Vue.js
- **Backend:** FastAPI
- **Banco de Dados:** PostgreSQL com SQLAlchemy
- **Cache:** Redis
- **Containerização:** Docker e Docker Compose
- **Autenticação:** JWT

## Pré-requisitos

Para testar a aplicação você precisa ter as seguintes ferramentas instaladas:

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instalação do Docker Compose](https://docs.docker.com/compose/install/)
- Git: [Instalação do Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Como Rodar a Aplicação

### 1. Clonar o Repositório

Clone este repositório na sua máquina local usando o comando:

``` bash
git clone https://github.com/filpss/pokeapp
```

### 2. Configurar o docker compose

O projeto já inclui um arquivo docker-compose.yml para facilitar a configuração, ou seja, ele vai criar os containers para o frontend, backend e o banco de dados.

### 3. Rodar a Aplicação

Para iniciar a aplicação, navegue até o diretório raiz do projeto e execute o comando:

```bash
docker-compose up -d --build
```

Isso fará com que:

    - Os containers sejam construídos e iniciados.
    - O backend se torne acessível em http://localhost:8000.
    - O frontend se torne acessível em http://localhost ou http://localhost:80.

### 4. Acessando a Aplicação

Abra o navegador e vá para http://localhost para acessar a interface do usuário.
Caso dejse ver a documentacão da API (Swagger UI) basta acessar http://localhost:8000/docs.

### 5. Parar a Aplicação

Ao finalizar, caso deseje parar a aplicação e remover os containers, execute:
```bash
docker-compose down
```
