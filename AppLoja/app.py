from flask import Flask,request
from flask import jsonify
from Pessoa import Pessoa
import sqlite3

app = Flask(__name__)

@app.route('/clientes', methods=['POST']) #GET requests will be blocked
def cadastrarClientes():

    print("Entrou na função")
    req_data = request.get_json()

    # Recuperar os dados da requisição
    nome = str(req_data['nome'])
    email = str(req_data['usuario'])
    senha = str(req_data['senha'])

    # Persistência dos dados
    conn = sqlite3.connect('bd_loja.db')
    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
      INSERT INTO tb_cliente (nome, email, senha)
      VALUES (?,?,?)
    """, (nome, email, senha))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()

    resp = jsonify()
    resp.status_code = 201

    return resp

@app.route('/clientes', methods=['GET']) #GET requests will be blocked
def consultarClientes():

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

@app.route("/clientes/<int:id>")
def consultarClientePorId(id):

    pessoa = []

    conn = sqlite3.connect('bd_loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
          SELECT * FROM tb_cliente WHERE id = %d;
        """%(id))

    resultSet = cursor.fetchone()

    if resultSet is not None:
        id = str(resultSet[0])
        nome = str(resultSet[1])
        email = str(resultSet[2])
        senha = str(resultSet[3])

        # Pessoa.
        pessoa = {'id': id,'nome': nome, 'email': email, 'senha': senha}

    conn.close()

    resp = jsonify(pessoa)
    resp.status_code = 201

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')