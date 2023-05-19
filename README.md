# Pipeline de ETL para Análise de Dados do Banco de Dados MySQL
Este projeto implementa uma pipeline de ETL (Extração, Transformação e Carga) para extrair dados de uma tabela chamada "cadastros" de um banco de dados MySQL,
realizar transformações nos dados e carregar os dados transformados.

## Pré-requisitos
- Python instalado
- Bibliotecas Python: mysql-connector-python, pandas

## Utilização
Configure as informações de conexão ao banco de dados, certifique-se de fornecer as credenciais corretas. O script irá se conectar ao banco de dados MySQL, extrair os dados da tabela "cadastros", realizará transformações nos dados selecionando apenas registros com idade maior ou igual a 18 anos e exibirá as primeiras linhas dos dados transformados.
