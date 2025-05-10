# 📊 Projeto de Análise de Churn - Telco Customer Churn Dataset (IBM)

Este projeto tem como objetivo analisar e explorar dados de cancelamento de clientes (churn) no setor de telecomunicações, utilizando o dataset "Telco Customer Churn" disponibilizado pela IBM. O foco principal é a geração de insights visuais e análises descritivas que serão compartilhadas em forma de desafio no LinkedIn.

## 📂 Fonte do Dataset

* Dataset: [Telco Customer Churn - IBM](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* Tamanho: Aproximadamente 7.000 registros
* Domínio: Telecomunicações

## 📅 Estrutura do Dataset

O conjunto de dados contém informações demográficas dos clientes, detalhes do serviço contratado, informações de pagamento e o status de churn (se o cliente cancelou ou não).

## 🧠 Aprendizados

* Prática com análise exploratória de dados reais
* Segmentação e identificação de perfis de risco
* Técnicas para lidar com dados faltantes e inconsistências
* Criação de visualizações impactantes para comunicar insights
* Formulação de hipóteses e validação com SQL e Python

## 🛠️ Ferramentas Sugeridas

* PostgreSQL (para queries analíticas)
* Python (pandas, matplotlib, seaborn, plotly)
* Jupyter Notebook ou Google Colab

## 🎯 Desafios Propostos

### 🔹 Desafio 1: Perfil dos Clientes que Cancelaram

**Pergunta**: Quais são os perfis mais comuns entre os clientes que cancelaram o serviço?

Sugestão de filtros para segmentação:

* Gênero
* Tipo de plano (serviço contratado)
* Tempo de contrato

### 🔹 Desafio 2: Identificação de Clientes em Risco de Churn

**Pergunta**: Entre os clientes ativos, quais mostram padrões semelhantes aos clientes que cancelaram?

Sugestão de critérios para risco:

* Alta idade + pouco tempo de contrato
* Alta frequência de chamadas para o suporte
* Atraso frequente no pagamento

### 🔹 Desafio 3: Receita Gerada por Clientes Ativos

**Pergunta**: Qual é a receita total gerada por clientes ativos, segmentada por tipo de plano?

Utilizar colunas relacionadas a gasto mensal e serviços contratados.

### 🔹 Desafio 4: Taxa de Retenção Recentemente Engajados

**Pergunta**: Qual é a taxa de retenção de clientes ativos que interagiram com a empresa nos últimos 15 dias?

Estratificar por tipo de plano e comparar com o total de clientes ativos.

### 🔹 Desafio 5: Visualização de Fatores de Churn

**Pergunta**: Quais fatores mais se correlacionam com o cancelamento?

Recomenda-se uso de:

* 🔍 Heatmap de correlações
* 🔿️ Gráficos de dispersão
* 🔢 Boxplots por tipo de plano e gasto mensal

## 📁Folders Structure

````

└── 📁churn_telco
    └── 📁churn_telco
        └── __init__.py
        └── 📁context
            └── etl_context.py
        └── main.py
        └── 📁strategy
            └── ExtractStrategy.py
            └── LoadStrategy.py
            └── TransformStrategy.py
        └── 📁utils
            └── __init__.py
            └── config.py
    └── 📁data
        └── 📁raw
            └── WA_Fn-UseC_-Telco-Customer-Churn.csv
        └── 📁stage
            └── tb_WA_Fn-UseC_-Telco-Customer-Churn.parquet
    └── 📁scripts
        └── config_sample.yaml
    └── 📁tests
        └── test_config_read.py
        └── test_extract.py
        └── test_load.py
        └── test_main.py
        └── test_transform.py
    └── .gitignore
    └── .python-version
    └── config.yaml
    └── README.md
    └── requirements.txt
````

## 📄 Observação Final

Não serão incluídas as soluções neste README para incentivar a exploração independente. Sinta-se livre para compartilhar suas descobertas e visualizações.

````---

**Autor**: humphry Torres
**LinkedIn**: [humphrytorres](https://www.linkedin.com/in/humphrytorres)
**GitHub**: [ht-yarll](https://github.com/ht-yarll)
