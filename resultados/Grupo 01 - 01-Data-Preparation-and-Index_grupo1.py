# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC ## Título: Analise de pedidos não faturados
# MAGIC
# MAGIC | ITEM | DESCRIÇÃO |
# MAGIC | -- | -- |
# MAGIC | Indústria: | Manofatura, varejo |
# MAGIC | Departamento: | Tecnologia da informação |
# MAGIC | Tipo de Solução: | Assistente GenAI / Extrator de Termos / Gerador de Conteúdo / Sumarizador / Classificação de Texto |

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### GRUPO 01 - <Nome do Grupo>
# MAGIC
# MAGIC | # | Nome do Integrante | Empresa |
# MAGIC | -- | -- | -- |
# MAGIC | 1 | Victor Tavares Alvarenga | WEG |
# MAGIC | 2 | Vanessa de oliveira Gil | WEG |
# MAGIC | 3 | Jean Fernandes | Dpaschoal |
# MAGIC | 4 | Marcos Lima | Dpaschoal |
# MAGIC | 5 | Guilherme Lomar | Casas Bahias |

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Cenário Atual
# MAGIC
# MAGIC O modelo de dados da WEG Equipamentos Elétricos SA gera indicadores de Entrada, Carteira, e ROL para painéis corporativos no Tableau. A Carteira de Pedidos é uma expectativa de reconhecimento de receita após confirmação de ordens de venda, representando um "instantâneo" atual do documento de venda sem histórico de modificações. A Carteira pode ter datas replanejadas para maior assertividade nas previsões de receita. A Entrada de Pedidos é uma métrica histórica, com cada modificação no registro gerando versionamento na base de dados.
# MAGIC
# MAGIC </br></br>
# MAGIC
# MAGIC #### Dores / Necessidades do Negócio
# MAGIC
# MAGIC As dores e necessidades do negócio considerando o contexto da WEG incluem:
# MAGIC 1. A necessidade de monitorar e gerenciar a carteira de vendas, incluindo o Order Backlog (B1) e o Past Due Order Backlog (B1), com base em dados do SAP ECC e do BI. 
# MAGIC 2. A necessidade de converter os valores de vendas de uma moeda para outra, utilizando taxas diárias ou médias mensais, de acordo com as regras estabelecidas. 
# MAGIC 3. A necessidade de alinhar o procedimento de conversão de moeda do BI com o contábil, gravando os dados na base na moeda da produtora e convertendo-os para as demais moedas pré-definidas.
# MAGIC 4. Idententificar carteira com faturamento em atraso e identifcar metricas do motivo do atraso
# MAGIC 5. Gerar valor a partir das tabelas que contem informações de entrada carteira e rol
# MAGIC
# MAGIC </br></br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Objetivo da Solução Proposta
# MAGIC
# MAGIC A solução proposta é um chatbot inteligente que visa auxiliar colaboradores e representantes de vendas da WEG Equipamentos Elétricos SA em consultas relacionadas à entrada e carteira de pedidos, bem como ROL com dados estruturados e não estruturados. O chatbot foi desenvolvido para fornecer respostas precisas e rápidas a perguntas comuns sobre esses tópicos, ajudando a otimizar o tempo dos usuários e aprimorar a eficiência no acesso a informações relevantes. Além disso, a ferramenta é capaz de processar tanto dados estruturados quanto não estruturados, garantindo uma cobertura abrangente de informações e uma experiência de usuário mais satisfatória. 
# MAGIC
# MAGIC </br></br>
# MAGIC
# MAGIC #### Benefícios
# MAGIC  
# MAGIC 1. Acesso fácil e rápido à informações: Os usuários podem obter respostas imediatas para suas perguntas sobre entrada e carteira de pedidos, ROL e outros tópicos relevantes, sem a necessidade de procurar em documentos ou sistemas complexos.
# MAGIC 2. Compatibilidade com dados estruturados e não estruturados: O chatbot é capaz de processar e interpretar diferentes tipos de dados, garantindo uma abrangência maior nas respostas fornecidas. 
# MAGIC 3. Auxílio na tomada de decisão
# MAGIC 4. Facilidade de uso para usuario com pouco conhecemento tecnico
# MAGIC
# MAGIC </br></br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Arquitetura
# MAGIC
# MAGIC * Provedor Cloud: AWS
# MAGIC * Cluster / DB Runtime: i2.xlarge 13.3 (30.5-61 GB Memory, 4-8 Cores) scale 2 workers
# MAGIC * Bibliotecas utilizadas: langchain, mlflow, databricks
# MAGIC
# MAGIC ### Técnicas Utilizadas
# MAGIC
# MAGIC * SQL com funções GenAI
# MAGIC * LLM Foundation:   DBRX
# MAGIC * Fontes de Dados:  Entrada Carteira e ROL WEG
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Referências:
# MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
# MAGIC * [Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)
# MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
# MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
# MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
# MAGIC * [LengChain](https://python.langchain.com/v0.2/docs/introduction/)
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC # Preparação dos dados para nosso Chatbot com RAG
# MAGIC
# MAGIC ## Construindo e indexando nosso conhecimento com o Databricks Vector Search
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-managed-flow-1.png?raw=true" style="float: right; width: 800px; margin-left: 10px">
# MAGIC
# MAGIC Neste notebook, vamos ingerir as páginas da documentação da Datrabricks **(em Português)** e indexá-las com o Databricks Vector Search para ajudar nosso chatbot a fornecer respostas melhores.
# MAGIC
# MAGIC Preparar dados de alta qualidade é fundamental para o desempenho do seu chatbot. Recomendamos que você reserve um tempo para implementar essas etapas com seu próprio conjunto de dados.
# MAGIC
# MAGIC Felizmente, o Lakehouse AI oferece soluções de ponta para acelerar seus projetos de IA e LLMs, além de simplificar a ingestão e preparação de dados em escala.
# MAGIC
# MAGIC Para este exemplo, usaremos a documentação do Databricks em [docs.databricks.com/pt](docs.databricks.com/pt):
# MAGIC - Download das páginas web
# MAGIC - Dividir as páginas em pequenos trechos de texto
# MAGIC - Calcular os embeddings usando um Databricks Foundation Model
# MAGIC - Criar um índice no Databricks Vector Search
# MAGIC
# MAGIC <!-- Collect usage data (view). Remove it to disable collection or disable tracker during installation. View README for more details.  -->
# MAGIC <img width="1px" src="https://ppxrzfxige.execute-api.us-west-2.amazonaws.com/v1/analytics?category=data-science&org_id=1444828305810485&notebook=%2F01-quickstart%2F01-Data-Preparation-and-Index&demo_name=llm-rag-chatbot&event=VIEW&path=%2F_dbdemos%2Fdata-science%2Fllm-rag-chatbot%2F01-quickstart%2F01-Data-Preparation-and-Index&version=1">

