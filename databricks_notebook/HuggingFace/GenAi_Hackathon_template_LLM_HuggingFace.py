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
# MAGIC
# MAGIC * Genie Spaces (Data Room)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Referências:
# MAGIC
# MAGIC * [Hugging Face models](https://huggingface.co/models) 
# MAGIC * [ML com Databricks](https://docs.databricks.com/en/machine-learning/index.html)
# MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/HuggingFaceHeader.png" width="900px">
# MAGIC
# MAGIC # Criando a base para o Hackathon [MUDAR IMAGEM]
# MAGIC Antes de criarmos nossas tabelas, precisamos criar um catálogo, um schema e um volume (que facilitará nosso processo de ingestão) para receber os arquivos da origem. 
# MAGIC * Catálogo:  Os objetos no Databricks (tabelas, views, modelos, etc), possuem o namespace composto por 3 partes. o catálogo é a primeira delas;
# MAGIC * Schema: Já o schema é o segundo nível deste namespace. Tanto o catálogo quanto o schema, servem para organização lógica simplificando a governança;
# MAGIC * Volume: O volume é um diretório onde você pode fazer upload de arquivos. O volume reside dentro de um schema, deixa o ambiente mais governado e facilita o desenvolvimento.
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <img style="float: left; margin-right: 20px" width="100px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Warning.png">
# MAGIC
# MAGIC ###Se você já possui as tabelas que pretende usar, avance para a sessão "Tratamento de dados".

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Criando o catálogo, schema e volume
# MAGIC
# MAGIC Tudo o que você precisará fazer, é preencher o widget no canto superior esquerdo chamado de **"Prefixo"**. O código abaixo se encarregará de fazer a criação de todo o necessário

# COMMAND ----------


prefixo = dbutils.widgets.get('Prefixo')  # USE O WIDGET NO CANTO SUPERIOR ESQUERDO PARA PREENCHER O PREFIXO DO SEU CATALOGO. SUGESTAO: INICIAIS DO SEU NOME + HACKATHON EXEMPLO: jsf_hackathon
catalog = prefix+"_catalog"
schema = prefix
volume = "genie_vol"

commands = [f"CREATE CATALOG IF NOT EXISTS {catalog}"
            ,f"CREATE SCHEMA IF NOT EXISTS {catalog}.{prefixo}"
            ,f"CREATE VOLUME IF NOT EXISTS {catalog}.{schema}.{volume}"
            ]
for sql_command in commands:
  print (f"Executando: {sql_command}")
  spark.sql(sql_command)


# COMMAND ----------

# MAGIC %md
# MAGIC ## Fazendo o upload dos arquivos
# MAGIC Siga os passos na célula abaixo, para realizar o upload dos seus dados para o volume que acabamos de criar

# COMMAND ----------

# MAGIC %md
# MAGIC 1 - > No menu esquerdo, com o botão direito, clique em **"Catálogo"** e selecione **"Abrir em uma nova aba"**. 
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="200px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Genie_catalog.jpeg">
# MAGIC
# MAGIC 2 - > Na nova aba, pesquise por **prefixo**_catalog. Onde **prefixo** é o valor que você definiu no passo anterior. Navegue até o volume chamado **genie_vol**, seguindo os passos da figura abaixo
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="300px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Genie_volume.jpeg">
# MAGIC
# MAGIC 3 - > No canto superior direito selecione **Upload to this volume**
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="300px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Genie_upload.jpeg">
# MAGIC
# MAGIC 4 - > No canto superior direito selecione **Upload to this volume**
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="300px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Genie_chooseFiles.jpeg">
# MAGIC
# MAGIC 5 - > Selecione ou arraste seus arquivos e em seguida clique em **upload**
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="400px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Genie_finishUpload.jpeg">
# MAGIC

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC #Criando tabelas
# MAGIC Agora que já temos os arquivos necessários no volume, podemos rodar o código abaixo para criar as tabelas.
# MAGIC
# MAGIC </br>
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="100px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/Warning.png">
# MAGIC
# MAGIC O código abaixo é um **acelerador** para criação de tabelas a partir de um **.json**, **.csv** ou **.parquet**. Caso seu dataset tenha algum requisito específico, **altere** o código de acordo com sua necessidade.

# COMMAND ----------

import os
from pyspark.sql import SparkSession

# Variável do path dos arquivos 
diretorio = f"/Volumes/{catalog}/{schema}/{volume}"

