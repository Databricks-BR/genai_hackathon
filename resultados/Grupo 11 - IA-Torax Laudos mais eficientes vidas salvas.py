# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_titulo.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC ## Título:  Leitura de LAUDOS para Saúde Preventiva
# MAGIC
# MAGIC | ITEM | DESCRIÇÃO |
# MAGIC | -- | -- |
# MAGIC | Indústria: | Saúde  |
# MAGIC | Departamento: |Clínica Médica  |
# MAGIC | Tipo de Solução: | Assistente para estruturação de laudos médicos |

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### GRUPO 11 - IA-Tórax: Laudos Mais Eficientes, Vidas Salvas
# MAGIC
# MAGIC | # | Nome do Integrante | Empresa | e-mail |
# MAGIC | -- | -- | -- | -- |
# MAGIC | 1 | Ricardo Camilo | Fleury/dti | ricardo.camilo@dtidigital.com.br |
# MAGIC | 2 | Ramon Finelli | Fleury/dti | ramon.finelli@dtidigital.com.br |
# MAGIC | 3 | Andre Oliveira | Fleury | andre.oliva@grupofleury.com.br|
# MAGIC | 4 | Davis Bispo | Fleury | davis.bispo@grupofleury.com.br |
# MAGIC | 5 | Yuri Lopes | Fleury | yuri.lopes@grupofleury.com.br |
# MAGIC | 6 | Gustavo Nascimento | Fleury | gustavo.lnascimento@grupofleury.com.br |
# MAGIC | 7 | Andrea Mourão | FQM | amourao@fqm.com.br | 

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Cenário Atual
# MAGIC
# MAGIC O laudo médico em exames de imagem é crucial para o diagnóstico preciso e planejamento de tratamento de doenças graves. Ele permite monitorar a progressão da doença, facilita a comunicação entre profissionais de saúde e serve como registro médico do paciente. Além disso, pode ter relevância legal em certos casos. Entretanto há uma incidência significativa de erros em laudos médicos, os estudos abaixo mostram a taxa de erros em exames de tórax:
# MAGIC
# MAGIC - Um estudo publicado na revista Radiology em 2017 analisou mais de **100.000** laudos de radiografia de tórax e encontrou uma taxa de erro geral de **4,7%**. O estudo também descobriu que os erros mais comuns eram a falha em detectar anormalidades (falsos negativos) e a interpretação incorreta de anormalidades (falsos positivos).
# MAGIC - Uma meta-análise publicada na revista The BMJ em 2015 analisou 22 estudos sobre a taxa de erros em laudos de TC de tórax e encontrou uma taxa média de **3,5%**. O estudo também descobriu que a taxa de erros era maior para pacientes com pneumonia e trauma.
# MAGIC - Um estudo publicado na revista JACR em 2019 analisou mais de **50.000** laudos de RM de tórax e encontrou uma taxa de erro geral de **2,1%**. O estudo também descobriu que os erros mais comuns eram a falha em detectar anormalidades (falsos negativos) e a interpretação incorreta de anormalidades (falsos positivos).
# MAGIC
# MAGIC É importante notar que esses estudos apenas fornecem estimativas da taxa de erros em laudos médicos de exames de tórax. A taxa real de erro pode ser maior ou menor em um caso individual.
# MAGIC
# MAGIC As causas que levam a erros em laudos médicos:
# MAGIC
# MAGIC - **Experiência e qualificação do radiologista:** Radiologistas com mais experiência e treinamento especializado em radiologia torácica tendem a ter taxas de erro mais baixas.
# MAGIC - **Qualidade do exame:** A qualidade da imagem do raio-X pode afetar a capacidade do radiologista de identificar com precisão as anormalidades.
# MAGIC - **Complexidade do caso:** Casos mais complexos, com imagens sutis ou múltiplas anormalidades, podem ter taxas de erro mais altas.
# MAGIC - **Tipo de exame:** Diferentes tipos de exames de tórax, como radiografia simples, tomografia computadorizada (TC) e ressonância magnética (RM), podem ter taxas de erro variáveis.
# MAGIC - **Fadiga:** Radiologistas que estão cansados ou com excesso de trabalho podem ser mais propensos a cometer erros.
# MAGIC - **Distrações:** Distrações no ambiente de trabalho, como telefones celulares ou conversas, podem levar a erros.
# MAGIC - **Falta de comunicação:** A falta de comunicação entre o radiologista e o médico solicitante pode levar a erros na interpretação do exame.
# MAGIC - **Prejuízos cognitivos:** Prejuízos cognitivos, como vieses e heurísticas, podem levar a erros no julgamento do radiologista.
# MAGIC
# MAGIC #### Dores / Necessidades do Negócio
# MAGIC
# MAGIC Padronizar e gerar insights a partir de laudos médicos enfrenta desafios como variação na terminologia, qualidade dos dados, interpretação subjetiva, falta de estrutura nos laudos, questões de privacidade e segurança, integração de sistemas diferentes, necessidade de treinamento para adoção de novos padrões e a complexidade inerente a algumas doenças.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Objetivo da Solução Proposta
# MAGIC
# MAGIC A solução visa utilizar LLM para criação de um template eficiente onde o corpo clínico possa preencher as informações diagnosticadas nas imagens, assim como a criação de um assistente que auxilia na correção de eventuais falhas na redação do documento médico. 
# MAGIC
# MAGIC #### Benefícios
# MAGIC
# MAGIC Benefícios para o corpo clínico:
# MAGIC
# MAGIC - **Maior eficiência e produtividade:** Automação de tarefas repetitivas, otimizando o tempo e liberando o corpo clínico para atividades mais complexas.
# MAGIC - **Laudos mais precisos e padronizados:** Templates e correção gramatical garantem clareza, confiabilidade e padronização na linguagem.
# MAGIC - **Redução do estresse e da exaustão:** Otimização do fluxo de trabalho contribui para um ambiente de trabalho mais saudável.
# MAGIC
# MAGIC Benefícios para os pacientes:
# MAGIC
# MAGIC - **Diagnósticos mais rápidos e precisos:** Agilidade na entrega dos laudos permite o início do tratamento adequado de forma célere.
# MAGIC - **Maior segurança do paciente:** Redução da taxa de erros nos laudos minimiza riscos de eventos adversos.
# MAGIC - **Atendimento mais humanizado:** Otimização do tempo do corpo clínico permite um atendimento mais personalizado.
# MAGIC
# MAGIC Impacto social:
# MAGIC
# MAGIC - **Acesso à saúde de qualidade:** Democratização do acesso a diagnósticos precisos e rápidos.
# MAGIC - **Redução dos custos com saúde:** Otimização do fluxo de trabalho e redução de erros nos laudos diminuem custos.
# MAGIC - **Melhoria da saúde da população:** Diagnósticos precisos e tratamento rápido contribuem para a saúde da população.
# MAGIC - **Avanço da pesquisa médica:** Análise histórica e acompanhamento personalizado dos exames permitem pesquisas mais aprofundadas.
# MAGIC
# MAGIC A solução LLM para geração de laudos médicos promove um futuro mais saudável e equitativo, com diagnósticos precisos, rápidos e personalizados para todos.

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Arquitetura
# MAGIC
# MAGIC * Provedor Cloud:  AWS
# MAGIC * Cluster / DB Runtime:   DBR 14.3 / Serverless SQL warehouse
# MAGIC * Bibliotecas utilizadas: Llama index
# MAGIC
# MAGIC ### Técnicas Utilizadas
# MAGIC
# MAGIC * SQL com funções GenAI
# MAGIC * LLM Foundation:   GPT4o
# MAGIC * Fontes de Dados:  Base de laudos proprietária

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Referências:
# MAGIC * [Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)
# MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
# MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
# MAGIC * [Foundation LLM Models APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html#pay-per-token-foundation-model-apis)
# MAGIC * [Caso da empresa COGNOA - Diagnóstico de Autismo](https://www.databricks.com/customers/cognoa)
# MAGIC * [Introdução ao DBRX LLM foundation model Databricks](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
# MAGIC * [Documentação do Gen AI Databricks](https://docs.databricks.com/en/generative-ai/generative-ai.html)
# MAGIC * [Biomedical with LLM - Hot Site](https://www.databricks.com/solutions/accelerators/biomedical-literature-qa-large-language-models-llms)
# MAGIC * [Getting started with generative AI in healthcare and life sciences - BLOG](https://www.databricks.com/blog/getting-started-generative-ai-healthcare-and-life-sciences)
# MAGIC * [Clinical Notes Summarization Using Large Language Models - Case com Notebook](https://www.databricks.com/solutions/accelerators/jsl-clinical-notes-summarization-using-llm)
# MAGIC * [IDC - Generative AI: Revolutionizing
# MAGIC Healthcare and Life Sciences - Book PDF](https://www.databricks.com/sites/default/files/2023-07/Generative%20AI-%20Revolutionizing%20Healthcare%20and%20Life%20Sciences.pdf)
# MAGIC * [IA pode ajudar na detecção do Câncer de Mama](https://www.estadao.com.br/saude/ferramenta-de-ia-pode-ajudar-na-deteccao-precoce-do-cancer-de-mama-a-partir-de-exame-de-sangue/)
# MAGIC * Giles RL, Lambert J, Longmore M, et al. Diagnostic Error in Chest Radiography: A Systematic Review of the Literature. Radiology. 2017; 284(3): 780-794.
# MAGIC * van der Schaaf EM, Leeflang JC, Hollander M, et al. Diagnostic accuracy of chest CT for non-traumatic acute chest pain: a meta-analysis. BMJ. 2015; 351: h3086.
# MAGIC * Proietti M, Merlo A, Bartolomeo F, et al. Diagnostic accuracy of magnetic resonance imaging for suspected pulmonary embolism: A meta-analysis of 51 studies. Journal of the American College of Radiology.
# MAGIC 2019; 16(12): 1804-1812.

