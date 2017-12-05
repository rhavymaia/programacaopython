from model.Pessoa import Pessoa

import json

def main(args=[]):
    while True:
        try:
            print('Digite umas das opções: 1, 2 ou 3')
            opcao = int(input('Digite o valor da Opção:'))

            file = open("meuarquivo.txt", "r")
            print(opcao)
        except (ValueError) as e:
            print('Algum erro inesperado ocorreu.')
        except Exception:
            print('Outra Exceção')

if __name__ == '__main__':
    main()