# Nesta etapa vamos ler todos os arquivos do diretório e criar uma tabela para cada arquivo
for nome_arquivo in os.listdir(diretorio):
        tipo_arquivo=nome_arquivo.split('.')[1]
        
        if tipo_arquivo =="csv" :
          df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(os.path.join(diretorio, nome_arquivo))
        if tipo_arquivo=="json":
          df = spark.read.format("json").option("inferSchema", "true").load(os.path.join(diretorio, nome_arquivo))
        if tipo_arquivo=="parquet":
          df = spark.read.format("parquet").option("inferSchema", "true").load(os.path.join(diretorio, nome_arquivo)) 
    
        # Seguindo a arquitetura medalhão, vamos remover a extensão do arquivo e adicionar o sulfixo _bronze ao nome das tabelas
        table_name = nome_arquivo.split('.')[0]+"_bronze"
        # Criando  tabela
        df.write.format("delta").mode("overwrite").saveAsTable(f"{catalog}.{schema}.{table_name}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Tratamento de Dados
# MAGIC
# MAGIC <img style="float: left; margin-right: 20px" width="400px" src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/medallion.jpeg">
# MAGIC
# MAGIC
# MAGIC * Se necessário, utilize a célula abaixo para transformar seus dados:
# MAGIC    * Joins
# MAGIC    * Data cleaning
# MAGIC    * Agregações
# MAGIC

# COMMAND ----------

#TO DO: Transforme seus dados nesta célula

# COMMAND ----------

# MAGIC %md
# MAGIC # Aplicações Comuns com LLMs
# MAGIC
# MAGIC Neste notebook, faremos um tour por algumas das principais aplicações comuns usando LLMs:
# MAGIC * Resumo
# MAGIC * Análise de sentimento
# MAGIC * Tradução
# MAGIC * Classificação zero-shot
# MAGIC * Aprendizado few-shot
# MAGIC
# MAGIC Veremos como modelos existentes, de código aberto (e proprietários) podem ser usados prontos para muitas aplicações. Para isso, usaremos modelos [Hugging Face](https://huggingface.co/models) e alguma engenharia de prompt simples.
# MAGIC
# MAGIC Em seguida, examinaremos as APIs do Hugging Face em mais detalhes para entender como configurar pipelines de LLM.
# MAGIC
# MAGIC ## Objetivos do Notebook
# MAGIC 1. Usar uma variedade de modelos existentes para uma variedade de aplicações comuns.
# MAGIC 1. Entender a engenharia de prompt básica.
# MAGIC 1. Construir uma solução de LLM com a sua base de dados.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Requerimentos
# MAGIC
# MAGIC * Criar um Cluster ML com o seguinge DBR ou posterior: **13.3.x-cpu-ml-scala2.12** e que seja **Single Node**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Aplicações Comuns de LLM
# MAGIC
# MAGIC O objetivo desta seção é familiarizá-lo com várias aplicações de LLM e mostrar o quão fácil pode ser começar com LLMs.
# MAGIC
# MAGIC Enquanto você passa pelos exemplos, observe os conjuntos de dados, modelos, APIs e opções usados. Esses exemplos simples podem ser pontos de partida quando você precisar construir sua própria aplicação.

# COMMAND ----------

# Importando do HF como carregar e criar o pipeline
from datasets import load_dataset
from transformers import pipeline

# COMMAND ----------

# MAGIC %md
# MAGIC ## Baixando um dataset 
# MAGIC ### [IMPORTANTE] 
# MAGIC Aqui baixa por volta de **300Mb**  de Dataset entre o HF e o seu Databricks. Não é baixado localmente no seu laptop

# COMMAND ----------

xsum_dataset = load_dataset(
    "xsum", version="1.2.0"
) 
xsum_dataset  

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Summarization
# MAGIC
# MAGIC Summarization can take two forms:
# MAGIC * `extractive` (selecting representative excerpts from the text)
# MAGIC * `abstractive` (generating novel text summaries)
# MAGIC
# MAGIC Here, we will use a model which does *abstractive* summarization.
# MAGIC
# MAGIC **Background reading**: The [Hugging Face summarization task page](https://huggingface.co/docs/transformers/tasks/summarization) lists model architectures which support summarization. The [summarization course chapter](https://huggingface.co/course/chapter7/5) provides a detailed walkthrough.
# MAGIC
# MAGIC In this section, we will use:
# MAGIC * **Data**: [xsum](https://huggingface.co/datasets/xsum) dataset, which provides a set of BBC articles and summaries.
# MAGIC * **Model**: [t5-small](https://huggingface.co/t5-small) model, which has 60 million parameters (242MB for PyTorch).  T5 is an encoder-decoder model created by Google which supports several tasks such as summarization, translation, Q&A, and text classification.  For more details, see the [Google blog post](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html), [code on GitHub](https://github.com/google-research/text-to-text-transfer-transformer), or the [research paper](https://arxiv.org/pdf/1910.10683.pdf).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Resumo de Texto
# MAGIC
# MAGIC O resumo pode assumir duas formas:
# MAGIC * `extractivo` (selecionando trechos representativos do texto)
# MAGIC * `abstrato` (gerando resumos de texto novos)
# MAGIC
# MAGIC Aqui, usaremos um modelo que faz resumo *abstrato*.
# MAGIC
# MAGIC **Leitura de fundo**: A [página de tarefas de resumo do Hugging Face](https://huggingface.co/docs/transformers/tasks/summarization) lista arquiteturas de modelo que suportam resumo. O [capítulo do curso de resumo](https://huggingface.co/course/chapter7/5) fornece uma explicação detalhada.
# MAGIC
# MAGIC Nesta seção, usaremos:
# MAGIC * **Dados**: [xsum](https://huggingface.co/datasets/xsum) conjunto de dados, que fornece um conjunto de artigos e resumos da BBC.
# MAGIC * **Modelo**: [t5-small](https://huggingface.co/t5-small) modelo, que tem 60 milhões de parâmetros (242MB para PyTorch). O T5 é um modelo codificador-decodificador criado pelo Google que suporta várias tarefas, como resumo, tradução, Q&A e classificação de texto. Para mais detalhes, consulte o [post do blog do Google](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html), [código no GitHub](https://github.com/google-research/text-to-text-transfer-transformer) ou o [artigo de pesquisa](https://arxiv.org/pdf/1910.10683.pdf).

# COMMAND ----------

#Mostra os 10 primeiros registro dos datasets
xsum_sample = xsum_dataset["train"].select(range(10))
display(xsum_sample.to_pandas())

# COMMAND ----------

# MAGIC %md Em seguida, usamos a ferramenta `pipeline` do Hugging Face para carregar um modelo pré-treinado. No construtor deste pipeline de LLM, especificamos:
# MAGIC * `task`: Este primeiro argumento especifica a tarefa principal. Veja [Tarefas do Hugging Face](https://huggingface.co/tasks) para mais informações.
# MAGIC * `model`: Este é o nome do modelo pré-treinado do [Hugging Face Hub](https://huggingface.co/models).
# MAGIC * `min_length`, `max_length`: Queremos que nossos resumos gerados estejam entre esses dois comprimentos de tokens.
# MAGIC * `truncation`: Alguns artigos de entrada podem ser muito longos para o LLM processar. A maioria dos LLMs tem limites fixos no comprimento das sequências de entrada. Esta opção informa ao pipeline para truncar a entrada, se necessário.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Baixando o modelo t5-small 
# MAGIC ### [IMPORTANTE] 
# MAGIC Aqui baixa por volta de **300Mb** do modelo entre o HF e o seu Databricks. Não é baixado localmente no seu laptop

# COMMAND ----------

summarizer = pipeline(
    task="summarization",
    model="t5-small",
    min_length=20,
    max_length=40,
    truncation=True,
) 

# COMMAND ----------

# Mostra um exemplo de artigo
display(xsum_sample["document"][0])

# COMMAND ----------

# Aplica resumo para 1 artigo
summarizer(xsum_sample["document"][0])

# COMMAND ----------

# Aplicar para todos os artigos
results = summarizer(xsum_sample["document"])

# COMMAND ----------

# Mostrando os resultados
import pandas as pd

display(
    pd.DataFrame.from_dict(results)
    .rename({"summary_text": "generated_summary"}, axis=1)
    .join(pd.DataFrame.from_dict(xsum_sample))[
        ["generated_summary", "summary", "document"]
    ]
)

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Sentiment analysis
# MAGIC
# MAGIC Sentiment analysis is a text classification task of estimating whether a piece of text is positive, negative, or another "sentiment" label.  The precise set of sentiment labels can vary across applications.
# MAGIC
# MAGIC **Background reading**: See the Hugging Face [task page on text classification](https://huggingface.co/tasks/text-classification) or [Wikipedia on sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis).
# MAGIC
# MAGIC In this section, we will use:
# MAGIC * **Data**: [poem sentiment](https://huggingface.co/datasets/poem_sentiment) dataset, which provides lines from poems tagged with sentiments `negative` (0), `positive` (1), `no_impact` (2), or `mixed` (3).
# MAGIC * **Model**: [fine-tuned version of BERT](https://huggingface.co/nickwong64/bert-base-uncased-poems-sentiment).  BERT, or Bidirectional Encoder Representations from Transformers, is an encoder-only model from Google usable for 11+ tasks such as sentiment analysis and entity recognition.  For more details, see this [Hugging Face blog post](https://huggingface.co/blog/bert-101) or the [Wikipedia page](https://en.wikipedia.org/wiki/BERT_&#40;language_model&#41;).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Análise de Sentimento
# MAGIC
# MAGIC A análise de sentimento é uma tarefa de classificação de texto que estima se um trecho de texto é positivo, negativo ou possui outro rótulo de "sentimento". O conjunto preciso de rótulos de sentimento pode variar conforme a aplicação.
# MAGIC
# MAGIC **Leitura**: Veja a [página de tarefas sobre classificação de texto](https://huggingface.co/tasks/text-classification) da Hugging Face ou a [Wikipedia sobre análise de sentimento](https://en.wikipedia.org/wiki/Sentiment_analysis).
# MAGIC
# MAGIC Nesta seção, usaremos:
# MAGIC * **Dados**: [poem sentiment](https://huggingface.co/datasets/poem_sentiment), um conjunto de dados que fornece versos de poemas etiquetados com sentimentos `negativo` (0), `positivo` (1), `sem impacto` (2) ou `misto` (3).
# MAGIC * **Modelo**: [versão treinada do BERT](https://huggingface.co/nickwong64/bert-base-uncased-poems-sentiment). BERT é um modelo apenas de codificador do Google utilizável para mais de 11 tarefas, como análise de sentimento e reconhecimento de entidades. Para mais detalhes, veja este [post no blog da Hugging Face](https://huggingface.co/blog/bert-101) ou a [página da Wikipedia](https://en.wikipedia.org/wiki/BERT_&#40;language_model&#41;).

# COMMAND ----------

#Carregando o dataset, que é pequeno.
poem_dataset = load_dataset(
    "poem_sentiment", version="1.0.0"
)

# COMMAND ----------


# Mostrando o Resultado
poem_sample = poem_dataset["train"].select(range(10))
display(poem_sample.to_pandas())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Baixando o modelo t5-small 
# MAGIC ### [IMPORTANTE] 
# MAGIC Aqui baixa por volta de **500Mb** do modelo entre o HF e o seu Databricks. Não é baixado localmente no seu laptop

# COMMAND ----------

#Baixando o modelo
sentiment_classifier = pipeline(
    task="text-classification",
    model="nickwong64/bert-base-uncased-poems-sentiment"  
)

# COMMAND ----------

display(poem_sample["verse_text"][1])

# COMMAND ----------

sentiment_classifier(poem_sample["verse_text"][1])

# COMMAND ----------

results = sentiment_classifier(poem_sample["verse_text"])

# COMMAND ----------

# Exibir o sentimento previsto lado a lado com o label verdadeiro e o texto original.
# A pontuação indica a confiança do modelo em sua previsão.
import pandas as pd
# join das predições
joined_data = (
    pd.DataFrame.from_dict(results)
    .rename({"label": "predicted_label"}, axis=1)
    .join(pd.DataFrame.from_dict(poem_sample).rename({"label": "true_label"}, axis=1))
)

# Mudança de Labeles
sentiment_labels = {0: "negative", 1: "positive", 2: "no_impact", 3: "mixed"}
joined_data = joined_data.replace({"true_label": sentiment_labels})

display(joined_data[["predicted_label", "true_label", "score", "verse_text"]])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tradução
# MAGIC
# MAGIC O modelo pode ser projetado para pares específicos de idiomas ou podem suportar mais de dois idiomas. Veremos ambos abaixo.
# MAGIC
# MAGIC **Leitura de fundo**: Veja a [página de task sobre tradução](https://huggingface.co/tasks/translation) da Hugging Face ou a [página da Wikipedia sobre tradução automática](https://en.wikipedia.org/wiki/Machine_translation).
# MAGIC
# MAGIC Nesta seção, usaremos:
# MAGIC * **Dados**: Usaremos algumas frases de exemplo codificadas. No entanto, há uma variedade de [dataset de tradução](https://huggingface.co/datasets?task_categories=task_categories:translation&sort=downloads) disponíveis na Hugging Face.
# MAGIC * **Modelos**:
# MAGIC    * [Helsinki-NLP/opus-mt-en-pt](https://huggingface.co/Helsinki-NLP/opus-mt-tc-big-en-pt) é usado para o primeiro exemplo de tradução do inglês ("en") para o portugês ("pt"). Este modelo é baseado no [Marian NMT](https://marian-nmt.github.io/), uma estrutura de tradução automática neural desenvolvida pela Microsoft e outros pesquisadores. Veja a [página do GitHub](https://github.com/Helsinki-NLP/Opus-MT) para código e links para recursos relacionados.
# MAGIC

# COMMAND ----------

en_to_pt_translation_pipeline = pipeline(
    task="translation",
    model="Helsinki-NLP/opus-mt-tc-big-en-pt"
)

# COMMAND ----------

en_to_pt_translation_pipeline(
    "The hackahton from databricks are great. I really liket to work with my fellow colleagues and develop data science projects"
)

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ### Zero-shot classification
# MAGIC
# MAGIC Zero-shot classification (or zero-shot learning) is the task of classifying a piece of text into one of a few given categories or labels, without having explicitly trained the model to predict those categories beforehand.  The idea appeared in literature before modern LLMs, but recent advances in LLMs have made zero-shot learning much more flexible and powerful.
# MAGIC
# MAGIC **Background reading**: See the Hugging Face [task page on zero-shot classification](https://huggingface.co/tasks/zero-shot-classification) or [Wikipedia on zero-shot learning](https://en.wikipedia.org/wiki/Zero-shot_learning).
# MAGIC
# MAGIC In this section, we will use:
# MAGIC * **Data**: a few example articles from the [xsum](https://huggingface.co/datasets/xsum) dataset used in the Summarization section above.  Our goal is to label news articles under a few categories.
# MAGIC * **Model**: [nli-deberta-v3-small](https://huggingface.co/cross-encoder/nli-deberta-v3-small), a fine-tuned version of the DeBERTa model.  The DeBERTa base model was developed by Microsoft and is one of several models derived from BERT; for more details on DeBERTa, see the [Hugging Face doc page](https://huggingface.co/docs/transformers/model_doc/deberta), the [code on GitHub](https://github.com/microsoft/DeBERTa), or the [research paper](https://arxiv.org/abs/2006.03654).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Classificação zero-shot
# MAGIC
# MAGIC Classificação zero-shot (ou aprendizado zero-shot) é a tarefa de classificar um texto em uma das poucas categorias ou rótulos fornecidos, sem ter treinado explicitamente o modelo para prever essas categorias anteriormente. A ideia apareceu na literatura antes dos modelos de linguagem modernos, mas os avanços recentes nesses modelos tornaram o aprendizado zero-shot muito mais flexível e poderoso.
# MAGIC
# MAGIC **Leitura de fundo**: Veja a [página de tarefas sobre classificação zero-shot](https://huggingface.co/tasks/zero-shot-classification) da Hugging Face ou a [Wikipedia sobre aprendizado zero-shot](https://en.wikipedia.org/wiki/Zero-shot_learning).
# MAGIC
# MAGIC Nesta seção, usaremos:
# MAGIC * **Dados**: alguns artigos de exemplo do conjunto de dados [xsum](https://huggingface.co/datasets/xsum) usado na seção de Resumo acima. Nosso objetivo é rotular artigos de notícias em algumas categorias.
# MAGIC * **Modelo**: [nli-deberta-v3-small](https://huggingface.co/cross-encoder/nli-deberta-v3-small), uma versão ajustada do modelo DeBERTa. O modelo base DeBERTa foi desenvolvido pela Microsoft e é um dos vários modelos derivados do BERT; para mais detalhes sobre o DeBERTa, veja a [página de documentação da Hugging Face](https://huggingface.co/docs/transformers/model_doc/deberta), o [código no GitHub](https://github.com/microsoft/DeBERTa) ou o [artigo de pesquisa](https://arxiv.org/abs/2006.03654).
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Baixando o modelo nli-deberta-v3-small 
# MAGIC ### [IMPORTANTE] 
# MAGIC Aqui baixa por volta de **600Mb** do modelo entre o HF e o seu Databricks. Não é baixado localmente no seu laptop

# COMMAND ----------

zero_shot_pipeline = pipeline(
    task="zero-shot-classification",
    model="cross-encoder/nli-deberta-v3-small"
)

# COMMAND ----------

#Criar uma função que classifica
def categorize_article(article: str) -> None:
    """
    This helper function defines the categories (labels) which the model must use to label articles.
    Note that our model was NOT fine-tuned to use these specific labels,
    but it "knows" what the labels mean from its more general training.

    This function then prints out the predicted labels alongside their confidence scores.
    """
    results = zero_shot_pipeline(
        article,
        candidate_labels=[
            "politics",
            "finance",
            "sports",
            "science and technology",
            "pop culture",
            "breaking news",
        ],
    )
    # Print the results nicely
    del results["sequence"]
    display(pd.DataFrame(results))

# COMMAND ----------

categorize_article(
    """
Simone Favaro got the crucial try with the last move of the game, following earlier touchdowns by Chris Fusaro, Zander Fagerson and Junior Bulumakau.
Rynard Landman and Ashton Hewitt got a try in either half for the Dragons.
Glasgow showed far superior strength in depth as they took control of a messy match in the second period.
Home coach Gregor Townsend gave a debut to powerhouse Fijian-born Wallaby wing Taqele Naiyaravoro, and centre Alex Dunbar returned from long-term injury, while the Dragons gave first starts of the season to wing Aled Brew and hooker Elliot Dee.
Glasgow lost hooker Pat McArthur to an early shoulder injury but took advantage of their first pressure when Rory Clegg slotted over a penalty on 12 minutes.
It took 24 minutes for a disjointed game to produce a try as Sarel Pretorius sniped from close range and Landman forced his way over for Jason Tovey to convert - although it was the lock's last contribution as he departed with a chest injury shortly afterwards.
Glasgow struck back when Fusaro drove over from a rolling maul on 35 minutes for Clegg to convert.
But the Dragons levelled at 10-10 before half-time when Naiyaravoro was yellow-carded for an aerial tackle on Brew and Tovey slotted the easy goal.
The visitors could not make the most of their one-man advantage after the break as their error count cost them dearly.
It was Glasgow's bench experience that showed when Mike Blair's break led to a short-range score from teenage prop Fagerson, converted by Clegg.
Debutant Favaro was the second home player to be sin-binned, on 63 minutes, but again the Warriors made light of it as replacement wing Bulumakau, a recruit from the Army, pounced to deftly hack through a bouncing ball for an opportunist try.
The Dragons got back within striking range with some excellent combined handling putting Hewitt over unopposed after 72 minutes.
However, Favaro became sinner-turned-saint as he got on the end of another effective rolling maul to earn his side the extra point with the last move of the game, Clegg converting.
Dragons director of rugby Lyn Jones said: "We're disappointed to have lost but our performance was a lot better [than against Leinster] and the game could have gone either way.
"Unfortunately too many errors behind the scrum cost us a great deal, though from where we were a fortnight ago in Dublin our workrate and desire was excellent.
"It was simply error count from individuals behind the scrum that cost us field position, it's not rocket science - they were correct in how they played and we had a few errors, that was the difference."
Glasgow Warriors: Rory Hughes, Taqele Naiyaravoro, Alex Dunbar, Fraser Lyle, Lee Jones, Rory Clegg, Grayson Hart; Alex Allan, Pat MacArthur, Zander Fagerson, Rob Harley (capt), Scott Cummings, Hugh Blake, Chris Fusaro, Adam Ashe.
Replacements: Fergus Scott, Jerry Yanuyanutawa, Mike Cusack, Greg Peterson, Simone Favaro, Mike Blair, Gregor Hunter, Junior Bulumakau.
Dragons: Carl Meyer, Ashton Hewitt, Ross Wardle, Adam Warren, Aled Brew, Jason Tovey, Sarel Pretorius; Boris Stankovich, Elliot Dee, Brok Harris, Nick Crosswell, Rynard Landman (capt), Lewis Evans, Nic Cudd, Ed Jackson.
Replacements: Rhys Buckley, Phil Price, Shaun Knight, Matthew Screech, Ollie Griffiths, Luc Jones, Charlie Davies, Nick Scott.
"""
)

# COMMAND ----------

categorize_article(
    """
The full cost of damage in Newton Stewart, one of the areas worst affected, is still being assessed.
Repair work is ongoing in Hawick and many roads in Peeblesshire remain badly affected by standing water.
Trains on the west coast mainline face disruption due to damage at the Lamington Viaduct.
Many businesses and householders were affected by flooding in Newton Stewart after the River Cree overflowed into the town.
First Minister Nicola Sturgeon visited the area to inspect the damage.
The waters breached a retaining wall, flooding many commercial properties on Victoria Street - the main shopping thoroughfare.
Jeanette Tate, who owns the Cinnamon Cafe which was badly affected, said she could not fault the multi-agency response once the flood hit.
However, she said more preventative work could have been carried out to ensure the retaining wall did not fail.
"It is difficult but I do think there is so much publicity for Dumfries and the Nith - and I totally appreciate that - but it is almost like we're neglected or forgotten," she said.
"That may not be true but it is perhaps my perspective over the last few days.
"Why were you not ready to help us a bit more when the warning and the alarm alerts had gone out?"
Meanwhile, a flood alert remains in place across the Borders because of the constant rain.
Peebles was badly hit by problems, sparking calls to introduce more defences in the area.
Scottish Borders Council has put a list on its website of the roads worst affected and drivers have been urged not to ignore closure signs.
The Labour Party's deputy Scottish leader Alex Rowley was in Hawick on Monday to see the situation first hand.
He said it was important to get the flood protection plan right but backed calls to speed up the process.
"I was quite taken aback by the amount of damage that has been done," he said.
"Obviously it is heart-breaking for people who have been forced out of their homes and the impact on businesses."
He said it was important that "immediate steps" were taken to protect the areas most vulnerable and a clear timetable put in place for flood prevention plans.
Have you been affected by flooding in Dumfries and Galloway or the Borders? Tell us about your experience of the situation and how it was handled. Email us on selkirk.news@bbc.co.uk or dumfries@bbc.co.uk.
"""
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Aprendizado Few-shot
# MAGIC
# MAGIC Em tarefas de few-shot learning, você dá ao modelo uma instrução, alguns exemplos de consulta-resposta de como seguir essa instrução e, em seguida, uma nova consulta. O modelo deve gerar a resposta para essa nova consulta. Essa técnica tem prós e contras: é muito poderosa e permite que os modelos sejam reutilizados para muitas mais aplicações, mas pode ser complicada e exigir uma engenharia de prompt significativa para obter bons e confiáveis resultados.
# MAGIC
# MAGIC **Leitura de fundo**: Veja a [página da Wikipedia sobre few-shot learning](https://en.wikipedia.org/wiki/Few-shot_learning_&#40;natural_language_processing&#41;) ou [este blog da Hugging Face sobre few-shot learning](https://huggingface.co/blog/few-shot-learning-gpt-neo-and-inference-api).
# MAGIC
# MAGIC Nesta seção, usaremos:
# MAGIC * **Tarefa**: Few-shot learning pode ser aplicado a muitas tarefas. Aqui, faremos análise de sentimento, que foi abordada anteriormente. No entanto, você verá como few-shot learning nos permite especificar rótulos personalizados, enquanto o modelo anterior foi ajustado para um conjunto específico de rótulos. Também mostraremos outras tarefas (de brinquedo) no final. Em termos da `tarefa` especificada no construtor do `pipeline` da Hugging Face, few-shot learning é tratado como uma tarefa de `text-generation`.
# MAGIC * **Dados**: Usamos alguns exemplos, incluindo um exemplo de tweet do post do blog linkado acima.
# MAGIC * **Modelo**: [gpt-neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B), uma versão do modelo GPT-Neo discutido no blog linkado acima. É um modelo transformer com 1,3 bilhões de parâmetros desenvolvido pela Eleuther AI. Para mais detalhes, veja o [código no GitHub](https://github.com/EleutherAI/gpt-neo) ou o [artigo de pesquisa](https://arxiv.org/abs/2204.06745).
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Baixando o modelo gpt-neo-1.3B
# MAGIC ### [IMPORTANTE] 
# MAGIC Aqui baixa por volta de **5Gb** do modelo entre o HF e o seu Databricks. Não é baixado localmente no seu laptop

# COMMAND ----------

# Vamos limitar o tokens
few_shot_pipeline = pipeline(
    task="text-generation",
    model="EleutherAI/gpt-neo-1.3B",
    max_new_tokens=10
)

# COMMAND ----------

# MAGIC %md **Dica**: Nos prompts de few-shot abaixo, separamos os exemplos com um token especial "###" e usamos o mesmo token para encorajar o LLM a encerrar sua saída após responder à consulta. Diremos ao pipeline para usar esse token especial como o token de fim de sequência (EOS) abaixo.

# COMMAND ----------

# Obtenha o ID do token para "###", que usaremos como o token EOS abaixo.
eos_token_id = few_shot_pipeline.tokenizer.encode("###")[0]


# COMMAND ----------

# Without any examples, the model output is inconsistent and usually incorrect.
results = few_shot_pipeline(
    """For each tweet, describe its sentiment:

[Tweet]: "This new music video was incredible"
[Sentiment]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])

# COMMAND ----------

# Sem quaisquer exemplos, a saída do modelo é inconsistente e geralmente incorreta.
results = few_shot_pipeline(
    """For each tweet, describe its sentiment:

[Tweet]: "This new music video was incredible"
[Sentiment]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])


# COMMAND ----------

# Com 1 exemplo pode acertar ou não.
results = few_shot_pipeline(
    """For each tweet, describe its sentiment:

[Tweet]: "This is the link to the article"
[Sentiment]: Neutral
###
[Tweet]: "This new music video was incredible"
[Sentiment]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])

# COMMAND ----------

# Agora com mais exemplos
results = few_shot_pipeline(
    """For each tweet, describe its sentiment:

[Tweet]: "I hate it when my phone battery dies."
[Sentiment]: Negative
###
[Tweet]: "My day has been 👍"
[Sentiment]: Positive
###
[Tweet]: "This is the link to the article"
[Sentiment]: Neutral
###
[Tweet]: "This new music video was incredible"
[Sentiment]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])

