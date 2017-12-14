import sqlite3

conn = sqlite3.connect('eventos.db')
cursor = conn.cursor()

id = 3

# excluindo um registro da tabela
cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
""", (id))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()