# HelpDesk DevOps

Sistema acadêmico desenvolvido para demonstrar conceitos de DevOps através da criação, versionamento e containerização de uma aplicação web para gerenciamento de chamados técnicos.

## Tecnologias Utilizadas

* Python 3.12
* Flask
* SQLAlchemy
* SQLite
* Docker
* Git
* GitHub

## Funcionalidades

* Cadastro de chamados
* Listagem de chamados
* Atualização de status
* Exclusão de chamados
* Interface Web
* API REST

## Arquitetura

```text
Usuário
   ↓
Interface Web
   ↓
Flask
   ↓
SQLite
```

## Estrutura do Projeto

```text
helpdesk-devops/

├── app.py
├── models.py
├── requirements.txt
├── Dockerfile
├── README.md
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── docs/
```

## Executando Localmente

### Criar ambiente virtual

```powershell
python -m venv .venv
```

### Ativar ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências

```powershell
pip install -r requirements.txt
```

### Executar aplicação

```powershell
python app.py
```

Acesse:

```text
http://localhost:5000
```

## Executando com Docker

### Construir imagem

```powershell
docker build -t helpdesk-devops:v1 .
```

### Executar container

```powershell
docker run -d -p 5000:5000 --name helpdesk-api helpdesk-devops:v1
```

### Verificar container

```powershell
docker ps
```

## Conceitos DevOps Demonstrados

* Controle de versão com Git
* Hospedagem de código no GitHub
* Containerização com Docker
* Criação de imagens Docker
* Execução de aplicações em containers
* Documentação técnica
* Versionamento de entregas

## Versão

v1.0.0

