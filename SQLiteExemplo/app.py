import sqlite3

# Conexão
conn = sqlite3.connect('rede_social.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute(""" CREATE TABLE usuario (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(150) NOT NULL,
        nascimento DATE,
        genero VARCHAR(10) NOT NULL,
        email VARCHAR(100) NOT NULL,
        senha VARCHAR(15) NOT NULL
);
""")

print('Tabela criada com sucesso.')

conn.close()