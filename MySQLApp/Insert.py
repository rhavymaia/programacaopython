from __future__ import print_function
import mysql.connector

try:
    # Abrir a conexão com o banco de dados.
    cnx = mysql.connector.connect(user='root',
                                  password='ifpbinfo',
                                  host='127.0.0.1',
                                  database='escola')
    # Cursor para executar a DML.
    cursor = cnx.cursor()
    # DML
    add_aluno = ("INSERT INTO tb_aluno (nm_matricula, nm_aluno, nm_email) "
                   "VALUES (%s, %s, %s)")

    data_aluno = ('Geert', 'Vanderkelen', 'gv@mail.com')

    # Inserir novo aluno (DML e dados).
    cursor.execute(add_aluno, data_aluno)
    id_aluno = cursor.lastrowid

    # Certificar que os dados foram persistidos.
    cnx.commit()

    cursor.close()

except mysql.connector.Error as err:
    print("Problema no banco de dados!")
else:
    # Fechar conexão.
    cnx.close()