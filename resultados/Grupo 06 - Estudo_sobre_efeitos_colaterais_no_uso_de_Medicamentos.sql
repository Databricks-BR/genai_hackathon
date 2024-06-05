-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  Identificação Eventos Adversos
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Saúde  |
-- MAGIC | Departamento: | Clínica Médica / Farmacêutica |
-- MAGIC | Tipo de Solução: | Assistente GenAI / Extrator de Termos |

-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GRUPO 06 - Estudo sobre efeitos colaterais no uso de Medicamentos
-- MAGIC
-- MAGIC | # | Nome do Integrante | Empresa | e-mail |
-- MAGIC | -- | -- | -- | -- |
-- MAGIC | 1 | Francisco Souza | Embracon | francisco.almir@embracon.com.br |
-- MAGIC | 2 | Felipe Santos | Embracon | felipe.sheison@embracon.com.br |
-- MAGIC | 3 | Diogo Mascarenhas | Embracon | diogo.mascarenhas@embracon.com.br |
-- MAGIC | 4 | Jose Pena | Epharma | jose.pena@epharma.com.br |
-- MAGIC | 5 | Marcio Dias Passos | Epharma | marcio.passos@epharma.com.br | 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cenário Atual
-- MAGIC
-- MAGIC Os eventos adversos a medicamentos (EAM) - **adverse drug events (ADEs)** - representam um problema clínico significativo na área da saúde, devido à crescente multimorbidade e complexidade do tratamento médico. Portanto, melhorar a segurança dos medicamentos foi definido como um desafio global para a segurança do paciente, com o objetivo de reduzir o nível de danos graves e evitáveis ​​relacionados aos medicamentos.
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC A fim de melhorar a segurança da medicação em pacientes hospitalizados, os hospitais precisam ter uma visão precisa e contínua sobre que tipo de EAM ocorre em seus pacientes internados, incluindo quais subpopulações apresentam alto risco de EAM. Essas informações são cruciais para obter uma melhor compreensão dos medicamentos, dos pacientes e dos processos clínicos que são mais passíveis de intervenções de segurança de medicamentos e em quais deles concentrar seus esforços.
-- MAGIC </br></br>
-- MAGIC Uma das principais barreiras para obter tal conhecimento é a falta de um sistema de monitoramento que possa detectar EAM de forma rotineira, rápida e em escala em pacientes hospitalizados. 
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
-- MAGIC Identificar quais as drogas que mais causam efeitos colaterais, identificar quais os efeitos colaterais mais comuns e relacionar quais drogras mais afetam os pacientes  
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC - Melhor entendimento dos efeitos colaterais associados ao uso de uma droga a partir do aumento da facilidade e eficiência na produção de estudos sobre o tema
-- MAGIC - Melhor segurança para os pacientes em receber o medicamento e dosagem correta
-- MAGIC - Melhorar a confiança dos pacientes na adesão dos tratamentos

-- COMMAND ----------

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
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Arquitetura
-- MAGIC
-- MAGIC * Provedor Cloud:   Azure
-- MAGIC * Cluster / DB Runtime:   DBR 14.3 LTS Spark 3.5.0 Standard_DS3_v2 14GB 4 Cores
-- MAGIC
-- MAGIC ### Técnicas Utilizadas
-- MAGIC
-- MAGIC Dados - Utilizou-se uma base de dados com 20k registros de relatórios médicos, onde consta-se ou não a presença de efeitos colaterais associados ao uso dos medicamentos.
-- MAGIC
-- MAGIC Estruturação dos dados - API Meta LLaMa 3 - A escolha do LLM a ser utilizado nessa etapa foi feita com base na acurácia na detecção de efeitos colaterais nos relatórios médicos constantes na base de dados
-- MAGIC
-- MAGIC Análise exploratória - com base nos dados estruturados foi feita uma análise exploratória visando entender quais drogas causam mais efeitos colaterias, quais os efeitos colaterais mais comuns e a relação droga x efeito colateral.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Referências:
-- MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
-- MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)

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

-- MAGIC %md-sandbox
-- MAGIC **<font color="red">ANTES DE CONTINUAR, SIGA AS INSTRUÇÕES ABAIXO.</font>**
-- MAGIC
-- MAGIC ## Configure o acesso ao dataset
-- MAGIC
-- MAGIC 1. Peça a um dos intrutores para liberar o acesso ao dataset
-- MAGIC 1. Acesse `Catalog` no menu principal à esquerda
-- MAGIC 1. Acesse `Delta Sharing` > `Shared with me`
-- MAGIC 1. Procure por `databricks-field-eng`
-- MAGIC 1. Ao lado de `br-genai-hackathon`, clique em `Create catalog`
-- MAGIC 1. Digite o nome `br-genai-hackathon` e clique em `Create`
-- MAGIC
-- MAGIC <img src="https://github.com/Databricks-BR/genai_hackathon/blob/main/images/sharing.gif?raw=true">

-- COMMAND ----------

-- MAGIC %md E depois solicitamos uma amostra do nosso conjunto de dados

-- COMMAND ----------

