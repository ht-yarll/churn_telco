# 📊 Projeto de Análise de Churn - Telco Customer Churn Dataset (IBM)

Este projeto tem como objetivo analisar e explorar dados de cancelamento de clientes (churn) no setor de telecomunicações, utilizando o dataset "Telco Customer Churn" disponibilizado pela IBM. O foco principal é a geração de um processo de ETL onde extraímos os dados de um csv local, normalizamos para deixar nos padrões de uma tabela Postgres e em seguida carregamos no banco de dados.

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
* Formulação de hipóteses e validação com SQL e Python
* Aplicação de conceitos dentro do SOLID
* Exercício de Object Calisthenics

## 🛠️ Ferramentas Sugeridas

* PostgreSQL (para queries analíticas)
* DBeaver (para acesso e conexão ao bancod e dados)
* Python (pandas, poalrs)
* Jupyter Notebook ou Google Colab

## 🎯 Desafios Propostos

### 🔹 Desafio 1: Perfil dos Clientes que Cancelaram

**Pergunta:**
Quais são os perfis mais comuns entre os clientes que cancelaram o serviço?

**Sugerido analisar por:**

* `gender` (Gênero)
* `internetservice` (Tipo de plano de internet)
* `contract` (Tipo de contrato)

**Objetivo:**
Identificar padrões sociodemográficos e de contratação que estejam mais associados ao churn.

````pgsql
SELECT
  COUNT(*) AS qtn_churn,
  gender,
  contract
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY gender, contract
ORDER BY qtn_churn DESC
````

### 🔹 Desafio 2: Cobrança Média por Tipo de Internet (Clientes Ativos)

**Pergunta:**
Qual é a média de cobrança mensal entre os clientes que ainda estão ativos (`churn = 'No'`), segmentados por tipo de serviço de internet?

**Colunas relevantes:**

* `monthlycharges`
* `internetservice`
* `churn`

````pgsql
SELECT
  ROUND(AVG(monthlycharges::DECIMAL), 2) AS avg_monthly_charges,
  internetservice AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
GROUP BY internetservice 
ORDER BY avg_monthly_charges DESC
````

### 🔹 Desafio 3: Top 3 Métodos de Pagamento Mais Associados a Cancelamentos

**Pergunta:**
Quais métodos de pagamento são mais utilizados por clientes que cancelaram o serviço?

**Colunas relevantes:**

* `paymentmethod`
* `churn`

**Objetivo:**
Listar os três métodos de pagamento com maior número de cancelamentos (`churn = 'Yes'`) e analisar se há concentração em alguma forma de pagamento específica.

````pgsql
SELECT 
  paymentmethod AS payment_method,
  count(*) AS churned_customers
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY payment_method 
ORDER BY churned_customers DESC
LIMIT 3
````

### 🔹 Desafio 4: Tempo Médio de Permanência e Proteção de Dispositivo

**Pergunta:**
Existe diferença significativa no tempo médio de permanência (`tenure`) entre os clientes que contratam ou não o serviço de **proteção de dispositivo**?

**Estratégia:**

* Comparar a média de `tenure` entre valores `Yes`, `No` e `No internet service` em `deviceprotection`.
* Cruzar com o tipo de `contract` para maior detalhamento.
* Focar inicialmente em clientes ativos, se necessário.

```
SELECT
  ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
  deviceprotection AS device_protection
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
GROUP BY device_protection 
ORDER BY avg_tenure DESC
```

### 🔹 Desafio 5 (Extra): Comparação Geral de Permanência

**Pergunta adicional:**
Como o tempo de permanência varia entre diferentes combinações de serviços contratados (ex: `streamingtv`, `techsupport`)?

**Objetivo:**
Encontrar combinações de serviços que favorecem a retenção e auxiliar na definição de estratégias de fidelização.

````pgsql
-- Com Churn
SELECT
  ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
  techsupport AS tech_supp,
  streamingmovies  AS streaming_movies,
  streamingtv  AS streaming_tv,
  internetservice  AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY tech_supp, streaming_movies, streaming_tv, internet_service 
ORDER BY avg_tenure DESC

-- Sem Churn
SELECT
  ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
  techsupport AS tech_supp,
  streamingmovies  AS streaming_movies,
  streamingtv  AS streaming_tv,
  internetservice  AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'No'
GROUP BY tech_supp, streaming_movies, streaming_tv, internet_service 
ORDER BY avg_tenure DESC
````

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

**Autor**: humphry Torres
**LinkedIn**: [humphrytorres](https://www.linkedin.com/in/humphrytorres)
**GitHub**: [ht-yarll](https://github.com/ht-yarll)