# COMMAND ----------

# MAGIC %md 
# MAGIC ### 0. Pré-requisitos

# COMMAND ----------

# MAGIC %md #### Gerais
# MAGIC
# MAGIC 1. Antes de seguir adiante, revise os requisitos no notebook **[./requirements.md]($./requirements.md)**
# MAGIC 1. Customize as configurações no notebook **[../config]($../config)**

# COMMAND ----------

# MAGIC %md #### Instalar as bibliotecas necessárias

# COMMAND ----------

# MAGIC %pip install mlflow==2.10.1

# COMMAND ----------

# MAGIC %pip install mlflow==2.10.1 lxml==4.9.3 transformers==4.30.2 langchain==0.1.5 databricks-vectorsearch==0.22
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md #### Inicializar recursos e catálogo

# COMMAND ----------

# MAGIC %run ../_resources/00-init $reset_all_data=false

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## 1. Conjunto de dados da documentação da Databricks
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-data-prep-1.png?raw=true" style="float: right; width: 600px; margin-left: 10px">
# MAGIC
# MAGIC Primeiro, vamos acessar nosso conjunto de dados bruto como uma tabela Delta Lake.
# MAGIC
# MAGIC Para esta demonstração, já baixamos as páginas da documentação do docs.databricks.com/pt e salvamos o conteúdo HTML.
# MAGIC
# MAGIC Agora, vamos utilizar o Delta Sharing para acessar esses dados.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC **<font color="red">ANTES DE CONTINUAR, SIGA AS INSTRUÇÕES ABAIXO.</font>**
# MAGIC
# MAGIC ## Configure o acesso ao dataset
# MAGIC
# MAGIC 1. Peça a um dos intrutores para liberar o acesso ao dataset
# MAGIC 1. Acesse `Catalog` no menu principal à esquerda
# MAGIC 1. Acesse `Delta Sharing` > `Shared with me`
# MAGIC 1. Procure por `databricks-field-eng`
# MAGIC 1. Ao lado de `br-genai-hackathon`, clique em `Create catalog`
# MAGIC 1. Digite o nome `br-genai-hackathon` e clique em `Create`
# MAGIC
# MAGIC <img src="https://github.com/Databricks-BR/genai_hackathon/blob/main/images/sharing.gif?raw=true">

