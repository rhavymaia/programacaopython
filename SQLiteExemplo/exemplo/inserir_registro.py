import sqlite3
from database.config import database

conn = sqlite3.connect(database,
                               detect_types=sqlite3.PARSE_DECLTYPES
                                            | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

evento = ('Semana Nacional de Ciência e Tecnologia 2', '2017-01-01 08:00:00', '2017-01-03 18:00:00')

# inserindo dados na tabela
cursor.execute("""
    INSERT INTO evento (nome, data_inicio, data_fim)
    VALUES (?, ?, ?)
""", evento)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()