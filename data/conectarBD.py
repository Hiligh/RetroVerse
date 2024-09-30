import mysql.connector

def conectarBD():
    conexao = mysql.connector.connect(
    host="localhost",
    database="retroversedb",
    user="root",
    password="1234",
    )

    if conexao.is_connected():
        print("DB Conectado!")
    return conexao