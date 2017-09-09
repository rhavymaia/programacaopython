class Pessoa():
    def __init__(self, nome, nascimento, email):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

    def __str__(self):
        return "Pessoa[nome: %s, email: %s]"%(self.nome, self.email)

