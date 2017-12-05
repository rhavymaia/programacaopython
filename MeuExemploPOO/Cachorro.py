from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, numMembros, habitat, corPelo):
        super(Cachorro, self).__init__(nome, numMembros, habitat, "ração", 1)
        self.corPelo = corPelo

    def mover(self):
        print("Cachorro se movendo!")

    def farejar(self):
        print("Cachorro farejando especificamente.")