# COMMAND ----------

# %sql SELECT * FROM `br-genai-hackathon`.chatbot.raw_documentation LIMIT 100

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ## 2. Dividindo as páginas da documentação em pequenos trechos
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-data-prep-2.png?raw=true" style="float: right; width: 600px; margin-left: 10px">
# MAGIC
# MAGIC Os modelos de LLM possuem um comprimento máximo de contexto de entrada e você não poderá calcular embeddings para textos muito longos. Além disso, quanto maior for o comprimento do contexto, mais tempo o modelo levará para fornecer uma resposta.
# MAGIC
# MAGIC A preparação do documento é fundamental para o bom desempenho do seu modelo e existem várias estratégias dependendo do seu conjunto de dados:
# MAGIC
# MAGIC * Dividir o documento em pequenos trechos (parágrafo, h2...)
# MAGIC * Truncar documentos para um comprimento fixo
# MAGIC * O tamanho do trecho depende do seu conteúdo e de como você o usará para criar sua solicitação. Adicionar vários trechos pequenos de documentos em sua solicitação pode fornecer resultados diferentes do que enviar apenas um grande trecho
# MAGIC * Dividir em trechos grandes e pedir a um modelo para resumi-los para acelerar a inferência
# MAGIC * Criar vários agentes para avaliar cada documento maior em paralelo e pedir a um agente final para criar sua resposta...

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### Divindo a documentação por seções da página web
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/chunk-window-size.png?raw=true" style="float: right" width="700px">
# MAGIC <br/>
# MAGIC Nesta demonstração, temos artigos de documentação extensos, que são muito longos para serem usados como prompt para o nosso modelo.
# MAGIC
# MAGIC Não poderemos usar vários documentos como contexto RAG, pois eles excederiam nosso tamanho máximo de entrada. Alguns estudos recentes também sugerem que um tamanho de janela maior nem sempre é melhor, pois os LLMs parecem se concentrar no início e no final do prompt.
# MAGIC
# MAGIC No nosso caso, vamos dividir esses artigos entre as tags HTML h2, remover o HTML e garantir que cada trecho tenha menos de 500 tokens usando o LangChain. 
# MAGIC
# MAGIC #### LLM Window Size e Tokenizer
# MAGIC
# MAGIC A mesma frase pode retornar diferentes tokens para modelos diferentes. Os LLMs são fornecidos com um `Tokenizer` que você pode usar para contar os tokens de uma determinada frase (geralmente mais do que o número de palavras) (veja a [documentação do Hugging Face](https://huggingface.co/docs/transformers/main/tokenizer_summary) ou [OpenAI](https://github.com/openai/tiktoken)).
# MAGIC
# MAGIC Certifique-se de que o tokenizer que você estará usando corresponda ao seu modelo. O Databricks DBRX Instruct usa o mesmo tokenizer que o GPT4. Vamos usar a biblioteca `transformers` para contar os tokens do DBRX Instruct com seu tokenizer. Isso também manterá o tamanho dos tokens do nosso documento abaixo do tamanho máximo dos embeddings (1024).
# MAGIC
# MAGIC <br/>
# MAGIC <br style="clear: both">
# MAGIC <div style="background-color: #def2ff; padding: 15px;  border-radius: 30px; ">
# MAGIC   <strong>Nota</strong><br/>
# MAGIC   Lembre-se de que os seguintes passos são específicos para o seu conjunto de dados. Esta é uma parte crítica para construir um assistente RAG de sucesso.
# MAGIC   <br/> Sempre reserve um tempo para revisar manualmente os trechos criados e garantir que façam sentido e contenham informações relevantes.
# MAGIC </div>

