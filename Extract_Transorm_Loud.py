from senhas import password_mysql
import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password_mysql,
    database="registros"
)

# Extraindo dados da tabela cadastros
query = "SELECT * FROM cadastros"
df = pd.read_sql(query, mydb)

mydb.close()

# Transformações de dados selecionando apenas registros em que a idade é maior ou igual a 18
df = df.query('Idade >= 18')[['ID', 'Nome', 'Idade']]

# Carregamento dos dados transformados
print(df.head())