# COMMAND ----------

# MAGIC %md
# MAGIC Obter uma amostra dos dados para testar o fluxo

# COMMAND ----------

df = spark.read.table("cleaned.pardini_cache.laudos").toPandas()[['laudo']]
#df.head(20)

# COMMAND ----------

# MAGIC %md
# MAGIC Salvar como CSV para usar com as funções SQL + Gen AI

# COMMAND ----------

df.sample(200).to_csv('laudos.csv', index=False)

# COMMAND ----------

# MAGIC %md
# MAGIC RAG com llama index

# COMMAND ----------

# MAGIC %pip install llama_index
# MAGIC %pip install jiwer typing-extensions
# MAGIC %pip install --upgrade typing-extensions
# MAGIC
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

Settings.llm = OpenAI(temperature=0.2, model="gpt-4o", api_key='')

# COMMAND ----------

from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader(input_dir="data")
documents = reader.load_data()

# COMMAND ----------

import os
from llama_index.core import VectorStoreIndex

os.environ['OPENAI_API_KEY'] = ''
vector_index = VectorStoreIndex.from_documents(documents)
vector_index.as_query_engine()

# COMMAND ----------

# MAGIC %md
# MAGIC A partir dos laudos existentes, propor um template padrão, com opções padrões, para facilitar e padronizar o preenchimento de laudos

