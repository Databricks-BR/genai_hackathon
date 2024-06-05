-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  Estruturação de atas governamentais
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Farmaceutica|
-- MAGIC | Departamento: | NC TECH |
-- MAGIC | Tipo de Solução: | Extrator de Texto |

-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GRUPO 08 -Zolpidem
-- MAGIC
-- MAGIC
-- MAGIC | # | Nome do Integrante | Empresa | e-mail |
-- MAGIC | -- | -- | -- | -- |
-- MAGIC | 1 | Daniel Brenner | EMS | daniel.brenner@gruponc.net.br |
-- MAGIC | 2 | Gabriela Braga | EMS | gabriela.braga@ems.com.br |
-- MAGIC | 3 | Heleni Bailo | EMS | heleni.bailo@gruponc.net.br |
-- MAGIC | 4 | Henrique Nishi | EMS | henrique.nishi@gruponc.net.br |
-- MAGIC | 5 | Marcio Lima| EMS | marcio.lima@ems.com.br | 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cenário Atual
-- MAGIC
-- MAGIC Consulta de dados atraves de arquivos (atas) disponibilizados pelo Governo de forma manual, analise do resultados pós licitação/pregão.....
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC Falta de dados estruturados; Volume de informação; Análise de Preços; Perda de licitações;
-- MAGIC
-- MAGIC Comparar preços e avaliar competitividade das propostas; Base de dados estruturada contemplando dados relevantes para analise historica e viabilizar a tomada de decisão de forma assertiva.
-- MAGIC </br></br>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Objetivo da Solução Proposta
-- MAGIC
-- MAGIC Construçao de uma base de dados estruturada para potencializar a eficiência com relação a identificação de oportunidades em licitações.
-- MAGIC
-- MAGIC
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC * Dados confiaveis;
-- MAGIC * Redução de custos;
-- MAGIC * Analises assertivas;
-- MAGIC * Redução de perda de oportunidades; 
-- MAGIC * Minimizar a ruptura de estoque;
-- MAGIC
-- MAGIC
-- MAGIC
-- MAGIC
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
-- MAGIC * Provedor Cloud:   Azure 
-- MAGIC * Cluster / DB Runtime: Standard_DS3_v2 / 14.3
-- MAGIC * Bibliotecas utilizadas: transformers==4.30.2 ;"unstructured[pdf,docx]==0.10.30" ; langchain==0.1.5; llama-index==0.9.3;
-- MAGIC                           databricks-vectorsearch==0.22; pydantic==1.10.9; mlflow==2.10.1
-- MAGIC
-- MAGIC ### Técnicas Utilizadas
-- MAGIC
-- MAGIC * SQL com funções GenAI 
-- MAGIC * LLM Foundation:   LLAMA3
-- MAGIC * Fontes de Dados:  https://contratos.sistema.gov.br/transparencia/arp
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Referências:
-- MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
-- MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
-- MAGIC * [Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)
-- MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
-- MAGIC
-- MAGIC

-- COMMAND ----------

-- MAGIC %md ## Dados de pdf para tabela

-- COMMAND ----------

-- MAGIC %python
-- MAGIC install transformers==4.30.2 "unstructured[pdf,docx]==0.10.30" langchain==0.1.5 llama-index==0.9.3 databricks-vectorsearch==0.22 pydantic==1.10.9 mlflow==2.10.1
-- MAGIC dbutils.library.restartPython()

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df = (spark.read
-- MAGIC         .format('BINARYFILE')
-- MAGIC         .load("dbfs:/Volumes/hackthondatabricks/files/files/"))
-- MAGIC
-- MAGIC # Write the data as a Delta table
-- MAGIC # (df.write.saveAsTable('hackthondatabricks.files.pdf_raw')),
-- MAGIC df=spark.sql('select * from hackthondatabricks.files.pdf_raw')

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from unstructured.partition.auto import partition
-- MAGIC import re
-- MAGIC
-- MAGIC def extract_doc_text(x : bytes) -> str:
-- MAGIC   # Read files and extract the values with unstructured
-- MAGIC   sections = partition(file=io.BytesIO(x))
-- MAGIC   def clean_section(txt):
-- MAGIC     txt = re.sub(r'\n', '', txt)
-- MAGIC     return re.sub(r' ?\.', '.', txt)
-- MAGIC   # Default split is by section of document, concatenate them all together because we want to split by sentence instead.
-- MAGIC   return "\n".join([clean_section(s.text) for s in sections]) 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC byte_content = df.select("content").collect()[0][0]
-- MAGIC df1=extract_doc_text(df.select("content").collect()[0][0])

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from pyspark.sql.functions import lit
-- MAGIC df=df.withColumn('content',lit(df1))
-- MAGIC #df.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable("hackthondatabricks.files.pdf_silver")

