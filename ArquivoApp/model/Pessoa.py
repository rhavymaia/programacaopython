import json

class Pessoa():

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def falar(self):
        print("Falando de Pessoa")

    def andar(self):
        print("Andar de Pessoa")

    def __str__(self):
        return ("[nome:%s]" % self.nome)