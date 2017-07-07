class Animal():
    def __init__(self, nome, numMembros, habitat):
        self.nome = nome
        self.numMembros = numMembros
        self.habitat = habitat

    def comer(self):
        print(self.nome + " animal come de forma genérica.")

    def mover(self):
        print(self.nome + " animal move de forma genérica.")

    def comunicar(self):
        print(self.nome + " animal comunica de forma genérica.")

    def __str__(self):
        return "Animal [nome: %s, numMembros: %d, habitat: %s]" % (self.nome, self.numMembros, self.habitat)

    def __add__(self, other):
        return Animal(self.nome + other.nome, self.numMembros, self.habitat)