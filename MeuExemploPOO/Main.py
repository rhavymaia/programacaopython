from Cachorro import Cachorro
from Galinha import Galinha
from model import Cavalo

def main():
    a1 = Cachorro("Lulu", 4, "Casa", "marrom")
    a1.mover()
    a1.farejar()
    print(a1)

    a2 = Cachorro("Max", 4, "Casa", "branco")
    a2.mover()
    a2.farejar()
    print(a2)

    print(a1 + a2)

    a2 = Galinha("Zezé", 2, "Galinheiro")
    a2.mover()
    a2.comer()

    c1 = Cavalo()

if __name__ == '__main__':
    main()