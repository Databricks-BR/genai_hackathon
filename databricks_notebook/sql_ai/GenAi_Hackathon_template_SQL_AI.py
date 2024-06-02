-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  .......   < nome da sua Solução >
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Saúde / Financeira / Varejo / ... |
-- MAGIC | Departamento: | Comercial / Marketing / Jurídico / Contratos / Clínica Médica / ... |
-- MAGIC | Tipo de Solução: | Assistente GenAI / Extrator de Termos / Gerador de Conteúdo / Sumarizador / Classificação de Texto |

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
-- MAGIC descreva ...
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC descreva ...
-- MAGIC </br></br>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Objetivo da Solução Proposta
-- MAGIC
-- MAGIC Descreva como pretente resolver o problema....
-- MAGIC
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC Descreva que benéficios, que melhorias, impactos... a solução trará pra empresa e/ou sociedade ...
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
-- MAGIC * SQL com funções GenAI
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
-- MAGIC * [Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)
-- MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
-- MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
-- MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
-- MAGIC * outros ...
-- MAGIC * outros ...
-- MAGIC * outros ...
-- MAGIC * outros ...

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_sql.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Uma forma de aplicar os modelos de IA Generativa é utilizar as **[Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)**.
-- MAGIC
-- MAGIC Estas permitem a utilização de SQL, uma linguagem amplamente utiliza por analistas de dados e de negócio, para executar uma LLM sobre nossos bancos de dados corporativos. Com isso, também podemos criar novas tabelas com as informações extraídas para serem utilizadas em nossas análises mais facilmente.
-- MAGIC
-- MAGIC Existem funções nativas para executar tarefas pré-definidas ou enviar qualquer instrução desejada para ser executada. Seguem as descrições abaixo:

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC | Gen AI SQL Function | Descrição |
-- MAGIC | -- | -- |
-- MAGIC | [ai_analyze_sentiment](https://docs.databricks.com/pt/sql/language-manual/functions/ai_analyze_sentiment.html) | Análise de Sentimento |
-- MAGIC | [ai_classify](https://docs.databricks.com/pt/sql/language-manual/functions/ai_classify.html) | Classificação de Texto |
-- MAGIC | [ai_extract](https://docs.databricks.com/pt/sql/language-manual/functions/ai_extract.html) | Extração de Termos |
-- MAGIC | [ai_fix_grammar](https://docs.databricks.com/pt/sql/language-manual/functions/ai_fix_grammar.html) | Correção de Gramática |
-- MAGIC | [ai_gen](https://docs.databricks.com/pt/sql/language-manual/functions/ai_gen.html) | Geração de Textos | 
-- MAGIC | [ai_mask](https://docs.databricks.com/pt/sql/language-manual/functions/ai_mask.html) | Marcaramento de dados sensíveis |
-- MAGIC | [ai_query](https://docs.databricks.com/pt/sql/language-manual/functions/ai_query.html) | Consultas Gen Ai |
-- MAGIC | [ai_similarity](https://docs.databricks.com/pt/sql/language-manual/functions/ai_similarity.html) | Análise de Similaridade |
-- MAGIC | [ai_summarize](https://docs.databricks.com/pt/sql/language-manual/functions/ai_summarize.html) | Sumarização de Textos |
-- MAGIC | [ai_translate](https://docs.databricks.com/pt/sql/language-manual/functions/ai_translate.html) | Tradução de Textos |

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC | Model | Task type | Endpoint |
-- MAGIC | --- | --- | --- |
-- MAGIC | **DBRX Instruct** | Chat | databricks-dbrx-instruct |
-- MAGIC | Llama 2 70B Chat | Chat | databricks-llama-2-70b-chat |
-- MAGIC | **Llama 3** 70B Chat | Chat | databricks-meta-llama-3-70b-instruct |
-- MAGIC | Mixtral-8x7B Instruct | Chat | databricks-mixtral-8x7b-instruct |
-- MAGIC | MPT 7B Instruct | Completion | databricks-mpt-7b-instruct |
-- MAGIC | MPT 30B Instruct | Completion | databricks-mpt-30b-instruct |
-- MAGIC | BGE Large (English) | Embedding | databricks-bge-large-en |
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## EXEMPLOS DE IMPLEMENTAÇÃO

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO PARA CRIAR UMA AMOSTRA DE UM PRONTUÁRIO FAKE
SELECT ai_query(
    'databricks-meta-llama-3-70b-instruct',
    'Crie um prontuário médico de um paciente com o nome de JOÃO DA SILVA com sintomas de COVID que está em tratamento há 10 dias, incluindo todos os medicamentos utilizados para minimizar os efeitos inflamatórios de uma crise pulmonar'
  ) AS summary

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO PARA CRIAR UM LAUDO MÉDICO FAKE
SELECT ai_query(
    'databricks-meta-llama-3-70b-instruct',
    'Crie um laudo médico de um paciente chamado José Fulano da Silva, sobre um laudo de um exame de tomografia computadorizada de tórax, com um quadro avançado que configura um câncer de pulmão. Responda em português.'
  ) AS laudo

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO PARA CRIAR UMA LISTA DE CLIENTES FAKE

SELECT ai_query(
    'databricks-meta-llama-3-70b-instruct',
    'Gere um conjunto de dados de amostra de 10 clientes contendo as seguintes colunas: 
      "customer_id" (longo de 1 a 10), "firstname", "lastname" e order_count (número positivo aleatório, menor que 200)

      Dê-me apenas JSON. Nenhum texto fora do JSON. Sem explicações ou notas
      [{"customer_id":<long>, "firstname":<string>, "lastname":<string>, "order_count":<int>}] 
      "array<struct<customer_id:long, firstname:string, lastname:string, order_count:int>>" '
      ) AS sample_data
      

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE TRADUÇÃO
SELECT ai_translate('Hello, how are you?', 'br') as traducao;

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE RESUMO DE UM TEXTO JURIDICO
SELECT ai_summarize(
"""
Faça o resumo em português:

DA PUBLICIDADE: Todas as declarações, anúncios públicos e divulgações deverão ser deverão ser previamente comunicadas pela parte receptora, pelos princípios da boa- fé, transparência contratual. Outrossim, pois necessária a aprovação da outra parte sobre a revelação de contéudos, necessitando o consentimento prévio e expresso.

DAS INFORMAÇÕES CONSIDERADAS CONFIDENCIAIS: As informações confidenciais são aquelas que a parte reveladora não quer que sejam reveladas a terceiros fora do acordo. Assim, deve ser escrito um rol com os dados que serão considerados confidenciais como: metodologias e Ferramentas de desenvolvimento de produtos e serviços, valores e informações financeiras, documentos de marketing e estratégia.

DAS PENALIDADES E DA QUEBRA DA CONFIDENCIALIDADE: deverá ser acordado entre as partes as penalidades em razão da não observância das cláusulas contratuais, como: pagamento de multa, indenização material e/ou moral, e/ou ressarcimento de todas as perdas, danos causados, lucros cessantes, danos diretos e indiretos, direitos autorais entre outros prejuízos patrimoniais ou morais que surjam em decorrência do descumprimento, além de responsabilidade civil e criminal de forma judicial.
""",
    10
  ) as resumo

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE CLASSIFICAÇÃO DE TEXTO JURÍDICO
SELECT ai_classify(
  """
      Em caso de violação de contrato por parte do prestador de serviços, o cliente terá o direito de aplicar uma multa contratual, cujo valor será equivalente a 20% do valor total do contrato, sem prejuízo de outras reivindicações ou ações legais que o cliente possa ter. Essa multa será imediatamente devida e pagável pelo prestador de serviços à data da ocorrência da violação do contrato.
  """
, ARRAY(  "cláusula de rescisão", "cláusula de garantia", "cláusula de multa"))
as avalia_contrato;

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE COMPARAÇÃO DE TEXTOS
-- Faz uma comparação de SIMILARIDADE ENTRE DOIS TEXTOS

-- Por exemplo pra ver se alguma cláusula contratual foi alterada (em um contexto jurídico)

SELECT ai_similarity(
  """
        Em caso de violação de contrato por parte do prestador de serviços, o cliente terá o direito de aplicar uma multa contratual, cujo valor será equivalente a 10% do valor total do contrato, sem prejuízo de outras reivindicações ou ações legais que o cliente possa ter. Essa multa será imediatamente devida e pagável pelo prestador de serviços à data da ocorrência da violação do contrato.

  """,
  """
        Em caso de violação de contrato por parte do prestador de serviços, o cliente terá o direito de aplicar uma multa contratual, cujo valor será equivalente a 20% do valor total do contrato, sem prejuízo de outras reivindicações ou ações legais que o cliente possa ter. Essa multa será imediatamente devida e pagável pelo prestador de serviços à data da ocorrência da violação do contrato.

  """) as similaridade

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE EXTRAÇÃO DE TERMOS

SELECT ai_extract(
    """
        Paciente José da Silva, CPF 023.677.123-11, está com dor no peito há 3 dias.
        Com fadiga intensa e Perda de apetite e no dia 10/03/2024 tomou 20 ml de Novalgina.
        Teve febre, mas apresenta melhoras no dia de hoje.
    """,
    array('nome', 'data', 'cpf', 'medicamento', 'dosagem')
  ) as extracao_de_termos;


-- COMMAND ----------

-- DBTITLE 1,EXEMPLO DE EXTRACAO DE TERMOS
SELECT extracao.nome,
       extracao.data,
       extracao.cpf,
       extracao.medicamento,
       extracao.dosagem
from (
  
  SELECT ai_extract(
    """
        Paciente José da Silva, CPF 023.677.123-11, está com dor no peito há 3 dias.
        Com fadiga intensa e Perda de apetite e no dia 10/03/2024 tomou 20 ml de Novalgina.
        Teve febre, mas apresenta melhoras no dia de hoje.
    """,
    array('nome', 'data', 'cpf', 'medicamento', 'dosagem')
  ) as extracao
)

