# 🚀 HelpDesk DevOps - Sistema de Gerenciamento de Chamados Técnicos

O sistema de chamados foi desenvolvido apenas como aplicação de apoio para demonstrar o uso de Git, GitHub e Docker em um cenário prático. O foco principal do projeto é o estudo de versionamento, containerização e publicação de aplicações.

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
| Flask | 3.1.3 | Framework web |
| SQLAlchemy | 2.0.x | ORM para banco de dados |
| SQLite | 3.x | Banco de dados leve |
 PostgreSQL | 16 | Banco de dados utilizado a partir da versão v1.1.0 |
| Docker | 24.x | Containerização |
| Docker Compose | 2.x | Orquestração dos containers |
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
## 📊 Logs e Outputs

### Exemplo conceitual de Logs da Aplicação

```text
[2026-06-18 10:30:45] INFO: Iniciando aplicação HelpDesk
[2026-06-18 10:30:45] INFO: Conectando ao banco de dados SQLite
[2026-06-18 10:30:46] INFO: Tabelas criadas com sucesso
[2026-06-18 10:30:50] INFO: Chamado #1 criado - "Problema no sistema"
[2026-06-18 10:31:15] INFO: Chamado #1 atualizado para status "Em andamento"
[2026-06-18 10:31:30] INFO: Chamado #1 encerrado com sucesso
```

### Exemplo de Output da API

```json
{
  "id": 1,
  "titulo": "Problema no sistema",
  "descricao": "Sistema apresentando lentidão",
  "status": "Aberto",
  "data_abertura": "2026-06-18T10:30:50"
}
```

### Resultado Esperado da Aplicação

Ao acessar a aplicação pelo navegador em:

http://localhost:5000

o usuário poderá:

- Criar novos chamados;
- Consultar chamados existentes;
- Alterar o status dos chamados;
- Excluir chamados;
- Visualizar informações atualizadas em tempo real.

---

## 🚧 Dificuldades Enfrentadas

Durante o desenvolvimento do projeto foram encontradas algumas dificuldades relacionadas à configuração do ambiente e à utilização das ferramentas DevOps.

### 1. Configuração do Docker

**Problema:** Primeiros testes apresentaram dificuldades na criação e execução da imagem Docker.

**Solução:** Revisão do Dockerfile e utilização da documentação oficial para ajustes na configuração.

### 2. Gerenciamento de Dependências

**Problema:** Algumas bibliotecas apresentaram incompatibilidades entre versões.

**Solução:** Definição de versões específicas no arquivo `requirements.txt`, garantindo maior estabilidade da aplicação.

### 3. Integração entre Flask e Banco de Dados

**Problema:** Erros iniciais na criação automática das tabelas e persistência dos dados.

**Solução:** Ajustes na configuração do SQLAlchemy e validação da conexão com o banco SQLite.

### 4. Aprendizado das Ferramentas DevOps

**Problema:** Adaptação aos conceitos de containerização, versionamento e boas práticas de documentação.

**Solução:** Estudo da documentação oficial do Docker, Git e GitHub, além de testes práticos durante o desenvolvimento.

### Lições Aprendidas

- Importância da documentação em projetos DevOps;
- Benefícios da containerização para portabilidade;
- Facilidade de replicação do ambiente utilizando Docker;
- Melhor organização do código através do Git e GitHub.

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

