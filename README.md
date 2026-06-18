# 🚀 HelpDesk DevOps - Sistema de Gerenciamento de Chamados Técnicos

## 🐳 O que é Docker?

O Docker é uma plataforma de código aberto utilizada para desenvolver, distribuir e executar aplicações em ambientes isolados chamados **containers**. Esses containers empacotam a aplicação juntamente com todas as suas dependências, bibliotecas e configurações necessárias para execução, garantindo que o software funcione da mesma forma em diferentes ambientes.

Os containers são leves, portáveis e compartilham o sistema operacional do hospedeiro, consumindo menos recursos do que máquinas virtuais tradicionais. Além disso, proporcionam maior consistência entre ambientes de desenvolvimento, testes e produção.

### Principais Benefícios do Docker

- Portabilidade entre diferentes sistemas e ambientes;
- Isolamento de aplicações e dependências;
- Facilidade de implantação e distribuição;
- Maior consistência entre desenvolvimento e produção;
- Suporte a práticas modernas de DevOps e CI/CD;
- Melhor aproveitamento dos recursos de hardware.

**Para Saber Mais**:

Caso deseje conhecer mais sobre Docker, sua arquitetura e o funcionamento dos containers, consulte os materiais abaixo:

- Documentação oficial do Docker: https://docs.docker.com/get-started/docker-overview/
- Docker Desktop (ferramenta utilizada durante o desenvolvimento e execução do projeto): https://docs.docker.com/desktop/
- Slides da apresentação do projeto: https://canva.link/u7k3rx2enddjywt

---

## 📋 Sobre o Projeto

Este projeto acadêmico foi desenvolvido para demonstrar conceitos fundamentais de **DevOps** através da criação, versionamento e containerização de uma aplicação web funcional para gerenciamento de chamados técnicos. A aplicação serve como um exemplo prático de como ferramentas e práticas DevOps podem ser aplicadas em um pipeline de desenvolvimento real.

## 🎯 Objetivos da Demonstração

- Investigar os recursos e funcionalidades da stack escolhida (Flask + Docker)
- Configurar um ambiente de desenvolvimento containerizado
- Demonstrar o uso prático em um cenário real de helpdesk
- Compreender as vantagens, limitações e aplicabilidade em pipelines DevOps

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|------------|---------|------------|
| Python | 3.12 | Linguagem de programação |
| Flask | 2.3.x | Framework web |
| SQLAlchemy | 2.0.x | ORM para banco de dados |
| SQLite | 3.x | Banco de dados leve |
| Docker | 24.x | Containerização |
| Git | 2.x | Controle de versão |
| GitHub | - | Hospedagem de código |

## ✨ Funcionalidades Implementadas

### Interface Web
- Cadastro de novos chamados
- Listagem completa de chamados
- Atualização de status
- Exclusão de chamados
- Interface responsiva com CSS

### API REST
- Endpoints para operações CRUD
- Retorno em formato JSON
- Documentação básica dos endpoints

## 🏗️ Arquitetura da Aplicação

```text
Usuário
   ↓
Interface Web / API REST
   ↓
Flask Application
   ↓
SQLAlchemy ORM
   ↓
SQLite Database
   ↓
Docker Container
```

## 📁 Estrutura do Projeto

```text
helpdesk-devops/
├── app.py
├── models.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
├── static/
├── templates/
└── docs/
```

## 🔧 Configuração e Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Docker (opcional)
- Git
- Pip

### Instalação Local

```bash
git clone https://github.com/seu-usuario/helpdesk-devops.git
cd helpdesk-devops
pip install -r requirements.txt
python app.py
```

## 🐳 Execução com Docker

### Construção da Imagem

```bash
docker build -t helpdesk-devops:v1.0.0 .
docker images
```

### Execução do Container

```bash
docker run -d -p 5000:5000 --name helpdesk-api helpdesk-devops:v1.0.0
docker ps
docker logs helpdesk-api
```

### Comandos Úteis

```bash
docker stop helpdesk-api
docker rm helpdesk-api
docker exec -it helpdesk-api /bin/bash
```

## 📊 Conceitos DevOps Demonstrados

- Controle de Versão com Git
- Hospedagem de Código no GitHub
- Containerização com Docker
- Documentação Técnica
- Versionamento de Releases
- Configuração por Ambiente
- Estrutura preparada para CI/CD

### Containerização com Docker

A aplicação foi empacotada em um container Docker, permitindo que todo o ambiente de execução seja reproduzido em qualquer máquina que possua Docker instalado. Essa abordagem elimina problemas relacionados a diferenças de configuração entre ambientes de desenvolvimento, homologação e produção.

Fluxo utilizado:

```text
Código Fonte → Dockerfile → Imagem Docker → Container em Execução
```

## 🎓 Aprendizados e Conclusões

### Principais Vantagens Identificadas

- Portabilidade
- Reprodutibilidade
- Isolamento
- Escalabilidade

### Limitações Encontradas

- SQLite não é recomendado para produção
- Ausência de autenticação
- Monitoramento básico

### Recomendações para Produção

- PostgreSQL ou MySQL
- JWT ou OAuth
- Prometheus + Grafana
- Kubernetes ou Docker Swarm
- GitHub Actions ou Jenkins

## 📦 Versões e Releases

### v1.0.0
- Funcionalidades CRUD completas
- Containerização com Docker
- Documentação inicial

## 👥 Contribuidores

- Rebeca
- Ryllen
- Ricardo
- André 
- Estival
- Pedro
- Gustavo

## 📝 Licença

Projeto desenvolvido para fins educacionais.

## Versão

v1.0.0

