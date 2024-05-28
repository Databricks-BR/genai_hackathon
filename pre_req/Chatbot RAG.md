![Databricks GenAI Hackathon](https://raw.githubusercontent.com/Databricks-BR/genai_hackathon/main/images/head_genai_hackathon.gif)<br><br>

# Chatbot com RAG

Nesse caso de uso utilizaremos os seguintes componentes do Lakehouse AI:
- Model Serving
- Vector Search

Verifique a disponibilidade desses serviços na sua nuvem/região:
- [AWS](https://docs.databricks.com/en/resources/supported-regions.html#supported-regions-list)
- [Azure](https://learn.microsoft.com/en-us/azure/databricks/resources/supported-regions#--supported-regions-list)
- [GCP](https://docs.gcp.databricks.com/en/resources/supported-regions.html?_ga=2.13522932.235452560.1716231820-700395039.1708095273#supported-regions-list)

# Serverless compute

O Model Serving e o Vector Search utilizam serverless compute. No entanto, este tipo de compute precisa ser habilitado.

Um **Account Admin** deve executar os passos abaixo:
1. Acessar o Account Console
1. Ir para `Settings` no menu principal à esquerda
1. Ir para `Feature Enablement`
1. Ler e aceitar os termos de utilização no banner que aparecerá no topo da página

*NOTA: caso o banner não apareça, significa que os termos já foram aceitos.*

# Cluster

Você irá precisar de um cluster com a seguinte configuração:
* DBR: 14.3 LTS
* Single Node
* 4 cores

# Databricks CLI

A Databricks CLI facilita a execução de diversas atividades dentro do Databricks. Aqui, a utilizaremos para criar tokens e armazená-los em secrets.

1. Caso já tenha a Databricks CLI instalada, valide a sua versão. Caso seja menor que **0.205.0**, você precisa desinstalar a versão atual e seguir com os passos seguintes<br>
  `databricks -v`<br>
2. Instale a Databricks CLI [[Linux/MacOS](https://docs.databricks.com/en/dev-tools/cli/install.html#curl-install)][[Windows](https://docs.databricks.com/en/dev-tools/cli/install.html#winget-install)]<br>
  `curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh`<br>
3. Configure as suas credenciais<br>
  `databricks configure`

# (Opcional) Service Principal

É recomendada a utilização de um service principal (SP) para que objetos produtivos não fiquem associados aos usuários pessoais.

Um **Workspace/Account Admin** deverá seguir os passos abaixo:

1. Crie um SP [[AWS](https://docs.databricks.com/en/admin/users-groups/service-principals.html#add-a-service-principal-to-a-workspace-using-the-workspace-admin-settings)][[Azure](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/service-principals#--add-a-service-principal-to-a-workspace-using-the-workspace-admin-settings)][[GCP](https://docs.gcp.databricks.com/en/admin/users-groups/service-principals.html#add-a-service-principal-to-a-workspace-using-the-workspace-admin-settings)]
2. Crie um token para o SP [[AWS](https://docs.databricks.com/en/admin/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal)][[Azure](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/service-principals#manage-personal-access-tokens-for-a-service-principal)][[GCP](https://docs.gcp.databricks.com/en/admin/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal)]<br>
  `databricks token-management create-obo-token <application-id> <lifetime-seconds> --comment <comment>`<br>  

# Secret

O endpoint do Model Serving precisa de um secret com o token para se autenticar com o Vector Search (veja a [documentação](https://docs.databricks.com/en/security/secrets/secrets.html)).<br/>

- Crie um secret scope:<br/>
`databricks secrets create-scope <scope>`
- Crie um secret para armazenar o token de autenticação. Use o token criado para seu SP ou, para testes, você pode usar seu [personal access token](https://docs.databricks.com/en/dev-tools/auth/pat.html).<br>
`databricks secrets put-secret <scope> <key>`