# COMMAND ----------

query_engine = vector_index.as_query_engine()
response = query_engine.query(
    "Crie um template completo para um laudo de torax, que será usado por todos os médicos do grupo. Não preencha os campos, deixe somente os tópicos e opções de preenchimento. não coloque dados do paciente no laudo"
)
print(response)

# COMMAND ----------

# MAGIC %md
# MAGIC RELATÓRIO DE TOMOGRAFIA COMPUTADORIZADA DO TÓRAX
# MAGIC
# MAGIC INDICAÇÃO CLÍNICA:
# MAGIC [Descrever a indicação clínica]
# MAGIC
# MAGIC ASPECTOS TÉCNICOS:
# MAGIC [Descrever a técnica utilizada, incluindo tipo de tomógrafo, uso de contraste, etc.]
# MAGIC
# MAGIC ASPECTOS OBSERVADOS:
# MAGIC - Parênquima pulmonar: [Descrever densidade tomográfica, presença de consolidações, massas, nódulos, etc.]
# MAGIC - Derrames pleurais: [Presença ou ausência]
# MAGIC - Coração: [Configuração, densidade tomográfica, sinais de aumento, etc.]
# MAGIC - Saco pericárdico: [Presença de líquido, espessamento, etc.]
# MAGIC - Vasos da base: [Anatômicos, curso e calibre normais, etc.]
# MAGIC - Aorta: [Trajeto e calibres normais, etc.]
# MAGIC - Linfonodomegalia mediastinal: [Presença ou ausência]
# MAGIC - Traqueia e brônquios principais: [Pérvios, dimensões e paredes normais, etc.]
# MAGIC - Arcabouço torácico: [Preservado, alterações ósseas, etc.]
# MAGIC - Superfícies e cavidades pleurais: [Espessamento, calcificações, derrame, pneumotórax, etc.]
# MAGIC - Partes moles e arcabouço ósseo da parede torácica: [Aspecto usual, alterações, etc.]
# MAGIC
# MAGIC IMPRESSÃO:
# MAGIC [Descrever as conclusões principais do exame, incluindo achados significativos e sua interpretação]
# MAGIC
# MAGIC Atenciosamente,
# MAGIC [Nome do Médico]
# MAGIC [CRM]
# MAGIC [Data do Laudo]

