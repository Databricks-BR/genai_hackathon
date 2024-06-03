# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC ## Título:  .......   < nome da sua Solução >
# MAGIC
# MAGIC | ITEM | DESCRIÇÃO |
# MAGIC | -- | -- |
# MAGIC | Indústria: | Saúde / Financeira / Varejo / ... |
# MAGIC | Departamento: | Comercial / Marketing / Jurídico / Contratos / Clínica Médica / ... |
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
# MAGIC | # | Nome do Integrante | Empresa | e-mail |
# MAGIC | -- | -- | -- | -- |
# MAGIC | 1 | nome | empresa | e-mail |
# MAGIC | 2 | nome | empresa | e-mail |
# MAGIC | 3 | nome | empresa | e-mail |
# MAGIC | 4 | nome | empresa | e-mail |
# MAGIC | 5 | nome | empresa | e-mail | 

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Cenário Atual
# MAGIC
# MAGIC descreva ...
# MAGIC </br></br>
# MAGIC
# MAGIC #### Dores / Necessidades do Negócio
# MAGIC
# MAGIC descreva ...
# MAGIC </br></br>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Objetivo da Solução Proposta
# MAGIC
# MAGIC Descreva como pretente resolver o problema....
# MAGIC
# MAGIC </br></br>
# MAGIC
# MAGIC #### Benefícios
# MAGIC
# MAGIC Descreva que benéficios, que melhorias, impactos... a solução trará pra empresa e/ou sociedade ...
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
# MAGIC * Provedor Cloud:   Azure / AWS / GCP
# MAGIC * Cluster / DB Runtime:   ____
# MAGIC * Bibliotecas utilizadas: _____
# MAGIC
# MAGIC ### Técnicas Utilizadas

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Referências:
# MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
# MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
# MAGIC * outros ...
# MAGIC * outros ...
# MAGIC * outros ...
# MAGIC * outros ...

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC # Recuperação-Augmentada de Geração (RAG)
# MAGIC
# MAGIC Em geral, uma arquitetura RAG é composta por dois tipos principais de modelos: o **modelo de recuperação** e o **modelo de geração**. Nesta demonstração, primeiro mostraremos como construir um modelo de recuperação usando tanto uma biblioteca de vetores (`FAISS`) quanto um banco de dados de vetores (`Chroma`). Em seguida, usaremos os resultados da recuperação para a etapa de geração.
# MAGIC
# MAGIC Neste notebook, implementaremos o fluxo de trabalho completo do RAG usando vetorização de texto, busca vetorial e o fluxo de trabalho de perguntas e respostas. Embora usemos [FAISS](https://faiss.ai/) (biblioteca de vetores) e [ChromaDB](https://docs.trychroma.com/) (banco de dados de vetores), e um modelo da Hugging Face, saiba que você pode facilmente trocar essas ferramentas pelos seus instrumentos ou modelos preferidos!
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/llm/updated_vector_search.png" width=1000 target="_blank" > 
# MAGIC
# MAGIC ## Objetivos de Aprendizagem
# MAGIC
# MAGIC Ao final desta demonstração, você deverá ser capaz de:
# MAGIC
# MAGIC 1. Implementar um fluxo de trabalho RAG de ponta a ponta (ler texto, converter texto em embeddings e salvá-los em um armazenamento vetorial).
# MAGIC 2. Consultar documentos semelhantes usando FAISS e ChromaDB.
# MAGIC 3. Aplicar um modelo de linguagem da Hugging Face para responder perguntas!
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %pip install faiss-cpu==1.7.4 chromadb==0.3.21

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC ## Preparando Dados
# MAGIC
# MAGIC Nesta seção, vamos usar os dados sobre <a href="https://newscatcherapi.com/" target="_blank">tópicos de notícias coletados pela equipe do NewsCatcher</a>, que coleta e indexa artigos de notícias e os libera para a comunidade de código aberto. O conjunto de dados pode ser baixado de <a href="https://www.kaggle.com/kotartemiy/topic-labeled-news-dataset" target="_blank">Kaggle</a>.

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

import pandas as pd

pdf = spark.table("`br-genai-hackathon`.huggingface_rag.labelled_newscatcher").toPandas()

pdf["id"] = pdf.index
display(pdf)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Modelo de Recuperação
# MAGIC
# MAGIC Converter texto em vetores de embeddings é o primeiro passo em qualquer pipeline de processamento de texto. À medida que a quantidade de texto aumenta, muitas vezes há a necessidade de salvar esses vetores de embeddings em um índice ou biblioteca de vetores dedicada, para que os desenvolvedores não precisem recomputar os embeddings e o processo de recuperação seja mais rápido. Podemos então buscar documentos com base em nossa consulta pretendida e passar esses documentos relevantes para um modelo de linguagem (LM) como contexto adicional. Também nos referimos a esse contexto como fornecer ao LM "estado" ou "memória". O LM então gera uma resposta com base no contexto adicional que recebe!

