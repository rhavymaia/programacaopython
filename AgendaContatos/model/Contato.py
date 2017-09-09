class Contato():
    def __init__(self, pessoa, criacao):
        self.pessoa = pessoa
        self.criacao = criacao

    def __str__(self):
        return "Contato[pessoa: %s]"%(self.pessoa)

    def listarTelefones(self):
        return []