# COMMAND ----------

query_engine = vector_index.as_query_engine()
response = query_engine.query(
    "crie uma proposta de tabela que irá estruturar os laudos. Essa tabela deve conter variáveis com valor 0 ou 1, indicando se determinado laudo possui ou não determinada informação."
)
print(response)

# COMMAND ----------

# MAGIC %md
# MAGIC A partir da query abaixo, obter o resultado e usar com Genie Spaces

# COMMAND ----------

# MAGIC %sql
# MAGIC select
# MAGIC laudo,
# MAGIC   CASE WHEN a LIKE 'Não' THEN 1 ELSE 0 END AS Formacoes_Cisticas_na_Pelve,
# MAGIC   CASE WHEN b LIKE 'Não' THEN 1 ELSE 0 END AS Espondilose_Incipiente,
# MAGIC   CASE WHEN c LIKE 'Não' THEN 1 ELSE 0 END AS Lesao_Ovalada_no_Pulmao_Direito,
# MAGIC   CASE WHEN d LIKE 'Não' THEN 1 ELSE 0 END AS Lesao_Alongada_no_Pulmao_Direito,
# MAGIC   CASE WHEN e LIKE 'Não' THEN 1 ELSE 0 END AS Formacao_Nodular_no_Pulmao,
# MAGIC   CASE WHEN f LIKE 'Não' THEN 1 ELSE 0 END AS Consolidacoes_Pulmonares,
# MAGIC   CASE WHEN g LIKE 'Não' THEN 1 ELSE 0 END AS Derrame_Pericardico,
# MAGIC   CASE WHEN h LIKE 'Não' THEN 1 ELSE 0 END AS Derrame_Pleural,
# MAGIC   CASE WHEN i LIKE 'Não' THEN 1 ELSE 0 END AS Pneumotorax,
# MAGIC   CASE WHEN j LIKE 'Não' THEN 1 ELSE 0 END AS Calculos_Renais,
# MAGIC   CASE WHEN k LIKE 'Não' THEN 1 ELSE 0 END AS Bacos_Acessorios,
# MAGIC   CASE WHEN l LIKE 'Não' THEN 1 ELSE 0 END AS Recomendacao_de_novos_exames,
# MAGIC   CASE WHEN m LIKE 'Não' THEN 1 ELSE 0 END AS Utilizacao_Contraste
# MAGIC   from (
# MAGIC     select
# MAGIC     laudo,
# MAGIC     ai_classify(laudo, ARRAY("Contém Formações Císticas na Pelve", "Não contém Formações Císticas na Pelve")) as a,
# MAGIC     ai_classify(laudo, ARRAY("Contém Espondilose Incipiente", "Não contém Espondilose Incipiente")) as b,
# MAGIC     ai_classify(laudo, ARRAY("Contém Lesão Ovalada no Pulmão Direito", "Não contém Lesão Ovalada no Pulmão Direito")) as c,
# MAGIC     ai_classify(laudo, ARRAY("Contém Lesão Alongada no Pulmão Direito", "Não contém Lesão Alongada no Pulmão Direito")) as d,
# MAGIC     ai_classify(laudo, ARRAY("Contém Formação Nodular no Pulmão", "Não contém Formação Nodular no Pulmão")) as e,
# MAGIC     ai_classify(laudo, ARRAY("Contém Consolidações Pulmonares", "Não contém Consolidações Pulmonares")) as f,
# MAGIC     ai_classify(laudo, ARRAY("Contém Derrame Pericárdico", "Não contém Derrame Pericárdico")) as g,
# MAGIC     ai_classify(laudo, ARRAY("Contém Derrame Pleural", "Não contém Derrame Pleural")) as h,
# MAGIC     ai_classify(laudo, ARRAY("Contém Pneumotórax", "Não contém Pneumotórax")) as i,
# MAGIC     ai_classify(laudo, ARRAY("Contém Cálculos Renais", "Não contém Cálculos Renais")) as j,
# MAGIC     ai_classify(laudo, ARRAY("Contém Baços Acessórios", "Não contém Baços Acessórios")) as k,
# MAGIC     ai_classify(laudo, ARRAY("Contém recomendação de novos exames", "Não contém recomendação de novos exames")) as l,
# MAGIC     ai_classify(laudo, ARRAY("Contém uso de contraste", "Não contém uso de contraste")) as m
# MAGIC    from cleaned.pardini_cache.laudos
# MAGIC   )
# MAGIC   limit 20

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/imagem1.jpeg" width="700px">

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/imagem2.jpeg" width="700px">