# COMMAND ----------

# MAGIC %md
# MAGIC ### Recuperação com a Biblioteca de Vetores: FAISS
# MAGIC
# MAGIC Bibliotecas de vetores são frequentemente suficientes para dados pequenos e estáticos. Como não é uma solução de banco de dados completa, não possui suporte CRUD (Create, Read, Update, Delete). Uma vez que o índice foi construído, se houver mais vetores que precisam ser adicionados/removidos/editados, o índice precisa ser reconstruído do zero.
# MAGIC
# MAGIC Dito isso, bibliotecas de vetores são fáceis, leves e rápidas de usar. Exemplos de bibliotecas de vetores são [FAISS](https://faiss.ai/), [ScaNN](https://github.com/google-research/google-research/tree/master/scann), [ANNOY](https://github.com/spotify/annoy) e [HNSM](https://arxiv.org/abs/1603.09320).
# MAGIC
# MAGIC FAISS tem várias maneiras de busca por similaridade: L2 (distância Euclidiana) e similaridade cosseno. Você pode ler mais sobre a implementação deles na página do [GitHub](https://github.com/facebookresearch/faiss/wiki/Getting-started#searching) ou no [post do blog](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/). Eles também publicaram seu próprio [guia de melhores práticas aqui](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index).
# MAGIC
# MAGIC Se você quiser ler mais sobre as comparações entre bibliotecas de vetores e bancos de dados, [aqui está um bom post de blog](https://weaviate.io/blog/vector-library-vs-vector-database#feature-comparison---library-versus-database).

# COMMAND ----------

# MAGIC %md
# MAGIC A visão geral do workflow geral está desenhada abaixo
# MAGIC
# MAGIC <img src="https://miro.medium.com/v2/resize:fit:1400/0*ouf0eyQskPeGWIGm" width=700>
# MAGIC
# MAGIC Fonte: [ Como usar FAISS para construir sua primeira busca de similaridade](https://medium.com/loopio-tech/how-to-use-faiss-to-build-your-first-similarity-search-bf0f708aa772).

# COMMAND ----------

from sentence_transformers import InputExample

pdf_subset = pdf.head(1000)

def example_create_fn(doc1: pd.Series) -> InputExample:
    """
    Helper function that outputs a sentence_transformer guid, label, and text
    """
    return InputExample(texts=[doc1])

faiss_train_examples = pdf_subset.apply(
    lambda x: example_create_fn(x["title"]), axis=1
).tolist()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Vectorize text into embedding vectors
# MAGIC We will be using the `Sentence-Transformers` [library](https://www.sbert.net/) to load a language model to vectorize our text into embeddings. The library hosts some of the most popular transformers on [Hugging Face Model Hub](https://huggingface.co/sentence-transformers).
# MAGIC Here, we are using the `model = SentenceTransformer("all-MiniLM-L6-v2")` to generate embeddings.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Vetorizar texto em vetores de embeding
# MAGIC Usaremos a biblioteca `Sentence-Transformers` [library](https://www.sbert.net/) para carregar um modelo de linguagem e vetorizar nosso texto em incorporações. A biblioteca hospeda alguns dos transformadores mais populares no [Hugging Face Model Hub](https://huggingface.co/sentence-transformers).
# MAGIC Aqui, estamos usando o `model = SentenceTransformer("all-MiniLM-L6-v2")` para gerar incorporações.
# MAGIC
# MAGIC Citations:
# MAGIC [1] https://www.sbert.net
# MAGIC [2] https://huggingface.co/sentence-transformers

# COMMAND ----------

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2", 
)  # Use a pre-cached model
faiss_title_embedding = model.encode(pdf_subset.title.values.tolist())
len(faiss_title_embedding), len(faiss_title_embedding[0])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Salvando vetores de embedding no índice do FAISS
# MAGIC Abaixo, criamos o objeto de índice do FAISS com base em nossos vetores de embedding, normalizamos vetores e adicionamos esses vetores ao índice do FAISS.

# COMMAND ----------

import numpy as np
import faiss

pdf_to_index = pdf_subset.set_index(["id"], drop=False)
id_index = np.array(pdf_to_index.id.values).flatten().astype("int")

