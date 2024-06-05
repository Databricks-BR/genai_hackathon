-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif" width="700px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/gabii26/databricks_imgs/main/head_titulo_ok.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Título:  Health Check
-- MAGIC
-- MAGIC | ITEM | DESCRIÇÃO |
-- MAGIC | -- | -- |
-- MAGIC | Indústria: | Saúde 
-- MAGIC | Departamento: | Costumer Service|
-- MAGIC | Tipo de Solução: | SQL AI

-- COMMAND ----------

-- MAGIC %md
-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_grupo.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### GRUPO 10 - Health Check
-- MAGIC
-- MAGIC | # | Nome do Integrante | Empresa | e-mail |
-- MAGIC | -- | -- | -- | -- |
-- MAGIC | 1 | Lucas Oliveira| Grupo Fleury | lucas.oliveira1@grupofleury.com.br |
-- MAGIC | 2 | Vinicius Almeida | Grupo Fleury | vinicius.dalmeida@grupofleury.com.br |
-- MAGIC | 3 | Nicolas Oliveira | Grupo Fleury | nicolas.gomes@grupofleury.com.br |
-- MAGIC | 4 | Augusto Mendes | Grupo Fleury | augusto.couto@grupofleury.com.br |
-- MAGIC | 5 | Gabriela Steil | Grupo Fleury | gabriela.steil@grupofleury.com.br | 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_contexto.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cenário Atual 
-- MAGIC <ins>Com a crescente ocorrência de epidemias, a superlotação dos hospitais e sobrecarga dos colaboradores da área sáude, tornou-se imprescindível criarmos alternativas para agilizar o processo de identificação de enfermidades, disseminação de tratamento acertivo de acordo com cada paciente e informar a unidade de atendimento mais próxima.<ins>
-- MAGIC
-- MAGIC #### Dores / Necessidades do Negócio
-- MAGIC <li> Superlotação de Leitos </li>
-- MAGIC <li> Aumento do tempo de espera </li>
-- MAGIC <li> Falha na predição de epidemias/endemias </li>
-- MAGIC <li> Despadronização na indicação de tratamentos </li>
-- MAGIC <li> Superlotação de Leitos </li>
-- MAGIC <li> Descentralização de informações referente a unidades de atendimento <b>(2.0)</b></li>
-- MAGIC <li> Melhor experiência do usuário <b>(2.0)</b></li>

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_proposito.png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Objetivo da Solução Proposta
-- MAGIC Nosso objetivo é fornecer informações de tratamento, classificar o estado do cliente e com base na classificação indicar a melhor ação para cada caso. <b>(Doenças respiratórias 1.0)</b>
-- MAGIC
-- MAGIC #### Benefícios
-- MAGIC <li>Aplicação dos melhores tratamentos</li>
-- MAGIC <li>Agilidade no atendimento</li>
-- MAGIC <li>Resposta rápidas a endemias/pandemias</li>
-- MAGIC <li>Melhor distribuição dos enfermos por localidade</li>
-- MAGIC <li>Tratamento personalizado <b>(2.0)</b></li>
-- MAGIC
-- MAGIC
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_arquitetura.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Arquitetura
-- MAGIC
-- MAGIC * Cluster 1 / DB Runtime: DBR 14.3 LTS ML (M5D/2 workers)
-- MAGIC * Cluster 2 - Unity / DB Runtime: DBR 14.3 LTS ML (M4.2xlarge /2 workers)
-- MAGIC * Bibliotecas utilizadas: PANDAS, NUMPY,RANDOM e PYSPARK.
-- MAGIC
-- MAGIC ### Técnicas Utilizadas
-- MAGIC
-- MAGIC * SQL com funções GenAI
-- MAGIC * Fontes de Dados: Gerado no playground <b>(LLAMA 3)<b>
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/gabii26/databricks_imgs/main/solucao.png" width="900px">
-- MAGIC <br></br>
-- MAGIC
-- MAGIC import pandas as pd
-- MAGIC import numpy as np
-- MAGIC
-- MAGIC import random
-- MAGIC
-- MAGIC # Lista de medicamentos e fabricantes fictícios
-- MAGIC medicamentos = [
-- MAGIC     {'Nome_Medicamento': 'Paracetamol', 'Fabricante': 'GenericPharma'},
-- MAGIC     {'Nome_Medicamento': 'Dipirona', 'Fabricante': 'Farmaco Inc.'},
-- MAGIC     {'Nome_Medicamento': 'Omeprazol', 'Fabricante': 'PharmaCare'},
-- MAGIC     {'Nome_Medicamento': 'Dexametasona', 'Fabricante': 'MediGen'},
-- MAGIC     {'Nome_Medicamento': 'Ibuprofeno', 'Fabricante': 'PharmaCo'},
-- MAGIC     {'Nome_Medicamento': 'Amoxicilina', 'Fabricante': 'DrugCorp'}
-- MAGIC ]
-- MAGIC
-- MAGIC # Gerando dados fictícios
-- MAGIC num_linhas = 10000
-- MAGIC  
-- MAGIC dados = {
-- MAGIC     'Nome_Medicamento': np.random.choice([med['Nome_Medicamento'] for med in medicamentos], num_linhas),
-- MAGIC     'Nome_Comercial': [f'{med} Comprimido' for med in np.random.choice([med['Nome_Medicamento'] for med in medicamentos], num_linhas)],
-- MAGIC     'Fabricante': [np.random.choice([med['Fabricante'] for med in medicamentos]) for _ in range(num_linhas)],
-- MAGIC     'Quando_Utilizar': ['Conforme orientação médica' for _ in range(num_linhas)],
-- MAGIC     'Frequencia_Uso': [np.random.choice(['Diariamente', 'Semanalmente', 'Quinzenalmente', 'Mensalmente']) for _ in range(num_linhas)],
-- MAGIC     'Quantidade_Por_Idade': [np.random.choice(['1 comprimido', '2 comprimidos', '3 comprimidos']) for _ in range(num_linhas)]
-- MAGIC }
-- MAGIC
-- MAGIC # Criando DataFrame
-- MAGIC df = pd.DataFrame(dados)
-- MAGIC
-- MAGIC # Salvando em um arquivo CSV
-- MAGIC df.to_csv('dados_medicamentos.csv', index=False)
-- MAGIC
-- MAGIC # Criar um dataframe vazio
-- MAGIC df_doencas = pd.DataFrame(columns=['Doença Respiratória', 'Tipo de Medicamento', 'Sintomas', 'Descrição do Remédio', 'Nome_Medicamento'])
-- MAGIC
-- MAGIC # Listas de informações fictícias
-- MAGIC doencas = ['Asma', 'Bronquite', 'Pneumonia', 'Tuberculose', 'Covid-19']
-- MAGIC medicamentos = ['Inalador', 'Antibiótico', 'Anti-inflamatório', 'Vacina', 'Oxigênio']
-- MAGIC sintomas = ['Dificuldade para respirar', 'Tosse seca', 'Febre alta', 'Dor no peito', 'Fadiga']
-- MAGIC descricao_remédios = ['Inalador para controle de asma', 'Antibiótico para infecções bacterianas', 'Anti-inflamatório para reduzir a inflamação', 'Vacina para prevenir doenças', 'Oxigênio para ajudar a respirar']
-- MAGIC nome_remédios = ['Ventolin', 'Amoxicilina', 'Prednisona', 'Vacina contra Covid-19', 'Oxigênio puro']
-- MAGIC
-- MAGIC # Adicionar 100 mil linhas com informações fictícias
-- MAGIC for i in range(100000):
-- MAGIC     doenca = random.choice(doencas)
-- MAGIC     medicamento = random.choice(medicamentos)
-- MAGIC     sintoma = random.choice(sintomas)
-- MAGIC     descricao_remédio = random.choice(descricao_remédios)
-- MAGIC     nome_remédio = random.choice(nome_remédios)
-- MAGIC    
-- MAGIC     df_doencas.loc[i] = [doenca, medicamento, sintoma, descricao_remédio, nome_remédio]
-- MAGIC     
-- MAGIC # Exibir o dataframe
-- MAGIC print(df_doencas.head())
-- MAGIC
-- MAGIC
-- MAGIC # Salvar o dataframe em um arquivo CSV
-- MAGIC df_doencas.to_csv('doencas_respiratorias.csv', index=False)
-- MAGIC
-- MAGIC
-- MAGIC df_doencas_medicamentos = df_doencas.merge(df, on='Nome_Medicamento', how='left')
-- MAGIC
-- MAGIC
-- MAGIC from pyspark.sql import SparkSession
-- MAGIC
-- MAGIC # Criar uma sessão do Spark
-- MAGIC spark = SparkSession.builder.getOrCreate()
-- MAGIC
-- MAGIC # Converter o DataFrame do pandas para um DataFrame do PySpark
-- MAGIC df_spark = spark.createDataFrame(df_doencas_medicamentos)
-- MAGIC
-- MAGIC df_spark.write.saveAsTable("cleaned.fleury_cache.df_doencas_medicamentos")
-- MAGIC
-- MAGIC
-- MAGIC %sql
-- MAGIC SELECT ai_extract(
-- MAGIC     Sintomas,
-- MAGIC     array('Nome_Medicamento', 'Sintomas')
-- MAGIC   ) as Sintomas
-- MAGIC   from cleaned.fleury_cache.df_doencas_medicamentos;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/gabii26/databricks_imgs/main/prototipo.png" width="900px">
-- MAGIC
-- MAGIC <br><br>
-- MAGIC <img src="https://raw.githubusercontent.com/gabii26/databricks_imgs/main/imagem.png" width="900px">
-- MAGIC <br><br>
-- MAGIC <img src="https://raw.githubusercontent.com/gabii26/databricks_imgs/main/imagem%20(1).png" width="900px">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_referencias.png" width="900px">
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Referências:
-- MAGIC * [Databricks AI SQL Functions](https://docs.databricks.com/en/large-language-models/ai-functions.html)
-- MAGIC * [Chat GPT](https://chatgpt.com/?oai-dm=1)
-- MAGIC * [Pixlr](https://pixlr.com/br/express/)
-- MAGIC * [Sql Functions](https://docs.databricks.com/pt/sql/language-manual/sql-ref-functions-builtin.html)
-- MAGIC
