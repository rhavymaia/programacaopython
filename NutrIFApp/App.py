from flask import Flask,request
from flask import jsonify
import sqlite3

app = Flask(__name__)

@app.route('/campi', methods=['POST']) #POST: cadastrar.
def cadastrarCampus():
    print("Cadastrar o campus")
    return ""

@app.route('/campi', methods=['GET']) #GET: listar todos.
def listarCampi():
    pass

@app.route("/campi/<int:id>",  methods=['GET']) #GET: retornar a entidade por id.
def consultarCampusPorId(id):
    pass

@app.route("/campi/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerCampusPorId(id):
    pass

@app.route('/alunos', methods=['POST']) #POST: cadastrar.
def cadastrarAluno():
    pass

@app.route('/alunos', methods=['GET']) #GET: listar todos.
def listarAlunos():
    pass

@app.route("/alunos/<int:id>") #GET: retornar a entidade por id.
def consultarAlunoPorId(id):
    pass

@app.route("/alunos/<int:id>", methods=['DELETE']) #DELETE: remover a entidade por id.
def removerAlunoPorId(id):
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')