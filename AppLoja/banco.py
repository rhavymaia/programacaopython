import sqlite3

# conectando...
conn = sqlite3.connect('bd_loja.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE tb_cliente (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,       
        email VARCHAR(40) NOT NULL,
        senha VARCHAR(15) NOT NULL        
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()