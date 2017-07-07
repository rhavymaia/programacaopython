from Animal import Animal

class Galinha(Animal):

    def __init__(self, nome, numMembros, habitat):
        super(Galinha, self).__init__(nome, numMembros, habitat)

    def ciscando(self):
        print("Galinha ciscando")