-- COMMAND ----------

-- MAGIC %md ### Prepara extração
-- MAGIC
-- MAGIC Novamente, iremos criar uma função para facilitar a extração das informações

-- COMMAND ----------

CREATE OR REPLACE FUNCTION analyze_notes(note STRING)
    RETURNS STRUCT<ata: STRING, ultima_atualizacao: ARRAY<STRING>, vigencia: ARRAY<STRING>>
    RETURN FROM_JSON(
        AI_QUERY(
            'databricks-meta-llama-3-70b-instruct',
            CONCAT(
                'Com base na ata da licitacao a seguir, extraia as seguintes informações:
                - ata
                -ultima atualizacao
                -vigencia
                Retorne somente um JSON (nenhum texto fora do JSON) com o seguinte formato:
                {
                    "ata": "<string>",
                    "ultima_atualizacao": <lista eventos>,
                    "vigencia": <lista drogas>
                }
                Nota clíncia: ', note
            )
        ),
        "STRUCT<ata: STRING, ultima_atualizacao: ARRAY<STRING>, vigencia: ARRAY<STRING>>"
    );

-- COMMAND ----------

CREATE OR REPLACE FUNCTION itens_ata(note STRING)
    -- RETURNS STRUCT<numero: STRING, item: ARRAY<STRING>, aceita_adesao: ARRAY<STRING>, quantidade_maxima_adesao: ARRAY<STRING>,codigo: ARRAY<STRING>,tipo: ARRAY<STRING>,qtd_homologada: ARRAY<STRING>>
    RETURNS STRING 
    RETURN 
    --RETURN FROM_JSON(
        AI_QUERY(
            'databricks-meta-llama-3-70b-instruct',
            CONCAT(
                'Com base na ata da licitacao a seguir, extraia as seguintes informações:
                -numero
                -item da ata 
                -aceita adesao
                -quantidade maxima adesao
                -codigo
                -tipo
                -qtd_homologada
                Retorne um JSON (nenhum texto fora do JSON) com o seguinte formato:
                {
                    "numero": "<string>",
                    "item da ata": "<string>",
                    "aceita adesao": "<string>",
                    "quantidade maxima adesao" "<string>",
                    "codigo" "<string>",
                    "tipo" "<string>",
                    "qtd_homologada" "<string>"
                }
                Nota clíncia: ', note
            )
        )
        -- ,
        -- "STRUCT<numero: STRING, item: ARRAY<STRING>, aceita_adesao: ARRAY<STRING>, quantidade_maxima_adesao: ARRAY<STRING>,codigo: ARRAY<STRING>,tipo: ARRAY<STRING>,qtd_homologada: ARRAY<STRING>>"
    -- );

-- COMMAND ----------

-- MAGIC %md ### Extrai todas as informações
-- MAGIC
-- MAGIC De forma similar, vamos aplicar nosso modelo de forma massiva em todo o nosso conjunto de dados

-- COMMAND ----------

--CREATE OR REPLACE TABLE summaries AS
SELECT relatorio FROM (
  SELECT *, itens_ata(content) AS relatorio FROM hackthondatabricks.files.pdf_silver)

-- COMMAND ----------

--CREATE OR REPLACE TABLE summaries AS
SELECT Info_atas FROM (
  SELECT *, analyze_notes(content) AS Info_atas FROM hackthondatabricks.files.pdf_silver)
