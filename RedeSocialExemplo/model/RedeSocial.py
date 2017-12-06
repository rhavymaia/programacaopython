class RedeSocial():

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return "<RedeSocial %s>"%(self.nome)