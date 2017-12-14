'''
    Função para exibir o menu. Defina números para acessar as opções.
'''
def exibirMenu():
    print("Rede Social \n"
        " 1 - Definir nome da rede social.\n"
        " n - Próxima opção.\n"
        " 0 - Sair")

def main(args = []):

    # Exibição do Menu de Opções.
    exibirMenu()

    continuar = True

    while continuar:
        try:
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                pass

            elif (opcao == 'n'):
                pass

            elif (opcao == 0):
                continuar = False
            else:
                print("Ops! Opção inválida!")

        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    main()



