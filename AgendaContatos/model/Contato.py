class Contato():
    def __init__(self, pessoa, criacao):
        self.pessoa = pessoa
        self.criacao = criacao
        self.telefones = []

    def __str__(self):
        return "Contato[pessoa: %s]"%(self.pessoa)

    def listarTelefones(self):
        return self.telefones;

    def contarTelefones(self):
        return len(self.telefones)