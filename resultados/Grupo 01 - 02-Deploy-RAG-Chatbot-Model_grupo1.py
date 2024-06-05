# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC # Construindo um Chatbot com Retrieval Augmented Generation (RAG)
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-managed-flow-2.png?raw=true" style="float: right; margin-left: 10px"  width="900px;">
# MAGIC
# MAGIC Nosso índice do Vector Search Index está pronto!
# MAGIC
# MAGIC Agora vamos construir e operacionalizar um novo endpoint do Model Serving para executar o chatbot.
# MAGIC
# MAGIC O processo será o seguinte:
# MAGIC
# MAGIC * Um usuário faz uma pergunta
# MAGIC * A pergunta é enviada para o nosso endpoint serverless do chatbot
# MAGIC * O endpoint calcula os embeddings e busca por documentos similares à pergunta, utilizando o Vector Search Index
# MAGIC * O endpoint cria um prompt enriquecido com o documento
# MAGIC * O prompt é enviado para o endpoint do Foundation Model DBRX Instruct
# MAGIC * Exibimos a saída para os usuários!
# MAGIC
# MAGIC <!-- Collect usage data (view). Remove it to disable collection or disable tracker during installation. View README for more details.  -->
# MAGIC <img width="1px" src="https://ppxrzfxige.execute-api.us-west-2.amazonaws.com/v1/analytics?category=data-science&org_id=1444828305810485&notebook=%2F01-quickstart%2F02-Deploy-RAG-Chatbot-Model&demo_name=llm-rag-chatbot&event=VIEW&path=%2F_dbdemos%2Fdata-science%2Fllm-rag-chatbot%2F01-quickstart%2F02-Deploy-RAG-Chatbot-Model&version=1">

# COMMAND ----------

# MAGIC %md 
# MAGIC ### 0. Pré-requisitos

# COMMAND ----------

# MAGIC %md #### Gerais
# MAGIC
# MAGIC 1. Antes de seguir adiante, revise os requisitos no notebook **[./requirements.md]($./requirements.md)**
# MAGIC 1. Customize as configurações no notebook **[../config]($../config)**
# MAGIC 1. Execute o notebook **[01-Data-Preparation-and-Index]($./01-Data-Preparation-and-Index)**
# MAGIC

# COMMAND ----------

# MAGIC %md #### Instalar as bibliotecas necessárias

# COMMAND ----------

# MAGIC %pip install mlflow==2.10.1 langchain databricks-vectorsearch==0.22 databricks-sdk==0.18.0 mlflow[databricks]
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md #### Inicializar recursos e catálogo

# COMMAND ----------

# MAGIC %run ../_resources/00-init $reset_all_data=false

# COMMAND ----------

# MAGIC %md #### (Opcional) Conceda as permissões para seu Service Principal

# COMMAND ----------

# from databricks.sdk import WorkspaceClient
# import databricks.sdk.service.catalog as c
# spark.sql(f'GRANT USAGE ON CATALOG {catalog} TO `{sp}`');
# spark.sql(f'GRANT USAGE ON DATABASE {catalog}.{db} TO `{sp}`');
# WorkspaceClient().grants.update(c.SecurableType.TABLE, f"{catalog}.{db}.databricks_documentation_vs_index", 
#                                 changes=[c.PermissionsChange(add=[c.Privilege["SELECT"]], principal=sp)])

# COMMAND ----------

# MAGIC %md #### Valide suas configurações

# COMMAND ----------

index_name= "ai_dev.silver.index" #f"{catalog}.{db}.databricks_documentation_vs_index"
host = "https://" + spark.conf.get("spark.databricks.workspaceUrl")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### 1. Definindo a busca de documentos relevantes do Vector Search
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-managed-model-1.png?raw=true" style="float: right" width="500px">
# MAGIC
# MAGIC Vamos começar construindo nosso Langchain retriever.
# MAGIC
# MAGIC Ele será responsável por:
# MAGIC
# MAGIC * Criar a pergunta de entrada (nosso Vector Search calculará os embeddings para nós)
# MAGIC * Chamar o índice do Vector Search para encontrar documentos similares para enriquecer o prompt
# MAGIC
# MAGIC Os módulos da Databricks para Langchain permite a execução desse processo em um único passo, lidando com toda a lógica e chamadas de API necessárias para você.

