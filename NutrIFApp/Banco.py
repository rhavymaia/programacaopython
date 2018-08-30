import sqlite3

# conectando...
conn = sqlite3.connect('bd_nutrif.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela de campus.
cursor.execute("""
CREATE TABLE tb_campus (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT       
);
""")

# criando a tabela de aluno.
cursor.execute("""
CREATE TABLE tb_aluno (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT       
);
""")

# criando a tabela de nutricionista.
cursor.execute("""
CREATE TABLE tb_nutricionista (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT       
);
""")

# criando a tabela de refeição.
cursor.execute("""
CREATE TABLE tb_refeicao (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT       
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()