# 🤖 Automação de Vagas no LinkedIn com Selenium e Power BI
### Este projeto tem como objetivo automatizar a coleta de vagas publicadas no LinkedIn, consolidar os dados e gerar insights interativos em um dashboard no Power BI.
### A automação utiliza Selenium para raspagem de dados, Excel para tratamento e modelagem, e Power BI para visualização.

## 🎯 Objetivo do Projeto

### O principal objetivo foi monitorar e analisar vagas de tecnologia no LinkedIn, permitindo uma visão geral sobre:

    As empresas que mais contratam;
    
    Distribuição das vagas por estado e tipo de cargo;
    
    Quantidade de oportunidades por nível de senioridade;
    
    Padrões geográficos e de frequência das publicações.

## 🎥 Visualização do Dashboard

<img width="100%" alt="Dashboard" src="https://github.com/GuilhermeSecco/JobScraper-BI-Dashboard/blob/main/Visualizao_Menor_Dashboard.gif?raw=true" />

## ⚙️ Tecnologias Utilizadas

### Python

    Selenium (automação da coleta de dados)
    Pandas (tratamento e consolidação das informações)

### Excel

    Junção e modelagem dos datasets gerados
    Tratamento de colunas e padronização de dados geográficos

### Power BI

    Criação de visualizações interativas
    Cálculo de métricas e indicadores

### Ferramentas auxiliares 
    GitHub 
    Firefox WebDriver 
    Trello

## 🧩 Estrutura do Projeto

    📦 Automacao-Vagas-Linkedin
     ┣ 📜 Vagas_LinkedIN.py                # Script de automação com Selenium
     ┣ 📜 Vagas em Python 30-10-2025.csv   # CSVs gerados automaticamente
     ┣ 📜 Vagas em Power BI 30-10-2025.csv
     ┣ 📜 Vagas em Selenium 30-10-2025.csv
     ┣ 📜 Vagas em Automação em Python 30-10-2025.csv
     ┣ 📜 Vagas em Análise de Dados 30-10-2025.csv
     ┣ 📜 Vagas.CSV                        # Dataset unificado e tratado no Excel
     ┣ 📊 Dashboard.pbix                   # Dashboard interativo no Power BI
     ┣ 📄 Dashboard.pdf                    # Versão em PDF do dashboard
     ┣ 🎞️ Visualização_Dashboard.gif       # Prévia animada da dashboard
     ┗ 📘 README.md                        # Documentação do projeto


## 🧠 Etapas do Desenvolvimento

### 1️⃣ Coleta de Dados – Selenium

O script Vagas_LinkedIN.py automatiza a busca no LinkedIn para diferentes termos, definidos na variável pesquisa.

Foram utilizadas cinco pesquisas distintas:

    Power BI
    
    Python
    
    Selenium
    
    Automação em Python
    
    Análise de Dados

Os resultados de cada busca são armazenados em CSVs individuais contendo:

    Nome da vaga
    
    Empresa
    
    Local
    
    Tempo desde a postagem
    
    Link da vaga

### 2️⃣ Tratamento e Modelagem – Excel

Os cinco CSVs foram unificados em um dataset único, onde:

    Foram padronizados nomes de estados e países;

    Criadas colunas auxiliares para região e país, garantindo a exibição correta no mapa do Power BI.

### 3️⃣ Visualização – Power BI

O dashboard final apresenta:

    Total de vagas publicadas;

    Distribuição por senioridade e empresa;

    Mapa interativo por estado e país;

    Indicadores de proporção entre vagas remotas e presenciais.


## 📊 Principais Insights

    São Paulo e Rio de Janeiro concentram a maioria das oportunidades presenciais.
    
    As vagas remotas representam cerca de 23% do total.
    
    Bradesco, Tata Consultancy e Shopee figuram entre as empresas com mais oportunidades.
    
    O nível Júnior e Estágio domina o mercado de entrada em dados e automação.

## 🚀 Possíveis Expansões

    Automatizar a unificação e limpeza via Python (eliminando a etapa manual no Excel).
    
    Criar um agendador para coleta semanal automática.
    
    Aplicar análise temporal com histórico de vagas.
    
    Desenvolver versão web interativa (Streamlit / Flask).
