# Dogs Django REST API

<p align="center">
  <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
  <img alt="DjangoREST" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
  <img alt="JWT" src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens">
  <img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white">
</p>

Uma API REST desenvolvida em Django que fornece serviços backend para uma plataforma de compartilhamento de fotos de cachorros. O projeto permite autenticação de usuários, upload de fotos e interação através de comentários.

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Como Executar](#-como-executar)
- [Endpoints da API](#-endpoints-da-api)

## 🎯 Sobre o Projeto

### Principais Desafios

- Implementação de autenticação JWT com tokens de acesso e refresh
- Gerenciamento eficiente de upload e armazenamento de arquivos de mídia
- Sistema de paginação customizado para otimizar performance
- Controle de permissões baseado em usuário para operações CRUD
- Configuração de CORS para integração com frontend

### Aprendizados

- Arquitetura de APIs RESTful com Django REST Framework
- Implementação de autenticação stateless com JWT
- Manipulação de arquivos de mídia em Django
- Serializers e ViewSets para criar endpoints eficientes
- Configuração de permissões e controle de acesso

## ⚡ Funcionalidades

### 1. Autenticação de Usuários

- Autenticação baseada em tokens JWT
- Token de acesso com validade de 1 dia
- Token de refresh com validade de 7 dias
- Endpoints de login e renovação de token
- Sistema seguro e stateless

### 2. Gerenciamento de Fotos

- Upload de fotos com armazenamento em sistema de arquivos
- Paginação customizada (15 itens por página)
- Controle de acesso baseado em permissões
- Listagem e detalhamento de fotos
- Metadados de fotos (autor, data, descrição)

### 3. Sistema de Comentários

- Adição de comentários em fotos
- Recursos de gerenciamento de comentários
- Associação de comentários com usuários e fotos
- API RESTful completa para operações CRUD

## 🏗 Arquitetura

### Estrutura de Apps Django

O projeto está estruturado em apps modulares seguindo o padrão MVT (Model-View-Template) do Django:

**authentication**

App responsável pelo gerenciamento de autenticação de usuários utilizando JWT (JSON Web Tokens). Implementa endpoints de login, logout e refresh de tokens, garantindo segurança através de tokens de curta duração para acesso e tokens de longa duração para renovação.

**photo**

Gerencia todas as operações relacionadas a fotos, incluindo upload, listagem, detalhamento e exclusão. Utiliza o sistema de arquivos de mídia do Django para armazenar imagens de forma eficiente e implementa paginação customizada para otimizar o carregamento de grandes volumes de dados.

**comment**

Implementa a funcionalidade completa de comentários, permitindo que usuários interajam com as fotos publicadas. Utiliza relacionamentos ForeignKey com os models de Photo e User para manter integridade referencial.

### Componentes Técnicos

**Django REST Framework**

Framework escolhido por sua robustez na criação de APIs RESTful. Oferece serializers para validação de dados, ViewSets para lógica de negócio organizada e sistema de roteamento automático de URLs.

**JWT Authentication**

Implementado através do `djangorestframework-simplejwt`, fornece autenticação stateless ideal para aplicações modernas. Tokens são armazenados no cliente e validados a cada requisição, eliminando necessidade de sessões no servidor.

**CORS Configuration**

Configuração de Cross-Origin Resource Sharing através do `django-cors-headers`, permitindo que o frontend React consuma a API de domínios diferentes durante desenvolvimento e produção.

**Media Storage**

Sistema de arquivos configurado para gerenciar upload e armazenamento de imagens. Utiliza a biblioteca Pillow para processamento de imagens e validação de formatos.

## 🛠 Tecnologias

**Django 5.2.4**

Framework web Python de alto nível que promove desenvolvimento rápido e design limpo. Escolhido por sua arquitetura MVT robusta, ORM poderoso e grande ecossistema de pacotes.

**Django REST Framework 3.16.0**

Toolkit poderoso e flexível para construir APIs Web. Oferece serialização de dados, autenticação, paginação e um sistema de permissões completo out-of-the-box.

**Simple JWT**

Biblioteca para implementar autenticação JWT no Django REST Framework. Fornece tokens de acesso e refresh, com configurações flexíveis de tempo de expiração.

**django-cors-headers**

Middleware Django para manipular cabeçalhos CORS (Cross-Origin Resource Sharing), essencial para permitir que aplicações frontend consumam a API.

**Pillow**

Biblioteca Python para processamento de imagens, utilizada para validar e manipular arquivos de imagem durante o upload.

**SQLite**

Banco de dados relacional leve e embutido, ideal para desenvolvimento e projetos de pequeno a médio porte. Não requer configuração de servidor separado.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)
- Git

### Instalação

1. Clone o repositório

```bash
git clone <url-do-repositório>
cd dogs-django-api
```

2. Crie e ative um ambiente virtual

```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

5. (Opcional) Crie um superusuário para acessar o admin

```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

7. Acesse a API em `http://localhost:8000/api/v1/`

## 📡 Endpoints da API

### Autenticação

- `POST /api/v1/auth/login/` - Login de usuário
- `POST /api/v1/auth/refresh/` - Renovar token de acesso
- `POST /api/v1/auth/register/` - Registrar novo usuário

### Fotos

- `GET /api/v1/photos/` - Listar fotos (paginado)
- `POST /api/v1/photos/` - Upload de nova foto
- `GET /api/v1/photos/{id}/` - Detalhes de uma foto
- `PUT /api/v1/photos/{id}/` - Atualizar foto
- `DELETE /api/v1/photos/{id}/` - Deletar foto

### Comentários

- `GET /api/v1/comments/` - Listar comentários
- `POST /api/v1/comments/` - Criar novo comentário
- `GET /api/v1/comments/{id}/` - Detalhes de um comentário
- `PUT /api/v1/comments/{id}/` - Atualizar comentário
- `DELETE /api/v1/comments/{id}/` - Deletar comentário

### Admin

- `GET /api/v1/admin/` - Interface administrativa do Django

## 🔧 Detalhes Técnicos

---
