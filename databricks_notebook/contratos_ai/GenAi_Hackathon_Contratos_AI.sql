-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  Contratos AI
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Todas (cross) |
-- MAGIC | Departamento: | Jurídico / Contratos  |
-- MAGIC | Tipo de Solução: | Assistente GenAI / Extrator de Termos  Sumarizador / Classificação de Texto |

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
-- MAGIC Quer se trate de um contrato de NDA (Non-Disclosure Agreement - Contrato de Confidencialidade), ou de um contrato de serviço, quando você está negociando os termos de um acordo, a revisão do contrato costuma ser um processo tedioso e ineficiente, com um nível de risco potencialmente alto. A revisão de contratos baseada em IA permite que as empresas simplifiquem e melhorem processos complexos e auxiliem os advogados na revisão dos termos do contrato em minutos ou horas. 
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Necessidades do Negócio
-- MAGIC
-- MAGIC Algumas aplicações de Gen AI no cilco de gestão de Contratos:
-- MAGIC
-- MAGIC | Caso de Uso | Descrição |
-- MAGIC | -- | -- |
-- MAGIC | Análise automática | Documento é escaneado e suas cláusulas essenciais são destacadas / sumarizadas |
-- MAGIC | Previsão de riscos | Extraindo termos e classificando, prevê problemas potenciais |
-- MAGIC | Análise de coerência | Verifica se tem um fluxo lógico, identifica contradições e ambiguidades |
-- MAGIC | Avaliação de conformidade | Compara textos com diretrizes legais |
-- MAGIC | Identificação de lacunas | Busca cláusulas ausentes |
-- MAGIC | Cláusulas abusivas | Busca cláusulas abusivas |
-- MAGIC | Tabulação de Contratos | Extrai os prinicpais termos (vigência, índices reajustes...) |
-- MAGIC
-- MAGIC </br></br>
-- MAGIC
-- MAGIC Existem várias cláusulas abusivas que podem estar presentes em contratos. Aqui estão alguns exemplos:
-- MAGIC * Cláusulas que excluem ou limitam a responsabilidade do fornecedor por danos causados ao consumidor.
-- MAGIC * Cláusulas que estabelecem a inversão do ônus da prova, colocando o consumidor em desvantagem em um processo judicial.
-- MAGIC * Cláusulas que permitem que o fornecedor modifique o contrato sem autorização do consumidor.
-- MAGIC * Cláusulas que impõem obrigações para outras pessoas além do contratante ou contratado.
-- MAGIC * Cláusulas que restringem direitos do consumidor de maneira desproporcional.
-- MAGIC * Cláusulas que impõem penalidades excessivas em caso de inadimplência.
-- MAGIC * Cláusulas que transferem de forma injusta os riscos e ônus para o consumidor.

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
-- MAGIC * [Base de Contratos](https://huggingface.co/datasets/antonyseabramedeiros/ContratosTI-llama2-1k/viewer/default/train)
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

-- MAGIC %md
-- MAGIC # Base de Dados exemplo

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cluster pra executar o script abaixo:
-- MAGIC
-- MAGIC * Runtime:   DBR 14.3 LTS ML (imagem com LIB's de ML).  ou superior

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC from transformers import pipeline
-- MAGIC from datasets import load_dataset
-- MAGIC
-- MAGIC

-- COMMAND ----------

-- MAGIC %python
-- MAGIC contract_dataset = load_dataset("antonyseabramedeiros/ContratosTI-llama2-1k") 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC contract_dataset = contract_dataset["train"].select(range(40))
-- MAGIC
-- MAGIC display(contract_dataset.to_pandas())
