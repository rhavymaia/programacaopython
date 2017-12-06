from model.Pessoa import Pessoa

class Usuario(Pessoa):

    def __init__(self, nome, nascimento, genero, email, senha):
        self.nome = nome
        self.nascimento = nascimento
        self.genero = genero
        self.email = email
        self.senha = senha

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()