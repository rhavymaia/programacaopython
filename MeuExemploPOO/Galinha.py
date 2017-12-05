from Animal import Animal

class Galinha(Animal):

    def __init__(self, nome, numMembros, habitat, bico):
        super(Galinha, self).__init__(nome, numMembros, habitat, "milho", 1)
        self.bico = bico

    def ciscando(self):
        print("Galinha ciscando")