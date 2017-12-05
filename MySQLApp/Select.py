import mysql.connector

try:
    # Abrir a conexão com o banco de dados.
    conn = mysql.connector.connect(user='root', # Usuário.
                                   password='ifpbinfo', # Senha.
                                   host='127.0.0.1', # IP local do BD.
                                   database='escola') # Nome do BD.
    # Cursor para executar a DML.
    cursor = conn.cursor()

    # Consulta
    query = ("SELECT id_aluno, nm_matricula, nm_aluno FROM tb_aluno")
    cursor.execute(query)
    linhas = cursor.fetchall()

    # Resultset
    for (id_aluno, nm_matricula, nm_aluno) in linhas:
      print(id_aluno, nm_matricula, nm_aluno)

    # Fechar cursor.
    cursor.close()

except mysql.connector.Error as err:
    # Problema com o MySQL.
    print("Problema no banco de dados!")
else:
    # Fechar conexão.
    conn.close()