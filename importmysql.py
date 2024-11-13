import mysql.connector

# Configuração de conexão com o banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "#Jeferson255",
    "database": "teste"
}

try:
    # Conectar ao banco de dados
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        cursor = connection.cursor()

        # Exemplo de consulta
        query = "SELECT * FROM teste"
        cursor.execute(query)

        # Obtendo os resultados
        results = cursor.fetchall()
        for row in results:
            print(row)

except mysql.connector.Error as err:
    print("Erro ao tentar se conectar ao banco de dados", err)

finally:
    # Fechar cursor e conexão
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