# COMMAND ----------

from databricks.vector_search.client import VectorSearchClient
from langchain_community.vectorstores import DatabricksVectorSearch
from langchain_community.embeddings import DatabricksEmbeddings

# Testa o Foundation Model BGE
# NOTA: este modelo de embedding deve ser o mesmo utilizado na indexação
embedding_model = DatabricksEmbeddings(endpoint="databricks-bge-large-en")
print(f"Embeddings: {embedding_model.embed_query('O que é Apache Spark?')[:20]}...")
VECTOR_SEARCH_ENDPOINT_NAME = 'weg-endpoint'
DATABRICKS_TOKEN = 'xxxxx'
def get_retriever(persist_dir: str = None):
    os.environ["DATABRICKS_HOST"] = host
    # Configura o client do Vector Search
    vsc = VectorSearchClient(workspace_url=host, personal_access_token=DATABRICKS_TOKEN)
    vs_index = vsc.get_index(
        endpoint_name=VECTOR_SEARCH_ENDPOINT_NAME,
        index_name=index_name
    )

    # Configura a busca
    vectorstore = DatabricksVectorSearch(
        vs_index, text_column="0", embedding=embedding_model
    )
    return vectorstore.as_retriever()


# Testa a busca
vectorstore = get_retriever()
similar_documents = vectorstore.get_relevant_documents("O que é Apache Spark?")
print(f"Documentos relevantes: {similar_documents}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ### 2. Definindo o Foundation Model para responder as perguntas
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-managed-model-3.png?raw=true" style="float: right" width="500px">
# MAGIC
# MAGIC Nosso chatbot usará o Foundation Model DBRX Instruct, da Databricks, para fornecer respostas. O DBRX Instruct é uma LLM (Language Model) de propósito geral, desenvolvido para criar aplicativos GenAI de nível empresarial, desbloqueando seus casos de uso com capacidades que antes eram limitadas a APIs de modelos proprietários.
# MAGIC
# MAGIC De acordo com nossos benchmarks, o DBRX supera o GPT-3.5 e é competitivo com o Gemini 1.0 Pro. Ele é especialmente capaz como um modelo de código, rivalizando com modelos especializados como o CodeLLaMA-70B em programação, além de sua força como um LLM de propósito geral.
# MAGIC
# MAGIC *Nota: vários tipos de endpoints ou modelos de langchain podem ser usados:*
# MAGIC
# MAGIC * Foundation Models **(o que usaremos)**
# MAGIC * Seus modelos customizados
# MAGIC * Modelos externos (como o Azure OpenAI)

# COMMAND ----------

# Testando o Databricks Foundation Model DBRX
from langchain_community.chat_models import ChatDatabricks
chat_model = ChatDatabricks(endpoint="databricks-dbrx-instruct", max_tokens = 200)
print(f"Test chat model: {chat_model.predict('O que é Apache Spark')}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC
# MAGIC ### 3. Construindo nosso Chatbot
# MAGIC
# MAGIC <img src="https://github.com/databricks-demos/dbdemos-resources/blob/main/images/product/chatbot-rag/llm-rag-managed-model-2.png?raw=true" style="float: right" width="600px">
# MAGIC
# MAGIC
# MAGIC Agora vamos mesclar a busca de documentos e o modelo em uma única cadeia Langchain.
# MAGIC
# MAGIC Vamos usar um modelo de prompt personalizado para nosso assistente fornecer uma resposta adequada.
# MAGIC
# MAGIC Certifique-se de dedicar um tempo para experimentar diferentes modelos e ajustar o tom e a personalidade do seu assistente de acordo com suas necessidades.

# COMMAND ----------

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatDatabricks

TEMPLATE = """Você é um assistente para usuários representantes de vendas da WEG Equipamentos Elétricos SA. Siga as intruções abaixo:
- Não responda perguntas caso não tenha informações suficientes.
- Mantenha a resposta o mais concisa possível.
Use os seguintes contextos para responder a pergunta no final:
{context}
Pergunta: {question}
Resposta:
"""
prompt = PromptTemplate(template=TEMPLATE, input_variables=["context", "question"])

chain = RetrievalQA.from_chain_type(
    llm=chat_model,
    chain_type="stuff",
    retriever=get_retriever(),
    chain_type_kwargs={"prompt": prompt}
)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Como é feito o cálculo final da quantidade de carteiras?"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "O que é carteira real?"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Quando as moedas são convertidas?"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Qual o cenário atual das entradas de carteira e ROL da WEG segundo o documento?"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

texto = "De acordo com o documento fornecido, a WEG Equipamentos Elétricos SA possui um modelo de dados para a geração dos dados dos indicadores de Entrada / Carteira / ROL, que é fonte de dados para os painéis corporativos criados utilizando a ferramenta Tableau. A CARTEIRA DE PEDIDOS representa uma expectativa para o reconhecimento da receita, pós confirmação da Ordem de venda. É uma “foto atual” do documento de venda, já que esta métrica não mantem o histórico das modificações, possuindo um começo e fim. A carteira pode ter suas datas replanejadas, visando maior assertividade nas previsões de receita baseadas na carteira. A ENTRADA DE PEDIDOS é uma métrica histórica, onde cada modificação no registro gera uma versionamento na base"

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": f"Melhore o seguinte texto de forma breve. Ele será utilizado em um pitch: {texto}"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Quais são as dores e necessidades do negócio considerando o contexto da WEG?"}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Foi criado um chatbot para responder sobre entrada e carteira de pedidos, ROL com dados estruturados e não estruturados. A ideia é auxiliar colaboradores e representantes de vendas com essa solução. Escreva um pitch falando sobre o objetivo da solução proposta."}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# langchain.debug = True #descomente essa linha para ver os detalhes da execução da cadeia
question = {"query": "Foi criado um chatbot para responder sobre entrada e carteira de pedidos, ROL com dados estruturados e não estruturados. A ideia é auxiliar colaboradores e representantes de vendas com essa solução. Escreva um pitch falando sobre os benefícios da solução proposta."}
answer = chain.run(question)
print(answer)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Registrando modelo no Unity Catalog
# MAGIC
# MAGIC Agora que nosso modelo está pronto, podemos registrá-lo no Unity Catalog

# COMMAND ----------

from mlflow.models import infer_signature
import mlflow
import langchain

mlflow.set_registry_uri("databricks-uc")
model_name = f"ai_dev.silver.dbdemos_chatbot_model"

with mlflow.start_run(run_name="dbdemos_chatbot_rag") as run:
    signature = infer_signature(question, answer)
    model_info = mlflow.langchain.log_model(
        chain,
        loader_fn=get_retriever,
        artifact_path="chain",
        registered_model_name=model_name,
        pip_requirements=[
            "mlflow==" + mlflow.__version__,
            "langchain==" + langchain.__version__,
            "databricks-vectorsearch"
        ],
        input_example=question,
        signature=signature
    )

# COMMAND ----------

# MAGIC %md **Conceder permissões ao SP no modelo**
# MAGIC
# MAGIC Podemos usar a interface do Catalog para conceder as permissões:
# MAGIC
# MAGIC 1. Acesse `Catalog` no menu principal à esquerda
# MAGIC 1. Encontre o seu modelo dentro do seu catálogo e banco de dados
# MAGIC 1. Vá para a guia `Permissões`
# MAGIC 1. Conceda a permissão `EXECUTE` ao SP

# COMMAND ----------

# MAGIC %md 
# MAGIC ### 5. Implantando nosso Chatbot usando o Model Serving
# MAGIC
# MAGIC Nosso modelo está registrado no Unity Catalog. O último passo é implantá-lo como um endpoint do Model Serving.
# MAGIC
# MAGIC Assim, poderemos enviar solicitações a partir da interface do nosso assistente.

# COMMAND ----------

# Criar ou atualiza o endpoint
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedModelInput, ServedModelInputWorkloadSize

serving_endpoint_name = f"dbdemos_endpoint_ai_dev_silver"[:63]
model_name = f"ai_dev.silver.dbdemos_chatbot_model"
host = "https://" + spark.conf.get("spark.databricks.workspaceUrl")
DATABRICKS_TOKEN = 'xxxxx'

def get_latest_model_version(model_name):
    mlflow_client = MlflowClient()
    latest_version = 1
    for mv in mlflow_client.search_model_versions(f"name='{model_name}'"):
        version_int = int(mv.version)
        if version_int > latest_version:
            latest_version = version_int
    return latest_version
    
latest_model_version = get_latest_model_version(model_name)

w = WorkspaceClient()
endpoint_config = EndpointCoreConfigInput(
    name=serving_endpoint_name,
    served_models=[
        ServedModelInput(
            model_name=model_name,
            model_version=latest_model_version,
            workload_size=ServedModelInputWorkloadSize.SMALL,
            scale_to_zero_enabled=True,
            environment_vars={
                "DATABRICKS_TOKEN": DATABRICKS_TOKEN,  # <scope>/<secret> that contains an access token
            }
        )
    ]
)


existing_endpoint = next(
    (e for e in w.serving_endpoints.list() if e.name == serving_endpoint_name), None
)
serving_endpoint_url = f"{host}/ml/endpoints/{serving_endpoint_name}"
if existing_endpoint == None:
    print(f"Criando endpoint {serving_endpoint_url}. Pode levar alguns minutos para terminar a implantação do endpoint...")
    w.serving_endpoints.create_and_wait(name=serving_endpoint_name, config=endpoint_config)
else:
    print(f"Atualizando o endpoint {serving_endpoint_url} para a versão {latest_model_version}. Pode levar alguns minutos para terminar a implantação do endpoint...")
    w.serving_endpoints.update_config_and_wait(served_models=endpoint_config.served_models, name=serving_endpoint_name)
    
displayHTML(f'Seu endpoint do Model Serving já está disponível. Abra seu <a href="/ml/endpoints/{serving_endpoint_name}">Model Serving Endpoint</a> para mais detalhes.')

# COMMAND ----------

# MAGIC %md Nosso endpoint agora está pronto! Você pode pesquisar o nome do endpoint na interface do Model Serving e visualizar seu desempenho!
# MAGIC
# MAGIC Vamos executar uma consulta REST para testá-lo em Python. Como você pode ver, podemos enviar uma pergunta e ele retornará um resposta com base na nossa documentação.

# COMMAND ----------

question = "Onde posso acompanhar meu consumo no Databricks?"

answer = w.serving_endpoints.query(serving_endpoint_name, inputs=[{"query": question}])
print(answer.predictions[0])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Parabéns! Você construiu seu primeiro Chabot com RAG usando Databricks!
# MAGIC
# MAGIC Agora você está pronto para implantar a mesma lógica para a sua base de conhecimento interna, aproveitando o Lakehouse AI.
# MAGIC
# MAGIC Vimos como o Lakehouse AI está posicionado de forma única para ajudar a resolver o desafio do GenAI:
# MAGIC
# MAGIC - Simplificar a ingestão e preparação de dados com as capacidades de engenharia do Databricks
# MAGIC - Acelerar a implantação de vector search com índices totalmente gerenciados
# MAGIC - Alavancar os Foundation Model endpoints do Databricks
# MAGIC - Implantar um endpoint de modelo em tempo real para executar RAG e fornecer recursos de perguntas e respostas
# MAGIC
# MAGIC O Lakehouse AI está posicionado de forma única para acelerar a implantação do seu GenAI.

# COMMAND ----------

# MAGIC %md # Limpeza
# MAGIC
# MAGIC Caso necessário, descomente a célula abaixo e a execute para remover todos os objetos criados

# COMMAND ----------

# /!\ ISTO IRÁ APAGAR TODO O SCHEMA USADO /!\ 
# cleanup_demo(catalog, db, serving_endpoint_name, f"{catalog}.{db}.databricks_documentation_vs_index")
