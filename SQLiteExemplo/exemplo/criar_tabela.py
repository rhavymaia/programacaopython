import sqlite3

# conectando...
conn = sqlite3.connect('eventos.db')
# definindo um cursor.
cursor = conn.cursor()

# criando a tabela.
cursor.execute("""
    CREATE TABLE evento (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_inicio DATETIME NOT NULL,
            data_fim DATETIME NOT NULL
    );
""")

print('Tabela criada com sucesso.')
# desconectando o cursor.
conn.close()