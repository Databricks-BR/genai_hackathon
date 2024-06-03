-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título: Assistente Jurídico para Reforma Tributária
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Todas as empresas impactadas pela Reforma Tributária brasileira |
-- MAGIC | Departamento: | Fiscal, Tributário e Jurídico |
-- MAGIC | Tipo de Solução: | Assistente GenAI  |

-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GRUPO 01 - <Nome do Grupo>
-- MAGIC
-- MAGIC | # | Nome do Integrante | Empresa | e-mail |
-- MAGIC | -- | -- | -- | -- |
-- MAGIC | 1 | nome | empresa | e-mail |
-- MAGIC | 2 | nome | empresa | e-mail |
-- MAGIC | 3 | nome | empresa | e-mail |
-- MAGIC | 4 | nome | empresa | e-mail |
-- MAGIC | 5 | nome | empresa | e-mail | 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cenário Atual
-- MAGIC
-- MAGIC Depois de 30 anos de discussão, a Câmara dos Deputados aprovou em 7 de julho de 2023 a primeira fase da reforma tributária e reformula a tributação sobre o consumo. O texto ainda precisa ser aprovado pelos senadores. A expectativa é que seja concluída a votação (em dois turnos) até o final de outubro de 2024, antes de ser promulgada. </br></br>
-- MAGIC O projeto de Lei que agora segue para o congresso, determinou diversos alterações em mais de 300 páginas e quase 500 artigos, que visa simplificar o sistema tributário brasileiro, substituindo tributos como PIS, Cofins, IPI, ICMS e ISS pelo Imposto sobre Operações com Bens e Serviços (IBS), modernizar o sistema, impulsionando a economia e promovendo competitividade empresarial.</br></br>
-- MAGIC O grande número de tributos, os diferentes métodos de apuração, as incertezas associadas ao “crédito físico”, as constantes alterações de regras e a grande quantidade de exceções fazem com que o recolhimento e a fiscalização tributária sejam extremamente complexos e custosos.</br></br>
-- MAGIC Apesar da Reforma Tributária buscar a simplificação do sistema, as fases de transição e adaptação dos processos e sistemas legados terão um grande impacto e esforço, pois as mudanças são estruturais, e vão requerer novas capacitações aos profissionais de Tax.
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC As empresas precisam adotar medidas estratégicas importantes, visando a análise dos possíveis impactos da Reforma Tributária em suas operações e isso envolve entender as mudanças que afetarão a carga tributária, os custos e os processos internos da empresa, passando pela capacitação da equipe para entender as novas regras e procedimentos tributários. A principal adaptação é ainda durante a fase de transição. Será preciso operar os tributos em duas perspectivas, o atual e o novo, ou seja, mais trabalho para a equipe interna. 
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Prazos da Reforma Tributária
-- MAGIC
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/reforma_tributaria.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Objetivo da Solução Proposta
-- MAGIC
-- MAGIC * Agilizar a busca por Informações sobre a Reforma Tributária
-- MAGIC * Democratizar o conhecimento sobre a Reforma Tributária
-- MAGIC * Utilizar tecnologias emergentes como Generative AI para funcionar como um Assitente Jurídico
-- MAGIC * Unificar e facilitar o acesso as informações e legislações sobre o tema
-- MAGIC * Acelerar a capacitação das equipes de TAX
-- MAGIC
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC A Reforma Tributária deve ser encarada como um **elemento disruptivo** no contexto da estratégia das organizações. Vantagem que tende a se materializar por meio de uma abordagem holística de gestão de riscos conversíveis em oportunidades, suportada por **TECNOLOGIA E ANÁLISE PREDITIVA DE DADOS DE FORMA INTEGRADA**, a ser convertida em uma alavanca poderosa de valor para o negócio.
-- MAGIC </br></br>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Arquitetura
-- MAGIC
-- MAGIC * Provedor Cloud:   Azure / AWS / GCP
-- MAGIC * Cluster / DB Runtime:   ____
-- MAGIC * Bibliotecas utilizadas: _____
-- MAGIC
-- MAGIC ### Técnicas Utilizadas
-- MAGIC
-- MAGIC * RAG - Retrieval Augmented Generation
-- MAGIC * LLM Foundation:   DBRX / LLAMA2 / LLAMA3 ...
-- MAGIC * Fontes de Dados:  _________
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Referências:
-- MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
-- MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
-- MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
-- MAGIC * outros ...
-- MAGIC * outros ...
-- MAGIC * [Emenda Constitucional - Reforma Tributária](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm)
-- MAGIC * [FAQ Reforma Tributária](https://www.gov.br/fazenda/pt-br/acesso-a-informacao/acoes-e-programas/reforma-tributaria/perguntas-e-respostas)
-- MAGIC * outros ...
-- MAGIC * outros ...
-- MAGIC * outros ...
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_unity_catalog.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Criando os Catálogos e as Tabelas - BASE DE TESTE

-- COMMAND ----------

create catalog hackathon;
use catalog hackathon;
create schema finance;
use finance;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC import pandas as pd
-- MAGIC from pyspark.sql import SparkSession
-- MAGIC
-- MAGIC url = f"https://raw.githubusercontent.com//Databricks-BR/genai_hackathon/main/datasets/"
-- MAGIC catalog_name = f"hackathon"
-- MAGIC schema_name = f"finance"
-- MAGIC
-- MAGIC
-- MAGIC entity_name = f"reforma_tributaria"
-- MAGIC table_name = f"{catalog_name}.{schema_name}.{entity_name}"
-- MAGIC file_name = f"{url}{entity_name}.csv"
-- MAGIC
-- MAGIC df = pd.read_csv(file_name)  # leitura arquivo CSV utilizando Dataframe Pandas
-- MAGIC s_df = spark.createDataFrame(df)  # converte Dataframe Pandas em Spark Dataframe
-- MAGIC s_df.write.mode("overwrite").saveAsTable(
-- MAGIC     table_name
-- MAGIC )  # grava o DataFrame na Tabela Delta

-- COMMAND ----------

select
  topico_texto,
  documento_texto
from
  hackathon.finance.reforma_tributaria

-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_rag.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC
-- MAGIC daqui em diante, utilizar o template de RAG
