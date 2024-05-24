-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC # Identificação de Eventos Adversos
-- MAGIC
-- MAGIC <img src="https://www.databricks.com/en-website-assets/static/ddac5f0f20296db7ed3c559cdb727876/12369.png" style="float: right; padding-left: 10px" width=600>
-- MAGIC
-- MAGIC Para garantir a segurança contínua dos medicamentos, as empresas farmacêuticas precisam monitorar e relatar eventos adversos (ADE) após o lançamento no mercado. 
-- MAGIC
-- MAGIC Isso é desafiador, dado que a maioria dos eventos adversos são capturados em textos não-estruturados como emails, chamadas telefônicas e publicações em redes sociais. 
-- MAGIC
-- MAGIC * Extraia facilmente eventos adversos de grandes volumes de dados textuais com NLP
-- MAGIC * Classifique e correlacione automaticamente eventos adversos e entidades de drogas
-- MAGIC * Use visualizações integradas para avaliar a frequência dos eventos
-- MAGIC
-- MAGIC Neste notebook demonstramos a extração, processamento e análise de eventos adversos de medicamentos a partir de uma coleção de 20.000 conversas do mundo real usando processamento de linguagem natural (NLP) com modelos de Inteligência Artificial Generativa (GenAI).
-- MAGIC
-- MAGIC Então, nós armazenamos as entidades extraídas para realizarmos análises descritivas e associativas.
-- MAGIC
-- MAGIC *Este notebook foi baseado no solution accelerator [Adverse Drug Events Detection](https://github.com/databricks-industry-solutions/adverse-drug-events). Para mais informações, visite https://www.databricks.com/solutions/accelerators/adverse-drug-event-detection.*

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Conjunto de dados
-- MAGIC
-- MAGIC Utilizamos uma versão ligeiramente modificada de alguns textos conversacionais de ADE que podem ser baixados em https://sites.google.com/site/adecorpus/home/document. Veja
-- MAGIC >[Development of a benchmark corpus to support the automatic extraction of drug-related adverse effects from medical case reports](https://www.sciencedirect.com/science/article/pii/S1532046412000615)
-- MAGIC para mais informações sobre este conjunto de dados.
-- MAGIC
-- MAGIC Foram utilizados dois arquivos principais no conjunto de dados:
-- MAGIC
-- MAGIC - DRUG-AE.rel : Conversas com ADE
-- MAGIC - ADE-NEG.txt : Conversas sem ADE
-- MAGIC
-- MAGIC **Agora, vamos visualizar estes dados**

-- COMMAND ----------

-- MAGIC %md Aqui, definimos o banco de dados que utilizaremos

-- COMMAND ----------

USE vr_demo.hls_ade

-- COMMAND ----------

-- MAGIC %md E depois solicitamos uma amostra do nosso conjunto de dados

-- COMMAND ----------

SELECT * FROM clinical_notes LIMIT 100

-- COMMAND ----------

-- MAGIC %md Também podemos analisar a distribuição entre conversas com e sem ADEs

-- COMMAND ----------

select is_ADE, count(*) as from clinical_notes group by is_ADE

-- COMMAND ----------

-- MAGIC %md ## Principais Conceitos

-- COMMAND ----------

-- MAGIC %md-sandbox ### > Foundation Models
-- MAGIC
-- MAGIC <img src="https://docs.databricks.com/en/_images/serving-endpoints-list.png" style="float: right; padding-left: 10px" width=600>
-- MAGIC
-- MAGIC Primeiro, precisamos de um modelo capaz de interpretar o texto das notas clínicas e traduzí-las para Português. Para isso, vamos utilizar **[Foundation Models](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)**, que são grandes modelos de linguagem (LLMs) servidos pela Databricks e que podem ser consultados sob-demanda sem a necessidade de implantação ou gerenciamento desses recursos.
-- MAGIC
-- MAGIC Os modelos disponíveis são:
-- MAGIC
-- MAGIC | Model | Task type | Endpoint |
-- MAGIC | --- | --- | --- |
-- MAGIC | DBRX Instruct | Chat | databricks-dbrx-instruct |
-- MAGIC | Llama 2 70B Chat | Chat | databricks-llama-2-70b-chat |
-- MAGIC | Llama 3 70B Chat | Chat | databricks-meta-llama-3-70b-instruct |
-- MAGIC | Mixtral-8x7B Instruct | Chat | databricks-mixtral-8x7b-instruct |
-- MAGIC | MPT 7B Instruct | Completion | databricks-mpt-7b-instruct |
-- MAGIC | MPT 30B Instruct | Completion | databricks-mpt-30b-instruct |
-- MAGIC | BGE Large (English) | Embedding | databricks-bge-large-en |

-- COMMAND ----------

-- MAGIC %md-sandbox ### > AI Playground
-- MAGIC
-- MAGIC <img src="https://docs.databricks.com/en/_images/ai-playground.gif" style="float: right; padding-left: 10px" width=600>
-- MAGIC
-- MAGIC Para decidir qual o melhor modelo e instrução para o nosso caso de uso, podemos utilizar o **[Databricks AI Playground](https://docs.databricks.com/en/large-language-models/ai-playground.html)**.
-- MAGIC
-- MAGIC Assim, podemos testar rapidamente diversas combinações de modelos e instruções através de uma interface intuitiva e escolher a melhor opção par utilizarmos no nosso projeto.
-- MAGIC
-- MAGIC Vamos testar a seguinte instrução:
-- MAGIC
-- MAGIC *Traduza para Português o texto a seguir (não adicione nenhum texto além da tradução):*
-- MAGIC
-- MAGIC *CONCLUSION: The administration of tissue plasminogen activator was responsible for the large extent of hemorrhage and should be considered in the differential diagnosis of hemorrhagic choroidal detachment.*

-- COMMAND ----------

-- MAGIC %md ### > AI Functions
-- MAGIC
-- MAGIC Por fim, para que possamos escalar a utilização dos modelos de IA Generativa, podemos utilizar as **[Databricks AI Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)**.
-- MAGIC
-- MAGIC Estas permitem a utilização de SQL, uma linguagem amplamente utiliza por analistas de dados e de negócio, para executar uma LLM sobre nossos bancos de dados corporativos. Com isso, também podemos criar novas tabelas com as informações extraídas para serem utilizadas em nossas análises mais facilmente.
-- MAGIC
-- MAGIC Existem funções nativas para executar tarefas pré-definidas ou enviar qualquer instrução desejada para ser executada. Seguem as descrições abaixo:
-- MAGIC
-- MAGIC | Gen AI SQL Function | Descrição |
-- MAGIC | -- | -- |
-- MAGIC | [ai_analyze_sentiment](https://docs.databricks.com/pt/sql/language-manual/functions/ai_analyze_sentiment.html) | Análise de Sentimento |
-- MAGIC | [ai_classify](https://docs.databricks.com/pt/sql/language-manual/functions/ai_classify.html) | Classifica o texto de acordo com as categorias definidas |
-- MAGIC | [ai_extract](https://docs.databricks.com/pt/sql/language-manual/functions/ai_extract.html) | Extrai as entidades desejadas |
-- MAGIC | [ai_fix_grammar](https://docs.databricks.com/pt/sql/language-manual/functions/ai_fix_grammar.html) | Corrige a gramática do texto fornecido |
-- MAGIC | [ai_gen](https://docs.databricks.com/pt/sql/language-manual/functions/ai_gen.html) | Gera um novo texto conforme a instrução | 
-- MAGIC | [ai_mask](https://docs.databricks.com/pt/sql/language-manual/functions/ai_mask.html) | Marcara dados sensíveis |
-- MAGIC | [ai_query](https://docs.databricks.com/pt/sql/language-manual/functions/ai_query.html) | Envia instruções para o modelo desejado |
-- MAGIC | [ai_similarity](https://docs.databricks.com/pt/sql/language-manual/functions/ai_similarity.html) | Calcula a similaridade entre duas expressões |
-- MAGIC | [ai_summarize](https://docs.databricks.com/pt/sql/language-manual/functions/ai_summarize.html) | Sumariza o texto fornecido |
-- MAGIC | [ai_translate](https://docs.databricks.com/pt/sql/language-manual/functions/ai_translate.html) | Traduz o texto fornecido |

-- COMMAND ----------

-- MAGIC %md ## Tradução das notas
-- MAGIC
-- MAGIC Nosso conjunto de dados original está em Inglês. Infelizmente, conjuntos de dados médicos/clínicos em Português são muito raros e, usualmente, são proprietários. Por isso, aproveitaremos os modelos de IA Generativa disponíveis no Databricks para traduzir esses textos.

-- COMMAND ----------

-- MAGIC %md ### Teste de tradução
-- MAGIC
-- MAGIC Primeiro, para simplificar a consulta aos modelos de Gen AI, vamos utilizar a função nativa **`AI_QUERY`**. Esta permite enviar consultas para o modelo fundacional desejado. No nosso caso, iremos solicitar a tradução ao **`DBRX`**.
-- MAGIC
-- MAGIC Vamos fazer um teste abaixo

-- COMMAND ----------

SELECT AI_QUERY('databricks-dbrx-instruct',
  'Traduza para Português o texto a seguir (não adicione nenhum texto além da tradução):
   CONCLUSION: The administration of tissue plasminogen activator was responsible for the large extent of hemorrhage and should be considered in the differential diagnosis of hemorrhagic choroidal detachment.') AS text

-- COMMAND ----------

-- MAGIC %md ### Prepara tradução
-- MAGIC
-- MAGIC Agora, definiremos uma função para que qualquer pessoa consiga traduzir facilmente qualquer documento para Português.

-- COMMAND ----------

CREATE OR REPLACE FUNCTION translate_to_pt(text STRING)
    RETURNS STRING
    RETURN AI_QUERY(
        'databricks-dbrx-instruct',
        CONCAT(
            'Traduza para Português o texto a seguir (não adicione nenhum texto além da tradução): ', text
        )
    );

-- COMMAND ----------

-- MAGIC %md E podemos testar nossa função

-- COMMAND ----------

SELECT translate_to_pt('''
  CONCLUSION: The administration of tissue plasminogen activator was responsible for the large extent of hemorrhage and should be considered in the differential diagnosis of hemorrhagic choroidal detachment.
''')

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Traduz todas as notas
-- MAGIC
-- MAGIC Vamos aplicar esta função em todo o nosso conjunto de dados original para gerar uma versão em Português

-- COMMAND ----------

CREATE OR REPLACE TABLE clinical_notes_pt AS
SELECT id, translate_to_pt(text) AS text, is_ADE FROM clinical_notes

-- COMMAND ----------

-- MAGIC %md E podemos visualizar o conjunto de dados resultante

-- COMMAND ----------

SELECT * FROM clinical_notes_pt LIMIT 100

-- COMMAND ----------

-- MAGIC %md ## Classificação de notas e extração entidades
-- MAGIC
-- MAGIC Agora, vamos tentar identificar a presença de ADEs nos textos utilizando novamente a função `AI_QUERY` e outro modelo fundacional, o `LLAMA 3`.
-- MAGIC
-- MAGIC Além disso, também vamos extrair as seguintes entidades:
-- MAGIC * Eventos adversos
-- MAGIC * Drogas

-- COMMAND ----------

-- MAGIC %md ### Prepara extração
-- MAGIC
-- MAGIC Novamente, iremos criar uma função para facilitar a extração das informações

-- COMMAND ----------

CREATE OR REPLACE FUNCTION analyze_clinical_notes(note STRING)
    RETURNS STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>
    RETURN FROM_JSON(
        AI_QUERY(
            'databricks-meta-llama-3-70b-instruct',
            CONCAT(
                'Com base na nota clínica a seguir, extraia as seguintes informações:
                - identifique a presença de evento adverso: S ou N
                - tipos de eventos adversos
                - drogas mencionadas
                Retorne somente um JSON (nenhum texto fora do JSON) com o seguinte formato:
                {
                    "presenca_evento": "<S ou N>",
                    "eventos": <lista eventos>,
                    "drogas": <lista drogas>
                }
                Nota clíncia: ', note
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    );

-- COMMAND ----------

-- MAGIC %md E podemos testar a extração

-- COMMAND ----------

SELECT analyze_clinical_notes('''
  CONCLUSÃO: A administração de ativador tissular do plasminogênio foi responsável pela grande extensão da hemorragia e deve ser considerada no diagnóstico diferencial de descolamento hemorrágico coroideano.
''') AS summary

-- COMMAND ----------

-- MAGIC %md ### Extrai todas as informações
-- MAGIC
-- MAGIC De forma similar, vamos aplicar nosso modelo de forma massiva em todo o nosso conjunto de dados

-- COMMAND ----------

CREATE OR REPLACE TABLE summaries AS
SELECT id, text, is_ADE, s.* FROM (
  SELECT *, analyze_clinical_notes(text) AS s FROM clinical_notes_pt)

-- COMMAND ----------

-- MAGIC %md E aqui podemos ver o resultado da extração

-- COMMAND ----------

SELECT * FROM summaries

-- COMMAND ----------

-- MAGIC %md ### Avalia a detecção de eventos
-- MAGIC
-- MAGIC Em geral, tarefas de classificação são avaliadas comparando as predições dos modelos com as observações feitas por humanos.

-- COMMAND ----------

-- MAGIC %md Abaixo, geramos uma matriz de confusão, onde o eixo X representa o valor verdadeiro, o eixo Y representa o valor predito pelo modelo e as cores representam a frequência

-- COMMAND ----------

SELECT is_ADE, presenca_evento, count(*) FROM summaries WHERE presenca_evento IS NOT NULL GROUP BY ALL

-- COMMAND ----------

-- MAGIC %md E também medimos a acuracidade geral do modelo

-- COMMAND ----------

SELECT SUM(CASE WHEN (is_ADE = TRUE AND presenca_evento = 'S') OR (is_ADE = FALSE AND presenca_evento = 'N') THEN 1 END) / COUNT(*) AS acuracidade FROM summaries

-- COMMAND ----------

-- MAGIC %md ## Análise dos dados
-- MAGIC
-- MAGIC Agora, com as entidades extraídas a partir dos textos conversacionais, vamos realizar análises para investigar os ADEs mais comuns e suas correlações com as drogas

-- COMMAND ----------

-- MAGIC %md ### Descritivas
-- MAGIC
-- MAGIC Vamos dar uma olhada rápida nas principais tendências nos dados

-- COMMAND ----------

-- MAGIC %md #### Drogas mais comuns

-- COMMAND ----------

SELECT droga, count(*) AS cnt FROM (SELECT explode(drogas) AS droga FROM summaries)
GROUP BY droga ORDER BY cnt DESC LIMIT 10

-- COMMAND ----------

-- MAGIC %md #### Eventos mais comuns

-- COMMAND ----------

SELECT evento, count(*) AS cnt FROM (SELECT explode(eventos) AS evento FROM summaries)
GROUP BY evento ORDER BY cnt DESC LIMIT 10

-- COMMAND ----------

-- MAGIC %md ### Associativas
-- MAGIC
-- MAGIC Agora vamos investigar quais ADEs estão relacionadas a cada droga

-- COMMAND ----------

-- MAGIC %md #### Droga x Evento
-- MAGIC
-- MAGIC Primeiro, vamos observar a coocorrência entre os pares de ADEs e drogas em um mesmo documento.
-- MAGIC
-- MAGIC Para facilitar nossa análise, criamos um mapa de calor com estas informações

-- COMMAND ----------

SELECT droga, evento, count(*) AS cnt FROM (SELECT explode(drogas) AS droga, explode(eventos) AS evento FROM vr_demo.hls_ade.summaries)
GROUP BY ALL ORDER BY cnt DESC LIMIT 100

-- COMMAND ----------

-- MAGIC %md #### Droga x Evento Normalizado
-- MAGIC
-- MAGIC Apesar de útil, a análise anterior não leva em conta a frequência esperada de ocorrências de cada ADE. Para refletirmos melhor quaisquer correlações entre ADEs e drogas, precisamos normalizar as contagens.
-- MAGIC
-- MAGIC Abaixo, reconstruímos o mapa de calor agora com contagens normalizadas

-- COMMAND ----------

WITH 
  e AS (SELECT evento, count(*) AS cnt FROM (SELECT explode(eventos) AS evento FROM summaries) GROUP BY evento HAVING cnt > 2),
  a AS (SELECT droga, evento, count(*) AS cnt FROM (SELECT explode(drogas) AS droga, explode(eventos) AS evento FROM vr_demo.hls_ade.summaries) GROUP BY ALL)
SELECT a.droga, a.evento, a.cnt/e.cnt AS pct FROM a INNER JOIN e ON a.evento = e.evento ORDER BY pct DESC LIMIT 100