SELECT * FROM `br-genai-hackathon`.eventos_adversos.clinical_notes_pt LIMIT 100

-- COMMAND ----------

-- MAGIC %md Também podemos analisar a distribuição entre conversas com e sem ADEs

-- COMMAND ----------

select is_ADE, count(*) as from `br-genai-hackathon`.eventos_adversos.clinical_notes_pt group by is_ADE

-- COMMAND ----------

-- MAGIC %md ## Principais Conceitos

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_foundation.png" width="900px">

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

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_sql.png" width="900px">
-- MAGIC

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

SELECT FROM_JSON(
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
                Nota clíncia: ', '''
  CONCLUSÃO: A administração de ativador tissular do plasminogênio foi responsável pela grande extensão da hemorragia e deve ser considerada no diagnóstico diferencial de descolamento hemorrágico coroideano.
''' 
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS summary

-- COMMAND ----------

-- MAGIC %md ### Extrai todas as informações
-- MAGIC
-- MAGIC De forma similar, vamos aplicar nosso modelo de forma massiva em todo o nosso conjunto de dados.

-- COMMAND ----------

-- MAGIC %md Uma amostra da base final utilizando a API Meta LLaMa 3

-- COMMAND ----------

--CREATE OR REPLACE TABLE summaries AS
SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt limit 10) 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Com base na matrix de confusão is_ADE x presenca_evento, escolheu-se a API do LLaMa 3 em detrimento das outras.

-- COMMAND ----------


with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt limit 100) )

SELECT is_ADE, presenca_evento, count(*) FROM aux WHERE presenca_evento IS NOT NULL GROUP BY ALL

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
        AI_QUERY(
            'databricks-dbrx-instruct',
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt limit 100) )

SELECT is_ADE, presenca_evento, count(*) FROM aux WHERE presenca_evento IS NOT NULL GROUP BY ALL

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
        AI_QUERY(
            'databricks-mixtral-8x7b-instruct',
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt limit 100) )

SELECT is_ADE, presenca_evento, count(*) FROM aux WHERE presenca_evento IS NOT NULL GROUP BY ALL

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

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt -- order by rand() 
      limit 100) )

SELECT droga, count(*) AS cnt FROM (SELECT explode(drogas) AS droga FROM aux)
GROUP BY droga ORDER BY cnt DESC LIMIT 10

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt -- order by rand() 
      limit 500) )

SELECT droga, count(*) AS cnt FROM (SELECT explode(drogas) AS droga FROM aux)
GROUP BY droga ORDER BY cnt DESC LIMIT 10

-- COMMAND ----------

select * from eph_lakehouse_dev.default.clinical_notes_pt
order by rand() limit 

-- COMMAND ----------

-- MAGIC %md #### Eventos mais comuns

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt  --order by rand() 
      limit 100) )


SELECT evento, count(*) AS cnt FROM (SELECT explode(eventos) AS evento FROM aux)
GROUP BY evento ORDER BY cnt DESC LIMIT 10

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt -- order by rand() 
      limit 500) )

SELECT evento, count(*) AS cnt FROM (SELECT explode(eventos) AS evento FROM aux)
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

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt  --order by rand() 
      limit 100) )


SELECT droga, evento, count(*) AS cnt FROM (SELECT explode(drogas) AS droga, explode(eventos) AS evento FROM aux)
GROUP BY ALL ORDER BY cnt DESC LIMIT 100

-- COMMAND ----------

with aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt -- order by rand() 
      limit 500) )

SELECT droga, evento, count(*) AS cnt FROM (SELECT explode(drogas) AS droga, explode(eventos) AS evento FROM aux)
GROUP BY ALL ORDER BY cnt DESC LIMIT 100

-- COMMAND ----------

-- MAGIC %md #### Droga x Evento Normalizado
-- MAGIC
-- MAGIC Apesar de útil, a análise anterior não leva em conta a frequência esperada de ocorrências de cada ADE. Para refletirmos melhor quaisquer correlações entre ADEs e drogas, precisamos normalizar as contagens.
-- MAGIC
-- MAGIC Abaixo, reconstruímos o mapa de calor agora com contagens normalizadas

-- COMMAND ----------

WITH 
 aux as (SELECT id, text, is_ADE, s.* FROM (
  SELECT *, FROM_JSON(
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
                Nota clíncia: ', text
            )
        ),
        "STRUCT<presenca_evento: STRING, eventos: ARRAY<STRING>, drogas: ARRAY<STRING>>"
    ) AS s FROM eph_lakehouse_dev.default.clinical_notes_pt  order by rand() limit 500) ),

  e AS (SELECT evento, count(*) AS cnt FROM (SELECT explode(eventos) AS evento FROM summaries) GROUP BY evento HAVING cnt > 2),
  a AS (SELECT droga, evento, count(*) AS cnt FROM (SELECT explode(drogas) AS droga, explode(eventos) AS evento FROM summaries) GROUP BY ALL)
SELECT a.droga, a.evento, a.cnt/e.cnt AS pct FROM a INNER JOIN e ON a.evento = e.evento ORDER BY pct DESC LIMIT 100
