import sqlite3
from database.config import database

# Conexão
conn = sqlite3.connect(database,
                               detect_types=sqlite3.PARSE_DECLTYPES
                                            | sqlite3.PARSE_COLNAMES)
# definindo um cursor.
cursor = conn.cursor()

# criando a tabela.
cursor.execute("""
    CREATE TABLE evento (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_inicio TIMESTAMP NOT NULL,
            data_fim TIMESTAMP NOT NULL
    );
""")

print('Tabela criada com sucesso.')
# desconectando o cursor.
conn.close()