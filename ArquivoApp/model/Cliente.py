from model.Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome):
        super(Cliente, self).__init__(nome)

    def pagar(self):
        print("Pagar de Cliente")