# COMMAND ----------

# # Install package
%pip install --upgrade --quiet  "unstructured[all-docs]"

# COMMAND ----------

from langchain_community.document_loaders import UnstructuredFileLoader

# COMMAND ----------

loader = UnstructuredFileLoader('/Volumes/ai_dev/bronze/vlm_std/hackaton/BW1 DWA3 EntrCartRol.pdf')
docs = loader.load()

# COMMAND ----------

from langchain.text_splitter import HTMLHeaderTextSplitter, RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, OpenAIGPTTokenizer

max_chunk_size = 500
tokenizer = OpenAIGPTTokenizer.from_pretrained("openai-gpt")
text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )
texts = text_splitter.split_documents(docs)    


# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando os trechos e salvando-os em uma tabela Delta
# MAGIC
# MAGIC O último passo é aplicar nossa UDF em todo o texto da documentação e salvar os trechos extraídos na tabela `databricks_documentation`.
# MAGIC
# MAGIC *Observe que esta parte geralmente seria configurada como um job de produção, sendo executado assim que uma nova página de documentação for atualizada. <br/> Isso poderia ser configurado como um pipeline de Delta Live Table para consumir atualizações incrementalmente.*

# COMMAND ----------

# %sql
# -- Note that the Change Data Feed has been enabled on the table to allow for incremental feeding of the index
# -- CREATE TABLE entrcartrol_documentation (
#   texts STRING
# ) AS SELECT * FROM   USING DELTA;

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------

import pandas as pd
df = pd.DataFrame(texts)
df

# COMMAND ----------

dff = spark.createDataFrame(df)

# COMMAND ----------

from pyspark.sql.functions import col
from pyspark.sql.types import StringType

# Assuming you have a DataFrame 'df' and a column 'my_column'
dff = dff.withColumn("0", col("0").cast(StringType()))
dff

# COMMAND ----------

df_with_id = df_with_id.withColumn("1", col("1").cast(StringType()))
df_with_id = df_with_id.withColumn("2", col("2").cast(StringType()))


# COMMAND ----------

df_with_id.write.saveAsTable(
    name='ai_dev.silver.absdsl01700_docs_v3',
    mode='overwrite'
)

display(spark.table("ai_dev.silver.absdsl01700_docs_v3"))

# COMMAND ----------

display(spark.table("ai_dev.silver.absdsl01700_docs_v1"))

# COMMAND ----------

from pyspark.sql.functions import monotonically_increasing_id
df_with_id = dff.withColumn("id", monotonically_increasing_id())
df_with_id


# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE `ai_dev`.`silver`.`absdsl01700_docs_v3` SET TBLPROPERTIES (delta.enableChangeDataFeed = true)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## 3. Indexando a documentação no Databricks Vector Search
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/databricks-vector-search-managed-type.png?raw=true" style="float: right" width="800px">
# MAGIC
# MAGIC A Databricks fornece múltiplos tipos de índices no Vector Search:
# MAGIC
# MAGIC - **Managed embeddings**: você fornece uma coluna de texto e o nome do endpoint, e o Databricks sincroniza o índice com a sua tabela Delta
# MAGIC - **Self Managed embeddings**: você calcula os embeddings e os salva como um campo da sua tabela Delta, o Databricks então sincronizará o índice
# MAGIC - **Direct index**: quando você quer usar e atualizar seu índice sem uma tabela Delta
# MAGIC
# MAGIC Nesta demonstração, mostraremos como configurar um índice de **Managed Embeddings**.
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### Databricks BGE Embeddings Foundation Model endpoints
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-data-prep-4.png?raw=true" style="float: right; width: 600px; margin-left: 10px">
# MAGIC
# MAGIC Foundation Models são fornecidos pela Databricks e podem ser utilizados imediatamente.
# MAGIC
# MAGIC O Databricks suporta vários tipos de endpoints para calcular embeddings ou inferir com um modelo:
# MAGIC * **Foundation Model endpoint**: fornecido pela Databricks (ex: llama2-70B, MPT, BGE). **Utilizaremos esse**.
# MAGIC * **External endpoint**: atua como um gateway para um modelo externo (ex: Azure OpenAI)
# MAGIC * **Modelos customizados**: modelo refinado servido pelo Databricks Model Serving
# MAGIC
# MAGIC Abra a página [Model Serving](/ml/endpoints) para explorar e experimentar os Foundation Models.
# MAGIC
# MAGIC Para esta demonstração, usaremos os foundation models `BGE` (embeddings) e `llama2-70B` (chat). <br/><br/>
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/databricks-foundation-models.png?raw=true" width="600px" >

# COMMAND ----------

import mlflow.deployments
deploy_client = mlflow.deployments.get_deploy_client("databricks")

# Endpoints de Embeddings convertem texto em vetores. Segue um exemplo usando o BGE:
response = deploy_client.predict(endpoint="databricks-bge-large-en", inputs={"input": ["Origem do dado?"]})
embeddings = [e['embedding'] for e in response.data]
print(embeddings)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### Criando um Vector Search endpoint
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-data-prep-3.png?raw=true" style="float: right; width: 600px; margin-left: 10px">
# MAGIC
# MAGIC A função do **Vector Search endpoint** é servir os embeddings indexados (você pode pensar nele como um endpoint de API).
# MAGIC
# MAGIC Múltiplos índices podem usar o mesmo endpoint.
# MAGIC
# MAGIC Vamos começar criando um.

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient
vsc = VectorSearchClient()

VECTOR_SEARCH_ENDPOINT_NAME = 'weg-endpoint'

# if not endpoint_exists(vsc, VECTOR_SEARCH_ENDPOINT_NAME):
#     vsc.create_endpoint(name=VECTOR_SEARCH_ENDPOINT_NAME, endpoint_type="STANDARD")

# wait_for_vs_endpoint_to_be_ready(vsc, VECTOR_SEARCH_ENDPOINT_NAME)
# print(f"Endpoint named {VECTOR_SEARCH_ENDPOINT_NAME} is ready.")

# COMMAND ----------

# MAGIC %md Você pode ver os endpoint criados na página do [Vector Search](/compute/vector-search). Clique no nome do endpoint para ver todos os índices servidos.

# COMMAND ----------

# MAGIC %md-sandbox ### Criando um índice com Managed Embeddings e BGE
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/index_creation.gif?raw=true" width="600px" style="float: right">
# MAGIC
# MAGIC Com o Managed Embeddings, o Databricks calculará automaticamente os embeddings para nós. Este é o modo mais fácil de começar com o Databricks.
# MAGIC
# MAGIC Agora só precisamos pedir ao Databricks para criar o índice.
# MAGIC
# MAGIC Só precisamos especificar a coluna de texto e nosso modelo de embeddings (`BGE`) para que o Databricks calcule os embeddings automaticamente para nós.
# MAGIC
# MAGIC Isso pode ser feito usando a API ou em alguns cliques dentro do Unity Catalog Explorer.