content_encoded_normalized = faiss_title_embedding.copy()
faiss.normalize_L2(content_encoded_normalized)

# Index1DMap translates search results to IDs: https://faiss.ai/cpp_api/file/IndexIDMap_8h.html#_CPPv4I0EN5faiss18IndexIDMapTemplateE
# The IndexFlatIP below builds index
index_content = faiss.IndexIDMap(faiss.IndexFlatIP(len(faiss_title_embedding[0])))
index_content.add_with_ids(content_encoded_normalized, id_index)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Busca por documentos relevantes
# MAGIC
# MAGIC Definimos uma função de busca abaixo para primeiro vetorizar nosso texto de consulta e, em seguida, buscar os vetores com a distância mais próxima.

# COMMAND ----------

def search_content(query, pdf_to_index, k=3):
    query_vector = model.encode([query])
    faiss.normalize_L2(query_vector)

    # We set k to limit the number of vectors we want to return
    top_k = index_content.search(query_vector, k)
    ids = top_k[1][0].tolist()
    similarities = top_k[0][0].tolist()
    results = pdf_to_index.loc[ids]
    results["similarities"] = similarities
    return results

# COMMAND ----------

# MAGIC %md
# MAGIC Tada! Agora você pode consultar conteúdo semelhante! Observe que você não precisou configurar nenhuma rede de banco de dados anteriormente ou passar qualquer credencial. O FAISS funciona localmente com seu código.

# COMMAND ----------

display(search_content("animal", pdf_to_index))

# COMMAND ----------

# MAGIC %md
# MAGIC Up until now, we haven't done the last step of conducting Q/A with a language model yet. We are going to demonstrate this with Chroma, a vector database.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Recuperação com o Banco de Dados de Vetores: Chroma
# MAGIC
# MAGIC O Chroma é um banco de dados de embeddings de código aberto. A empresa acaba de arrecadar sua [financiamento de semente em abril de 2023](https://www.trychroma.com/blog/seed) e está rapidamente se tornando popular para apoiar aplicações baseadas em LLM.

# COMMAND ----------

import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="/tmp/llms-with-databricks/database.db",  # this is an optional argument. If you don't supply this, the data will be ephemeral. Optimatly, choose a proper directory
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Conceito Chroma: Coleção
# MAGIC
# MAGIC A `coleção` do Chroma é semelhante a um índice que armazena um conjunto de seus documentos.
# MAGIC
# MAGIC De acordo com a [documentação](https://docs.trychroma.com/getting-started):
# MAGIC > As coleções são onde você armazenará seus embeddings, documentos e metadados adicionais.
# MAGIC
# MAGIC O legal sobre o ChromaDB é que, se você não fornecer um modelo para vetorizar texto em embeddings, ele carregará automaticamente uma função de embedding padrão, ou seja, `SentenceTransformerEmbeddingFunction`. Ele pode lidar com tokenização, embedding e indexação automaticamente para você. Se você quiser mudar o modelo de embedding, leia [aqui como fazer isso](https://docs.trychroma.com/embeddings). TLDR: você pode adicionar um argumento opcional `model_name`.
# MAGIC
# MAGIC Você pode ler [a documentação aqui](https://docs.trychroma.com/usage-guide#using-collections) sobre as regras para nomes de coleção.

# COMMAND ----------

collection_name = "my_news"

# If you have created the collection before, you need to delete the collection first
if len(chroma_client.list_collections()) > 0 and collection_name in [chroma_client.list_collections()[0].name]:
    chroma_client.delete_collection(name=collection_name)

print(f"Creating collection: '{collection_name}'")
collection = chroma_client.create_collection(name=collection_name)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Etapa 1: Adicionar dados à coleção
# MAGIC
# MAGIC Como estamos reutilizando os mesmos dados, podemos pular a etapa de leitura dos dados. Como mencionado no texto acima, o Chroma pode cuidar da vetorização de texto para nós, portanto podemos adicionar texto diretamente à coleção e o Chroma converterá o texto em embeddings nos bastidores.

# COMMAND ----------

display(pdf_subset)

# COMMAND ----------

collection.add(
    documents=pdf_subset["title"][:100].tolist(),
    metadatas=[{"topic": topic} for topic in pdf_subset["topic"][:100].tolist()],
    ids=[f"id{x}" for x in range(100)],
)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Etapa 2: Consultar por 10 documentos relevantes sobre "espaço"
# MAGIC
# MAGIC Vamos retornar os 10 documentos mais relevantes. Você pode pensar em `10` como 10 vizinhos mais próximos. Você também pode alterar o número de resultados retornados.

