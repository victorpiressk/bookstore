# 📚 Bookstore API

![Build Status](https://github.com/victorpiressk/bookstore-api/workflows/Python%20application/badge.svg)
![Code Quality](https://img.shields.io/badge/code%20style-black-000000.svg)
![Tests](https://img.shields.io/badge/tests-15%20passing-success)
![Python](https://img.shields.io/badge/python-3.14.0-blue)
![Django](https://img.shields.io/badge/django-5.2-green)

API REST desenvolvida com Django e Django REST Framework para gerenciamento de uma livraria, com suporte a produtos, categorias e pedidos, autenticação por token e versionamento de rotas.

---

## 🚀 Tecnologias

- **Python 3.14.0**
- **Django 5.2**
- **Django REST Framework 3.16.1**
- **Poetry 2.1.4** (gerenciamento de dependências)
- **PostgreSQL 14** (desenvolvimento e produção)
- **Token Authentication** (DRF)
- **Pytest / Pytest-Django** (15 testes automatizados)
- **Factory Boy** (factories para testes)
- **Docker & Docker Compose** (desenvolvimento local)
- **Whitenoise** (arquivos estáticos)
- **Gunicorn** (servidor WSGI em produção)
- **Black** (qualidade de código)
- **GitHub Actions** (CI/CD)
- **Render** (deploy em produção)
- **Supabase** (banco de dados em produção)

---

## 📋 Funcionalidades

- ✅ CRUD completo de produtos e categorias
- ✅ Criação e listagem de pedidos com cálculo automático de total
- ✅ Autenticação por Token, Session e Basic Authentication
- ✅ Versionamento de rotas (v1/v2) preparado para evolução futura
- ✅ Paginação automática (10 itens por página)
- ✅ Permissões por recurso — pedidos exigem autenticação
- ✅ Testes automatizados com factories e APITestCase

---

## 📂 Estrutura do Projeto

```
bookstore-api/
├── .github/workflows/         # CI/CD com GitHub Actions
├── bookstore/                 # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── order/                     # App de pedidos
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── factories.py
│   ├── urls.py
│   └── tests/
├── product/                   # App de produtos e categorias
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── factories.py
│   ├── urls.py
│   └── tests/
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── pyproject.toml
└── manage.py
```

---

## 🔧 Instalação Local (sem Docker)

### Pré-requisitos

- Python 3.14.0
- Poetry 2.1.4+
- PostgreSQL 14+

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/victorpiressk/bookstore.git
cd bookstore

# 2. Instale o Poetry (se não tiver)
pip install poetry==2.1.4

# 3. Instale as dependências
poetry install

# 4. Ative o ambiente virtual
poetry shell

# 5. Configure as variáveis de ambiente
# Crie um arquivo .env com base nas variáveis descritas na seção abaixo

# 6. Execute as migrations
poetry run python manage.py migrate

# 7. (Opcional) Crie um superusuário
poetry run python manage.py createsuperuser

# 8. Inicie o servidor
poetry run python manage.py runserver
```

**A API estará disponível em:** `http://localhost:8000`

---

## 🐳 Desenvolvimento com Docker (Recomendado)

O projeto utiliza um arquivo `env.dev` para configurar as variáveis de ambiente no Docker. Ele já está incluído no repositório com as configurações necessárias para execução local. Sem ele, o Docker não consegue reconhecer as variáveis de ambiente da aplicação.

```bash
# 1. Build e iniciar os containers
docker-compose up -d --build

# 2. Executar migrations
docker-compose exec backend python manage.py migrate

# 3. (Opcional) Criar superusuário
docker-compose exec backend python manage.py createsuperuser
```

### Serviços disponíveis

| Serviço  | Endereço             |
|----------|----------------------|
| backend  | http://localhost:8000 |
| db       | localhost:5432        |

---

## 📡 Endpoints da API

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api-token-auth` | Obter token de autenticação |

### Produtos

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/bookstore/v1/product/` | Listar produtos | Não |
| POST | `/bookstore/v1/product/` | Criar produto | Não |
| GET | `/bookstore/v1/product/{id}/` | Detalhar produto | Não |
| PUT | `/bookstore/v1/product/{id}/` | Atualizar produto | Não |
| DELETE | `/bookstore/v1/product/{id}/` | Deletar produto | Não |

### Categorias

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/bookstore/v1/category/` | Listar categorias | Não |
| POST | `/bookstore/v1/category/` | Criar categoria | Não |
| GET | `/bookstore/v1/category/{id}/` | Detalhar categoria | Não |
| PUT | `/bookstore/v1/category/{id}/` | Atualizar categoria | Não |
| DELETE | `/bookstore/v1/category/{id}/` | Deletar categoria | Não |

### Pedidos

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/bookstore/v1/order/` | Listar pedidos | ✅ Token |
| POST | `/bookstore/v1/order/` | Criar pedido | ✅ Token |
| GET | `/bookstore/v1/order/{id}/` | Detalhar pedido | ✅ Token |
| PUT | `/bookstore/v1/order/{id}/` | Atualizar pedido | ✅ Token |
| DELETE | `/bookstore/v1/order/{id}/` | Deletar pedido | ✅ Token |

> Substitua `v1` por `v2` nas rotas — a estrutura de versionamento está preparada para evolução futura.

---

## ⚙️ Variáveis de Ambiente

O arquivo `env.dev` já está incluído no repositório com as configurações para execução local via Docker:

```env
DEBUG=True
SECRET_KEY=foo
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=bookstore_dev_db
SQL_USER=bookstore_dev
SQL_PASSWORD=bookstore_dev
SQL_HOST=db
SQL_PORT=5432
```

---

## 🚀 Deploy em Produção

Este projeto foi colocado em produção utilizando duas plataformas gratuitas: **Render** para hospedar a API e **Supabase** para o banco de dados.

### Por que Render?

O Render oferece hospedagem gratuita para aplicações web sem limite de tempo, sendo uma boa opção para projetos Django com Gunicorn. O plano gratuito inclui hospedagem da aplicação sem remoção automática, o que garante que a API permaneça disponível continuamente.

> **Atenção:** o plano gratuito do Render também oferece um banco de dados PostgreSQL, porém ele é removido automaticamente após 30 dias, causando perda total dos dados. Por esse motivo, o banco do Render não foi utilizado neste projeto.

### Por que Supabase?

O Supabase resolve o problema de persistência dos dados. No plano gratuito, ele disponibiliza até dois bancos PostgreSQL sem limite de tempo, mantendo os dados íntegros independentemente do período de inatividade. Neste projeto, o Supabase atua exclusivamente como banco de dados, enquanto o Render é responsável por hospedar e servir a aplicação.

### Configuração no Render

#### Build Command:
```bash
poetry install --no-root && python manage.py collectstatic --noinput && python manage.py migrate
```

#### Start Command:
```bash
poetry run gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT
```

Configure as variáveis de ambiente do Render com os dados de conexão fornecidos pelo Supabase.

---

## 🔐 Autenticação

Os endpoints de `order` exigem autenticação. Como a aplicação não possui endpoint de cadastro de usuários nem acesso ao terminal em produção, esse fluxo deve ser realizado exclusivamente no ambiente local.

### 1. Iniciar o ambiente

Siga todos os passos da seção Desenvolvimento com Docker, incluindo a criação do superusuário. Certifique-se de que os containers estão em execução antes de prosseguir.

### 2. Iniciar o servidor

> **Nota:** ao executar `docker-compose up`, o servidor já é iniciado automaticamente pelo comando padrão definido no container. Caso seja necessário iniciá-lo manualmente, utilize o comando abaixo:

```bash
docker-compose exec backend python manage.py runserver 0.0.0.0:8000
```

### 3. Instalar o Postman

Caso ainda não tenha o Postman instalado, faça o download em [postman.com/downloads](https://www.postman.com/downloads/) e siga as instruções de instalação para o seu sistema operacional.

### 4. Obter o token

- Abra o Postman e crie uma nova requisição
- Método: `POST`
- URL: `http://localhost:8000/api-token-auth`
- Aba **Body** → selecione **raw** e formato **JSON**
- Insira o body:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

- Envie a requisição — o token será retornado no corpo da resposta

### 5. Acessar endpoints de order

- Crie uma nova aba no Postman
- Método: `GET`
- URL: `http://localhost:8000/bookstore/v1/order/`
- Aba **Headers** → adicione:
  - Chave: `Authorization`
  - Valor: `Token SEU_TOKEN_AQUI`
- Aba **Authorization** → tipo **Basic Auth** → informe username e senha

Envie a requisição para listar as ordens de pedidos.

---

## 🧪 Testes

O projeto possui **15 testes automatizados** cobrindo models, serializers, views e factories.

### Executar testes localmente com Docker

```bash
# Primeira execução ou após mudanças nos models
docker-compose exec backend pytest --create-db -v

# Execuções subsequentes
docker-compose exec backend pytest -v
```

---

## 📄 CI/CD

### GitHub Actions

- **Build & Test:** instalação de dependências e execução dos testes
- **Pull Request Workflow:** qualidade de código com Wemake Python Styleguide

Executado em pushes e pull requests.

---

## 🧹 Qualidade de Código

```bash
poetry run black .
```

---

## 🗄️ Modelos de Dados

### Product
```python
- title (max 100 caracteres)
- description (max 500 caracteres, opcional)
- price (inteiro positivo)
- active (booleano, padrão True)
- category (ManyToMany → Category)
```

### Category
```python
- title (max 100 caracteres)
- slug (único)
- description (max 200 caracteres, opcional)
- active (booleano, padrão True)
```

### Order
```python
- product (ManyToMany → Product)
- user (ForeignKey → User)
- total (calculado via serializer)
```

---

## 🎓 Projeto Educacional & Portfólio

Desenvolvido como projeto de portfólio demonstrando: Django REST Framework, autenticação por token, versionamento de API, testes automatizados com factories, containerização com Docker e deploy em produção.

---

## 👨‍💻 Autor

**Victor Pires** — [@victorpiressk](https://github.com/victorpiressk) — [LinkedIn](https://www.linkedin.com/in/victor-p-rego/)

---

**Versão:** 1.0.0
**Status:** ✅ Em Produção