# COMMAND ----------

from databricks.sdk import WorkspaceClient
import databricks.sdk.service.catalog as c

# A tabela a ser indexada
source_table_fullname = f"{catalog}.{db}.databricks_documentation"
# Onde armazanaremos o índice
vs_index_fullname = f"{catalog}.{db}.databricks_documentation_vs_index"

if not index_exists(vsc, VECTOR_SEARCH_ENDPOINT_NAME, vs_index_fullname):
  print(f"Creating index {vs_index_fullname} on endpoint {VECTOR_SEARCH_ENDPOINT_NAME}...")
  vsc.create_delta_sync_index(
    endpoint_name=VECTOR_SEARCH_ENDPOINT_NAME,
    index_name=vs_index_fullname,
    source_table_name=source_table_fullname,
    pipeline_type="TRIGGERED",
    primary_key="id",
    embedding_source_column='content',
    embedding_model_endpoint_name='databricks-bge-large-en'
  )
  # Espera que o índice esteja pronto e que todos os embeddings tenham sido criados
  wait_for_index_to_be_ready(vsc, VECTOR_SEARCH_ENDPOINT_NAME, vs_index_fullname)
else:
  # Dispara a atualização dos nossos embeddings com os novos dados salvos na tabela
  wait_for_index_to_be_ready(vsc, VECTOR_SEARCH_ENDPOINT_NAME, vs_index_fullname)
  vsc.get_index(VECTOR_SEARCH_ENDPOINT_NAME, vs_index_fullname).sync()

print(f"index {vs_index_fullname} on table {source_table_fullname} is ready")

# COMMAND ----------

# MAGIC %md 
# MAGIC ## 4. Testando a busca por conteúdos similares
# MAGIC
# MAGIC Isso é tudo que precisamos fazer. O Databricks irá capturar e sincronizar automaticamente novas entradas na sua Delta Live Table.
# MAGIC
# MAGIC Observe que, dependendo do tamanho do seu conjunto de dados e do modelo, a criação do índice pode levar alguns segundos para iniciar e indexar seus embeddings.
# MAGIC
# MAGIC Vamos experimentar e buscar por conteúdos similares.
# MAGIC
# MAGIC *Nota: `similarity_search` também possui um parâmetro de filtro. Isso é útil para adicionar uma camada de segurança ao seu sistema RAG: você pode filtrar algum conteúdo sensível com base em quem está fazendo a chamada (por exemplo, filtrar por um departamento específico com base na preferência do usuário).*

# COMMAND ----------

# import mlflow.deployments
# deploy_client = mlflow.deployments.get_deploy_client("databricks")

vs_index_fullname = 'ai_dev.silver.index'
question = "O que é Delta Live Tables?"

results = vsc.get_index(VECTOR_SEARCH_ENDPOINT_NAME, vs_index_fullname).similarity_search(
  query_text=question,
  columns=["0"],
  num_results=1)
docs = results.get('result', {}).get('data_array', [])
docs

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Próximo passo: Construir nosso Chatbot com RAG
# MAGIC
# MAGIC Vimos como o Databricks Lakehouse AI facilita a ingestão e preparação dos seus documentos, e como é possível implantar um índice do Vector Search em cima deles com apenas algumas linhas de código.
# MAGIC
# MAGIC Isso simplifica e acelera seus projetos de dados, permitindo que você se concentre no próximo passo: criar o endpoint do seu chatbot em tempo real com uma boa estratégia de RAG.
# MAGIC
# MAGIC Abra o notebook [02-Deploy-RAG-Chatbot-Model]($./02-Deploy-RAG-Chatbot-Model) para criar e operacionalizar seu chatbot.
