from flask import Flask,request
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route('/cliente', methods=['POST']) #GET requests will be blocked
def cadastrarCliente():

    # Recuperar os dados da requisição
    nome = str(request.form['nome'])
    email = str(request.form['email'])
    senha = str(request.form['senha'])

    # Persistir dados do Cliente
    salvarCliente(nome, email, senha)

    return """
        <html>
            <head></head>
            <body>%s, %s, %s</body>
        </html>
    """%(nome, email, senha)

@app.route('/cliente', methods=['GET']) #GET requests will be blocked
def consultarCliente():

    conn = sqlite3.connect('bd_loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
      SELECT * FROM tb_cliente;
    """)
    # Lista de Pessoas.
    pessoas = []

    for linha in cursor.fetchall():
        nome = str(linha[1])
        email = str(linha[2])
        senha = str(linha[3])
        # Pessoa.
        pessoa = {'nome': nome, 'email': email,'senha': senha}
        # Adicionar a pessoa a lista.
        pessoas.append(pessoa)

    conn.close()

    resp = jsonify(pessoas)
    resp.status_code = 201

    return resp

def salvarCliente(nome, email, senha):
    # Persistência dos dados
    conn = sqlite3.connect('bd_loja.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
          INSERT INTO tb_cliente (nome, email, senha)
          VALUES (?,?,?)
        """, (nome, email, senha))

    conn.commit()
    print("Savando dados de %s, %s, %s" % (nome, email, senha))

if __name__ == '__main__':
    app.run(host='0.0.0.0')