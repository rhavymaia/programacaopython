# 04_create_data_nrecords.py
import sqlite3

conn = sqlite3.connect('rede_social.db')
cursor = conn.cursor()

# criando uma lista de dados
tuplas = [
    ('João', '2000-10-15', 'M', 'joao@email.com', '123456'),
    ('Maria', '2000-10-09', 'M', 'joao@email.com', '123456')
]

for tupla in tuplas:
    cursor.execute("""
    INSERT INTO usuario (nome, nascimento, genero, email, senha)
    VALUES (?,?,?,?,?)
    """, tupla)
    conn.commit()

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO usuario (nome, nascimento, genero, email, senha)
VALUES (?,?,?,?,?)
""", tuplas)
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()