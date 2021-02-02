# My Base Application 4 ROP-e

Um boilerplate implementado para sustentar uma aplicação django (websites, webapps, APIs) de fácil instalação e manutenção.
Base customizada para a Platafor ROP-e (Relatorio de Ocorrencias Policiais Eletrônica) 

##  Esta infraestrutura suporta:

> ## Banco de dados: 
   - SQLite
   - PostgreSQL

Para escolher o SGBD apenas necessário editar a variável de ambiente, $DATABASE e atribuir um destes valores [SQLITE | MYSQL | POSTGRESQL]: 
>Por exemplo: $DATABASE=POSTGRESQL

> ## Banco de dados com replicação

Esta infraestrutura possui duas instâncias de banco de dados, uma chamada de "master" e uma "slave". De forma que a instância slave é uma cópia em tempo real da instância master.

> ## Interface de gerenciamento do banco de dados

   1. PgAdmin

> ## HTTPs
> ## Proxy reverso com Nginx
> ## Base para uma aplicação gjango /src

# Esta implementação usa:

## Motor base: 

   1. Docker
   2. Docker Compose

## Umsamos como inspiração:
### Boilerplate - ddp (Docker - Django - Postgres)

   - Basic requirements (docker and docker-compose)

To install use:

> git clone --recurse-submodules git@github.com:cflb/boilerplate-ddp.git

Enter the directory you just cloned

> cd boilerplate-ddp/

Build containers:

> docker-compose build

Up containers:

> docker-compose up

Open browser:

> localhost

### Django Project Boileplate

1. Rename your project with:
   > python manage.py rename yourprojectname newprojectname

#### This project includes:

1. Settings modules for deploying with Azure
2. Django commands for renaming your project and creating a superuser
3. A cli tool for setting environment variables for deployment
