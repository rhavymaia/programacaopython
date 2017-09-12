from model.Pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome):
        super(Funcionario, self).__init__(nome)