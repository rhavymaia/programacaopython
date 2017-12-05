import mysql.connector

try:
    # Abrir a conexão com o banco de dados.
    cnx = mysql.connector.connect(user='root',
                              password='ifpbinfo',
                              host='127.0.0.1',
                              database='escola')

except mysql.connector.Error as err:
    print("Problema no banco de dados!")
else:
    # Fechar conexão.
    cnx.close()