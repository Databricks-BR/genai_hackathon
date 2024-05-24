![til](/images/head_genai_hackathon.gif)

  

# SQL AI Functions

  

O SQL AI Functions permite você utilizar os seus LLMs como funções no Databricks SQL

  

## Verificando se a feature está habilitada com ai_query() ou ai_gen()

  

Para verificar se o a função ai_query() está funcionando o mais fácil é executar uma query. Crie um SQL Warehouse Serveless ou Pro, e rode o SQL abaixo:

  
```
SELECT ai_query("databricks-dbrx-instruct","tell me a small joke")

SELECT ai_gen("tell me a small joke")
```
  
Caso funcione, você tem o necessário para executar esse caso de uso técnico.

# Regiões de nuvem disponíveis

  

Para essas funçoes funcionarem precisa do Foundation Models disponível. Veja as regiões e disponibilidades desta feature:


[AWS](https://docs.databricks.com/en/machine-learning/foundation-models/supported-models.html)

 [Azure](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/model-serving-limits)

  Google Cloud não possui essa feature.

  

## Alternativa com Model Serving e OpenAI

  
Podemos criar model serving e conectar a um OpenAI ou outro serviço pago de LLMs. Aqui vai um exemplo com a OpenAI. 
  
### OpenAI

Crie uma conta na [OpenAI](https://platform.openai.com/signup) e depois gere uma API key [Aqui](https://platform.openai.com/account/api-keys)

**IMPORTANTE** É crucial que mantenha a sua chave para si mesmo. Se outras pessoas tiverem acesso a essa chave, eles poderão usar essa chave e cobrar da sua conta!

### Model Serving
Para criar um serving é necessário cria um secret e depois configurar uma instância do model serving.

#### Databricks CLI

1. Caso já tenha a Databricks CLI instalada, valide a sua versão. Caso seja menor que **0.205.0**, você precisa desinstalar a versão atual e seguir com os passos seguintes<br>

`databricks -v`<br>

2. Instale a Databricks CLI [[Linux/MacOS](https://docs.databricks.com/en/dev-tools/cli/install.html#curl-install)][[Windows](https://docs.databricks.com/en/dev-tools/cli/install.html#winget-install)]<br>

`curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh`<br>

3. Configure as suas credenciais<br>

`databricks configure`

  

#### Secret

 O endpoint do Model Serving precisa de um secret com o token para se autenticar com o Vector Search (veja a [documentação](https://docs.databricks.com/en/security/secrets/secrets.html)).<br/>

- Crie um secret scope:<br/>

`databricks secrets create-scope <scope>`

- Crie um secret para armazenar o token de autenticação. Use o token criado para seu SP ou, para testes, você pode usar seu [personal access token](https://docs.databricks.com/en/dev-tools/auth/pat.html).<br>

`databricks secrets put-secret <scope> <key>`

#### Configurando Model Serving com External Model do OpenAI

* 1- Serving no Menu Lateral
* 2- Create Serving Endpoint em cima à direita
* 3- Em Name Colocar o nome, por exemplo, "openai-endpoint"
* 4- No Campo Served Entities em Entity, clicar em Select an Entity
* 5- Escolher External Models, provider Open AI e Confirm
* 6- OpenAI API 
  *  OpenAI API type: openAI
  * OpenAI API key secret reference: {{secrets/< scope >/< keys >}}
  * Aperte Create

  Agora teste usando seu Model Serving Name
 ```
SELECT ai_query("openai-endpoint","tell me a small joke")
```

  
  
  
  
  

