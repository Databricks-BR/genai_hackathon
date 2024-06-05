-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Clusterização de NPS para Melhoria de Produto e Prevenção de Churn
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Fintechs  |
-- MAGIC | Departamento: | Custumer Services/Marketing |
-- MAGIC | Tipo de Solução: | Assistente GenAI/ Analise de Sentimento / Extrator de Termos / Classificação de Texto |

-- COMMAND ----------



-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GRUPO 07 - FINPAY
-- MAGIC
-- MAGIC | # | Nome do Integrante | Empresa | e-mail |
-- MAGIC | -- | -- | -- | -- |
-- MAGIC | 1 | Andrea Filgueiras | RecargaPay | andrea.filgueiras@recargapay.com |
-- MAGIC | 2 | Diego Belchior | RecargaPay | diego.belchior@recargapay.com |
-- MAGIC | 3 | Fernando Andrade | Finnet | fernando.andrade@finnet.com.br |
-- MAGIC | 4 | Lucas Campos | Finnet | lucas.barros@finnet.com.br |
-- MAGIC | 5 | Marcel Cortapasso | RecargaPay | marcel.cortapasso@recargapay.com | 
-- MAGIC | 6 | Silas Silva | Finnet | silas.silva@finnet.com.br | 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cenário Atual
-- MAGIC
-- MAGIC NPS - **net promoter score** - é uma das metodologias mais usadas por times de marketing e costumer services em empresas de technologia para indicar qual o nível de satisfação dos clientes com seus produtos e plataformas. Portanto, elevar os insights que podem ser retirados desta ferramenta é prioridade para que os times consigam otimizar as iniciativas de negocio.
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC A fim de atuar nas deficiencias dos produtos as empresas precisam conseguir traduzir as respostas do NPS em ações de produto. Entretanto, por mais que parte dos resultados sejam qualitativos, devido a grande massa de dados e falta de estruturação dos resultados encotrar inciativas diretas torna-se um desafio.
-- MAGIC
-- MAGIC </br></br>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Objetivo da Solução Proposta
-- MAGIC
-- MAGIC Fazer uma análise de sentimento dos feedbacks das notas de NPS classificando cada uma para que seja possível identificar:
-- MAGIC * potenciais clientes em processo de churn - direcionar para CS
-- MAGIC * Oportunidades de Melhoria no produto - direcionar para desenvolvimento de produtos
-- MAGIC * Oportunidades de Oferta de serviços já existente - direcionar para marketing
-- MAGIC
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC * Atuação preventiva do time de CS para clientes em possível processo de churn
-- MAGIC * Direcionamento de Oportunidade de Melhoria do serviço para o time de produtos
-- MAGIC * Oportunidade comercial para sugestões de melhoria de serviços já existentes 
-- MAGIC
-- MAGIC </br></br>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Técnicas Utilizadas
-- MAGIC
-- MAGIC * SQL AI
-- MAGIC * GENIE

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Referências:
-- MAGIC * [SQL AI](https://github.com/Databricks-BR/genai_hackathon/blob/main/databricks_notebook/sql_ai/GenAi_Hackathon_template_SQL_AI.sql)
-- MAGIC

-- COMMAND ----------

-- MAGIC %md ## Análise de Sentimentos
-- MAGIC
-- MAGIC Usando a analise de sentimentos da sql_ai criamos uma forma qual o sentimento de cada uma das nossas respostas

-- COMMAND ----------

-- MAGIC %md ## Análise dos dados
-- MAGIC
-- MAGIC Usando o Genie nos colocamos na cabeça de um analisa de cs que pode fazer perguntas diretas sobre os resultados
