from model.Maratona import Maratona
from model.Cliente import Cliente
from model.Funcionario import Funcionario

def main(args=[]):
    funcionario = Funcionario("José")
    cliente = Cliente("Maria")

    maratona = Maratona()
    maratona.correr(funcionario)
    maratona.correr(cliente)

if __name__ == '__main__':
    main(['teste'])