# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

# COMMAND ----------

# MAGIC %md #### Instalar as bibliotecas necessárias

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

# MAGIC %md
# MAGIC
# MAGIC Lista de arquivos utilizados

# COMMAND ----------

content = ""
list_arq = []
for arq in dbutils.fs.ls("dbfs:/Volumes/dev/hackathon/hackathonfiles"):
    list_arq.append(arq.path.split("/")[-1])

print(list_arq)

# COMMAND ----------

# MAGIC %md
# MAGIC __Concatenação dos arquivos__

# COMMAND ----------

# Caminho do arquivo TXT
content = " "
for arq in list_arq:
    file_path = f"/Volumes/dev/hackathon/hackathonfiles/{arq}"

    # Abrir o arquivo em modo de leitura
    with open(file_path, 'r') as file:
        # Ler todo o conteúdo do arquivo como uma única string
        content += file.read()

    # Exibir o conteúdo
print(content)

# COMMAND ----------

# MAGIC %md
# MAGIC ----
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Geração dos Chanks com os arquivos txt

# COMMAND ----------

from transformers import OpenAIGPTTokenizer

# Configurações iniciais
max_chunk_size = 500  # Este é o limite de tokens desejado por chunk
chunk_overlap = 50

# Carregar o tokenizer do OpenAI GPT
tokenizer = OpenAIGPTTokenizer.from_pretrained("openai-gpt")

def split_text_into_safe_chunks(text, max_chunk_size, chunk_overlap):
    """ Divide o texto em chunks de tokens, assegurando que cada chunk esteja dentro do limite de tokens do modelo. """
    # Tokeniza o texto completo
    tokenized_text = tokenizer.encode(text)
    chunks = []
    start = 0

    while start < len(tokenized_text):
        # Determina o fim do chunk atual considerando o limite de tokens
        end = start + max_chunk_size
        if end < len(tokenized_text):
            # Adiciona sobreposição, mas verifica se ainda está dentro dos limites
            end_with_overlap = min(end + chunk_overlap, len(tokenized_text))
        else:
            end_with_overlap = end

        # Decodifica os tokens de volta para texto
        chunk = tokenizer.decode(tokenized_text[start:end_with_overlap])
        chunks.append(chunk)
        # Atualiza o índice de início para o próximo chunk, sem contar a sobreposição
        start += max_chunk_size

    return chunks

# Exemplo de uso
text = content
chunks = split_text_into_safe_chunks(text, max_chunk_size, chunk_overlap)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:", chunk)


# COMMAND ----------

# MAGIC %md
# MAGIC ----

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criação do df Spark

# COMMAND ----------

index = [c for c in range(len(chunks))]

# Combinar as listas em uma lista de tuplas
data = list(zip(index,chunks))

# Definir o esquema (nomes das colunas)
schema = ["index", "Chunks"]

# Criar o DataFrame
df = spark.createDataFrame(data, schema)

# Exibir o DataFrame
display(df)

# COMMAND ----------

(df
 .write
 .mode("overwrite")
 .option("overwriteSchema", "true")
 .option("mergeSchema", "true")
 .option("delta.enableChangeDataFeed", "true")
 .option("delta.autoOptimize.optimizeWrite", "true")
 .option("deltaTable.deletedFileRetentionDuration", "interval 60 days")
 .option("delta.logRetentionDuration", "interval 60 days")
 .option("delta.timeUntilArchived", "730 days")
 .option("delta.enableDeletionVectors", "true")
 .saveAsTable(f'dev.hackathon.chunks'))

# COMMAND ----------

# MAGIC %md
# MAGIC
