-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  Leitura de LAUDOS para Saúde Preventiva
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Saúde  |
-- MAGIC | Departamento: |Clínica Médica  |
-- MAGIC | Tipo de Solução: | Extrator de Termos / Classificação de Texto |

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
-- MAGIC O câncer de pulmão mata cerca de 28 mil brasileiros por ano e lidera a lista dos cânceres mais mortais do planeta. Um dos problemas deste tipo de câncer é que ele é diagnosticado tardiamente, o que diminui as chances de cura. Essa doença provoca o crescimento desordenado das células dos órgãos do sistema respiratório, causando tumorações. Tendo em vista a importância do diagnóstico precoce, a informação pode salvar vidas. Uma vez identificado algum nódulo em um exame de tomografia do Tórax, é necessário que a equipe médica analise o estágio e entenda a sua progressão. 
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC
-- MAGIC Se o paciente não faz o acompanhamento, e entra em um estágio psicológico de negação, o tempo poderá ser crítico para seu tratamento. Se a evolução do quadro progride, por exemplo, para um estágio quatro, que envolve metástase, a cura é difícil. Como a doença costuma ser assintomática na fase inicial, recomenda-se que pessoas do grupo de risco façam exames com regularidade. Esse procedimento é chamado de rastreamento do câncer de pulmão. Essa doença tem uma taxa de sobrevida de 18% para pacientes com cinco anos após o diagnóstico. Mas, segundo dados do INCA, quando diagnosticada rapidamente, a taxa sobe para 56%. Ou seja, quanto mais cedo for identificada, maior é a chance de sucesso do tratamento.
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
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC </br></br>
-- MAGIC Quais as informações relevantes para essa análise ??
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC </br></br>
-- MAGIC Existe alguma forma de identificar / classificar os casos mais críticos??
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC </br></br>
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC
-- MAGIC Descreva que benéficios, que melhorias, impactos... a solução trará pra empresa e/ou sociedade ...  
-- MAGIC .... </br>
-- MAGIC .... </br>
-- MAGIC benefícios para os pacientes??
-- MAGIC .... </br>
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
-- MAGIC * [Caso da empresa COGNOA - Diagnóstico de Autismo](https://www.databricks.com/customers/cognoa)
-- MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
-- MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
-- MAGIC * [Biomedical with LLM - Hot Site](https://www.databricks.com/solutions/accelerators/biomedical-literature-qa-large-language-models-llms)
-- MAGIC * [Getting started with generative AI in healthcare and life sciences - BLOG](https://www.databricks.com/blog/getting-started-generative-ai-healthcare-and-life-sciences)
-- MAGIC * [Clinical Notes Summarization Using Large Language Models - Case com Notebook](https://www.databricks.com/solutions/accelerators/jsl-clinical-notes-summarization-using-llm)
-- MAGIC * [IDC - Generative AI: Revolutionizing
-- MAGIC Healthcare and Life Sciences - Book PDF](https://www.databricks.com/sites/default/files/2023-07/Generative%20AI-%20Revolutionizing%20Healthcare%20and%20Life%20Sciences.pdf)
-- MAGIC * [IA pode ajudar na detecção do Câncer de Mama](https://www.estadao.com.br/saude/ferramenta-de-ia-pode-ajudar-na-deteccao-precoce-do-cancer-de-mama-a-partir-de-exame-de-sangue/)
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
-- MAGIC # EXEMPLOS DE IMPLEMENTAÇÃO

-- COMMAND ----------

-- DBTITLE 1,EXEMPLO PARA CRIAR UM LAUDO MÉDICO FAKE
SELECT ai_query(
    'databricks-meta-llama-3-70b-instruct',
    'Crie um laudo médico de um paciente chamado José Fulano da Silva, sobre um laudo de um exame de tomografia computadorizada de tórax, com um quadro avançado que configura um câncer de pulmão. Responda em português.'
  ) AS laudo

-- COMMAND ----------

insert into tomografia_torax 
SELECT ai_query(
   -- 'databricks-llama-2-70b-chat',
   -- 'databricks-dbrx-instruct',
    'databricks-mixtral-8x7b-instruct',
    'Crie um laudo médico de um paciente chamado José Fulano da Silva, sobre um laudo de um exame de tomografia computadorizada de tórax, com um quadro avançado que configura um câncer de pulmão. Responda em português.'
  ) AS laudo

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


-- COMMAND ----------

SELECT extracao.paciente,
       extracao.medico,
       extracao.data_exame,
       extracao.localizacao,
       extracao.dimensoes
from (
  
  SELECT ai_extract(
"""
Paciente: Carmelinda Fake da Silva
Sexo: Feminino
Médico Solicitante: Dr. Joaquim Fake Salvador
Procedimento(s): TC - Tórax
Nascimento: 06/12/1939 84 anos
Data Exame: 01/12/2023
Plano: Unimed

TOMOGRAFIA DE TORAX S-C

Técnica: Feito estudo do tórax em aparelho multislice evidenciando:

Relatório:
- Áreas hipoatenuantes focais esparsas por ambos os campos pulmonares.
- Granuloma cálcico de 0,5 cm em segmento anterior do lobo superior do pulmão esquerdo.
- Traves fibroatelectasiacas e banda parenquimatosas em lobo inferior do pulmão esquerdo.
- Nódulo com densidade de partes moles, de contornos irregulares, com convergencia de traves para o seu
interior, localizado em segmento posterior do lobo superior do pulmão direito, medindo cerca de 2,6 x2,5 x2,3 cm
em seus maiores eixos.
- Micronódulos parenquimatosos, associado a opacidade com padrão de atenuação em vidro fosco em
segmento apico posterior do lobo superior do pulmão esquerdo.
- Nódulos parenquimatosos de 0,55 cm esparsos por ambos os campos pulmonares.
- Traqueia e brônquios fontes pérvios.
- Mediastino centrado.
- Seios costais e costofrênicos livres.
- Área cardíaca com aumento de suas dimensões.
- Aorta torácica de calibre normal. Placas de calcificações em paredes da aorta e seus ramos.
- Alterações degenerativas da coluna dorsal.
- Aumento do número de linfonodos axilares bilateralmente.

Opinião:
- Áreas hipoatenuantes focais esparsas por ambos os campos pulmonares.
- Granuloma cálcicoem segmento anterior do lobo superior do pulmão esquerdo.
- Traves fibroatelectasiacas em lobo inferior do pulmão esquerdo.
- Nódulo com densidade de partes moles, de contornos irregulares, com convergencia de traves para o seu
interior, localizado em segmento posterior do lobo superior do pulmão direito. ( com discreto aumento de suas
dimensões).
- Micronódulos parenquimatosos, associado a opacidade com padrão de atenuação em vidro fosco em
segmento apico posterior do lobo superior do pulmão esquerdo.
- Nódulos parenquimatosos esparsos por ambos os campos pulmonares.

Achado adicional:
Esteatose hepática.
"""
,
    array('paciente', 'medico', 'data_exame', 'localizacao', 'dimensoes')
  ) as extracao
)


-- COMMAND ----------

-- MAGIC %md
-- MAGIC # UTILIZANDO OUTRA TÉCNICA

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_prompt.png" width="1024px">

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC #Create the few shot learning examples
-- MAGIC from langchain_core.prompts import (
-- MAGIC     ChatPromptTemplate,
-- MAGIC     FewShotChatMessagePromptTemplate,
-- MAGIC )
-- MAGIC examples = [
-- MAGIC   {
-- MAGIC     "input":"Paciente: João da Silva Data: 23/02/2023 Exame: Tomografia Computadorizada de Tórax Resumo: João da Silva, um homem de 45 anos, foi subjeto a uma tomografia computadorizada de tórax para avaliação de sintomas respiratórios. O exame revelou a presença de um nódulo no pulmão esquerdo. Descrição do Nódulo: O nódulo é uma lesão circular, com um diâmetro de aproximadamente 1 cm. Ela está localizada na porção superior do pulmão esquerdo, próxima à borda pleural.",
-- MAGIC
-- MAGIC     "output":
-- MAGIC     """ 
-- MAGIC     {
-- MAGIC       "patient_name": "João da Silva",
-- MAGIC       "patient_age": "45 anos",
-- MAGIC       "exam_date": "23/02/2023",
-- MAGIC       "exam_type": "Tomografia Computadorizada de Tórax",
-- MAGIC       "diagnosis": "O nódulo é uma lesão circular",
-- MAGIC       "nodule_size": "1 cm",
-- MAGIC       "location": "próxima à borda pleural",
-- MAGIC       "nodulo_side": "porção superior do pulmão esquerdo",
-- MAGIC       "nodulo_type": "lesão circular",
-- MAGIC     }
-- MAGIC     """
-- MAGIC   }
-- MAGIC ]
-- MAGIC
-- MAGIC # This is a prompt template used to format each individual example.
-- MAGIC example_prompt = ChatPromptTemplate.from_messages(
-- MAGIC     [
-- MAGIC         ("human", "{input}"),
-- MAGIC         ("ai", "{output}"),
-- MAGIC     ]
-- MAGIC )
-- MAGIC few_shot_prompt = FewShotChatMessagePromptTemplate(
-- MAGIC     example_prompt=example_prompt,
-- MAGIC     examples=examples,
-- MAGIC )
-- MAGIC
-- MAGIC final_prompt = ChatPromptTemplate.from_messages(
-- MAGIC     [
-- MAGIC         ("system", "Extracts keywords that are present in this medical document. Please only output a single JSON code that exactly as the result."),
-- MAGIC         few_shot_prompt,
-- MAGIC         ("human", "{input}"),
-- MAGIC     ]
-- MAGIC )

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_fewshot.png" width="1024px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Few-shot learning
-- MAGIC
-- MAGIC Em tarefas de aprendizagem rápidas (**few-shot learning**), você fornece ao modelo uma instrução (**prompt**), alguns exemplos de resposta de consulta sobre como seguir essa instrução e, em seguida, uma nova consulta. 
-- MAGIC O modelo deve gerar a resposta para essa nova consulta. </br>
-- MAGIC Essa técnica tem prós e contras: é muito poderosa e permite que os modelos sejam reutilizados para muitas outras aplicações, mas pode ser complicada e exigir muita engenharia imediata para obter resultados bons e confiáveis.
-- MAGIC
-- MAGIC **Referências**: 
-- MAGIC * [Wikipedia page on few-shot learning](https://en.wikipedia.org/wiki/Few-shot_learning_&#40;natural_language_processing&#41;)
-- MAGIC * [this Hugging Face blog about few-shot learning](https://huggingface.co/blog/few-shot-learning-gpt-neo-and-inference-api).
-- MAGIC
-- MAGIC
-- MAGIC

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from langchain import PromptTemplate
-- MAGIC from langchain.chains.llm import LLMChain
-- MAGIC from langchain.chat_models import ChatDatabricks
-- MAGIC
-- MAGIC #chat_model = ChatDatabricks(endpoint="databricks-llama-2-70b-chat", max_tokens = 200)
-- MAGIC dbrx_model = ChatDatabricks(endpoint="databricks-dbrx-instruct", max_tokens = 800)

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC # Initialize the ChatDatabricks model with endpoint and token settings
-- MAGIC chat_model = ChatDatabricks(endpoint="databricks-dbrx-instruct", max_tokens=800)
-- MAGIC
-- MAGIC # Initialize the chat model with the prompt template
-- MAGIC chain = LLMChain(
-- MAGIC     llm=chat_model,
-- MAGIC     prompt=final_prompt
-- MAGIC )

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Faz a validação do Modelo

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #example 1
-- MAGIC resultado_genai = chain.predict(input="Francisco da Silva foi diagnosticado com a presença de um nódulo no lado esquerdo do pulmão de tamanho aproximado de 2 cm")
-- MAGIC
-- MAGIC displayHTML('<pre>' + resultado_genai + '</pre>')

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #example 2 - Utilizando um Laudo Real (impersonalizado / FAKE)
-- MAGIC
-- MAGIC resultado_genai = chain.predict(input=
-- MAGIC """
-- MAGIC Paciente: Carmelinda Fake da Silva
-- MAGIC Sexo: Feminino
-- MAGIC Médico Solicitante: Dr. Joaquim Fake Salvador
-- MAGIC Procedimento(s): TC - Tórax
-- MAGIC Nascimento: 06/12/1939 84 anos
-- MAGIC Data Exame: 01/12/2023
-- MAGIC Plano: Unimed
-- MAGIC
-- MAGIC TOMOGRAFIA DE TORAX S-C
-- MAGIC
-- MAGIC Técnica: Feito estudo do tórax em aparelho multislice evidenciando:
-- MAGIC
-- MAGIC Relatório:
-- MAGIC - Áreas hipoatenuantes focais esparsas por ambos os campos pulmonares.
-- MAGIC - Granuloma cálcico de 0,5 cm em segmento anterior do lobo superior do pulmão esquerdo.
-- MAGIC - Traves fibroatelectasiacas e banda parenquimatosas em lobo inferior do pulmão esquerdo.
-- MAGIC - Nódulo com densidade de partes moles, de contornos irregulares, com convergencia de traves para o seu
-- MAGIC interior, localizado em segmento posterior do lobo superior do pulmão direito, medindo cerca de 2,6 x2,5 x2,3 cm
-- MAGIC em seus maiores eixos.
-- MAGIC - Micronódulos parenquimatosos, associado a opacidade com padrão de atenuação em vidro fosco em
-- MAGIC segmento apico posterior do lobo superior do pulmão esquerdo.
-- MAGIC - Nódulos parenquimatosos de 0,55 cm esparsos por ambos os campos pulmonares.
-- MAGIC - Traqueia e brônquios fontes pérvios.
-- MAGIC - Mediastino centrado.
-- MAGIC - Seios costais e costofrênicos livres.
-- MAGIC - Área cardíaca com aumento de suas dimensões.
-- MAGIC - Aorta torácica de calibre normal. Placas de calcificações em paredes da aorta e seus ramos.
-- MAGIC - Alterações degenerativas da coluna dorsal.
-- MAGIC - Aumento do número de linfonodos axilares bilateralmente.
-- MAGIC
-- MAGIC Opinião:
-- MAGIC - Áreas hipoatenuantes focais esparsas por ambos os campos pulmonares.
-- MAGIC - Granuloma cálcicoem segmento anterior do lobo superior do pulmão esquerdo.
-- MAGIC - Traves fibroatelectasiacas em lobo inferior do pulmão esquerdo.
-- MAGIC - Nódulo com densidade de partes moles, de contornos irregulares, com convergencia de traves para o seu
-- MAGIC interior, localizado em segmento posterior do lobo superior do pulmão direito. ( com discreto aumento de suas
-- MAGIC dimensões).
-- MAGIC - Micronódulos parenquimatosos, associado a opacidade com padrão de atenuação em vidro fosco em
-- MAGIC segmento apico posterior do lobo superior do pulmão esquerdo.
-- MAGIC - Nódulos parenquimatosos esparsos por ambos os campos pulmonares.
-- MAGIC
-- MAGIC Achado adicional:
-- MAGIC Esteatose hepática.
-- MAGIC """
-- MAGIC )
-- MAGIC
-- MAGIC displayHTML('<pre>' + resultado_genai + '</pre>')