# COMMAND ----------

import json

results = collection.query(query_texts=["space"], n_results=10)

print(json.dumps(results, indent=4))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Bônus: Adicionar uma instrução de filtro
# MAGIC
# MAGIC Além de realizar buscas por relevância, também podemos adicionar instruções de filtro. Consulte a [documentação](https://docs.trychroma.com/usage-guide#using-where-filters) para mais informações.

# COMMAND ----------

collection.query(query_texts=["space"], where={"topic": "SCIENCE"}, n_results=10)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Bônus: Atualizar dados em uma coleção
# MAGIC
# MAGIC Ao contrário de uma biblioteca de vetores, bancos de dados de vetores suportam alterações nos dados, portanto podemos atualizar ou excluir dados.
# MAGIC
# MAGIC De fato, podemos atualizar ou excluir dados em uma coleção do Chroma.

# COMMAND ----------

collection.delete(ids=["id0"])

# COMMAND ----------

# MAGIC %md
# MAGIC O registro com `ids=0` não está mais presente.

# COMMAND ----------

collection.get(
    ids=["id0"],
)

# COMMAND ----------

# MAGIC %md Nós também podemos atualizar um ponto em específico.

# COMMAND ----------

collection.get(
    ids=["id2"],
)

# COMMAND ----------

collection.update(
    ids=["id2"],
    metadatas=[{"topic": "TECHNOLOGY"}],
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Modelo de Geração
# MAGIC
# MAGIC Agora que identificamos documentos do conjunto de dados de notícias, podemos passar esses documentos como contexto adicional para um modelo de linguagem gerar uma resposta com base neles!
# MAGIC
# MAGIC Primeiramente, precisamos escolher um modelo de `text-generation`. Abaixo, usamos um modelo do Hugging Face. Você também poderia o [Databricks Foundation Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis).
# MAGIC
# MAGIC
# MAGIC ## Generation Model
# MAGIC
# MAGIC Now that we have identified documents about space from the news dataset, we can pass these documents as additional context for a language model to generate a response based on them! 
# MAGIC
# MAGIC We first need to pick a `text-generation` model. Below, we use a Hugging Face model. You can also use OpenAI as well, but you will need to get an Open AI token and [pay based on the number of tokens](https://openai.com/pricing). 

# COMMAND ----------

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
lm_model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline(
    "text-generation",
    model=lm_model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    device_map="auto",
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Aqui é onde entra o prompt engineering, que é o desenvolvimento de prompts. Nós passamos o contexto em nosso `prompt_template`, mas há inúmeras maneiras de escrever um prompt. Alguns prompts podem gerar resultados melhores do que outros e é necessário algum experimento para descobrir como melhor falar com o modelo. Cada modelo de linguagem se comporta de maneira diferente em relação aos prompts.
# MAGIC
# MAGIC Nosso modelo de prompt abaixo foi inspirado em [um artigo de 2023 sobre modelo de linguagem auxiliado por programa](https://arxiv.org/pdf/2211.10435.pdf). Os autores forneceram seu modelo de prompt de exemplo [aqui](https://github.com/reasoning-machines/pal/blob/main/pal/prompt/date_understanding_prompt.py).
# MAGIC
# MAGIC Os links abaixo também fornecem orientação útil sobre engenharia de prompts:
# MAGIC - [Prompt engineering com OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
# MAGIC - [Repositório do GitHub que compila as melhores práticas para interagir com o ChatGPT](https://github.com/f/awesome-chatgpt-prompts)

# COMMAND ----------

question = "What's the latest news on space development?"
context = " ".join([f"#{str(i)}" for i in results["documents"][0]])
prompt_template = f"Relevant context: {context}\n\n The user's question: {question}"

# COMMAND ----------

lm_response = pipe(prompt_template)
print(lm_response[0]["generated_text"])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Você acabou de completar a implementação da sua primeira arquitetura RAG usando vetorização de texto, busca e fluxo de perguntas & respostas (que requer prompt engineering)!

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Resumo
# MAGIC
# MAGIC Nesta demonstração, demonstramos como construir um modelo completo de RAG utilizando dois sistemas de armazenamento de vetores distintos. Inicialmente, ilustramos a utilização do FAISS, uma biblioteca de vetores, para armazenar embeddings e recuperar documentos com base em termos de pesquisa. Posteriormente, exploramos o uso do ChromaDB para armazenamento de documentos, incluindo a consulta e atualização de dados dentro do ChromaDB. Na parte final da demonstração, empregamos os resultados do modelo de recuperação como contexto para a geração de texto por meio da prompt engineering.