# COMMAND ----------

# O modelo as vezes erra, veja como fica referente a drinks!
results = few_shot_pipeline(
    """For each food, suggest a good drink pairing:

[food]: tapas
[drink]: wine
###
[food]: pizza
[drink]: soda
###
[food]: jalapenos poppers
[drink]: beer
###
[food]: scone
[drink]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])

# COMMAND ----------

# This example sometimes works and sometimes does not, when sampling.  Too abstract?
results = few_shot_pipeline(
    """Given a word describing how someone is feeling, suggest a description of that person.  The description should not include the original word.

[word]: happy
[description]: smiling, laughing, clapping
###
[word]: nervous
[description]: glancing around quickly, sweating, fidgeting
###
[word]: sleepy
[description]: heavy-lidded, slumping, rubbing eyes
###
[word]: confused
[description]:""",
    eos_token_id=eos_token_id,
)

print(results[0]["generated_text"])

# COMMAND ----------

# We override max_new_tokens to generate longer answers.
# These book descriptions were taken from their corresponding Wikipedia pages.
results = few_shot_pipeline(
    """Generate a book summary from the title:

[book title]: "Stranger in a Strange Land"
[book description]: "This novel tells the story of Valentine Michael Smith, a human who comes to Earth in early adulthood after being born on the planet Mars and raised by Martians, and explores his interaction with and eventual transformation of Terran culture."
###
[book title]: "The Adventures of Tom Sawyer"
[book description]: "This novel is about a boy growing up along the Mississippi River. It is set in the 1840s in the town of St. Petersburg, which is based on Hannibal, Missouri, where Twain lived as a boy. In the novel, Tom Sawyer has several adventures, often with his friend Huckleberry Finn."
###
[book title]: "Dune"
[book description]: "This novel is set in the distant future amidst a feudal interstellar society in which various noble houses control planetary fiefs. It tells the story of young Paul Atreides, whose family accepts the stewardship of the planet Arrakis. While the planet is an inhospitable and sparsely populated desert wasteland, it is the only source of melange, or spice, a drug that extends life and enhances mental abilities.  The story explores the multilayered interactions of politics, religion, ecology, technology, and human emotion, as the factions of the empire confront each other in a struggle for the control of Arrakis and its spice."
###
[book title]: "Blue Mars"
[book description]:""",
    eos_token_id=eos_token_id,
    max_new_tokens=50,
)

print(results[0]["generated_text"])
