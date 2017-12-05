# 06_read_data.py
import sqlite3
from model.Usuario import Usuario

conn = sqlite3.connect('rede_social.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
  SELECT * FROM usuario;
""")

usuarios = []

linhas = cursor.fetchall()
for linha in linhas:
    id = linha[0]
    nome = linha[1]
    nascimento = linha[2]
    genero = linha[3]
    email = linha[4]
    senha = linha[5]
    usuario = Usuario(nome, nascimento, genero, email, senha)
    print(usuario)
    usuarios.append(usuario)

print(usuarios)

conn.close()