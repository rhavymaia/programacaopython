# 03_create_data_sql.py
import sqlite3

conn = sqlite3.connect('rede_social.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO usuario (nome, nascimento, genero, email, senha)
VALUES ('Regis', '2000-12-25', 'M', 'regis@email.com', '123456')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()