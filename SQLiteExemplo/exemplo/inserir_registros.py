import sqlite3
from database.config import database

conn = sqlite3.connect(database)
cursor = conn.cursor()

evento1 = ('Semana Nacional de Ciência e Tecnologia', '2017-01-01 08:00:00', '2017-01-03 18:00:00')
evento2 = ('2º Simpósio de Pesquisa, Inovação e Pós-graduação', '2017-11-20 08:00:00', '2017-11-23 18:00:00')
# criando uma lista de dados
lista = [evento1, evento2]

# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO evento (nome, data_inicio, data_fim)
    VALUES (?, ?, ?)
""", lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()