from interface.PessoaInterface import PessoaInterface
from datetime import date
from typing import TypeVar
from typing import List

class Pessoa(PessoaInterface):

    def __init__(self, nome: str, email: str, nascimento: date):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

    def cadastrar(self):
        print('Cadastrando em Pessoa')
        pessoa = Pessoa(self.nome, self.email, self.nascimento)
        return pessoa

    def falar(self):
        print("Falando de Pessoa")

    def andar(self):
        print("Andar de Pessoa")

    def __str__(self):
        return ("[nome:%s]" % self.nome)

    def __eq__(self, other):
        return (self.nome == other.nome) \
               and (self.email == other.email) \
               and (self.nascimento == other.nascimento)