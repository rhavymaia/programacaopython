from model.Usuario import Usuario
from model.RedeSocial import RedeSocial
from database.RedeSocialDAO import RedeSocialDAO

'''
    Função para exibir o menu. Defina os números para acessar as opções.
'''
def exibirMenu():
    print("Rede Social \n"
        " 1 - Definir nome da rede social.\n"
        " n - Próxima opção.\n"
        " 0 - Sair")

'''
    Criação da Rede Social.
'''
def criarRedeSocial():
    # Necessário inicializar os valores da RedeSocial.
    nome = str(input("Digite um nome da Rede Social: "))
    redeSocial = RedeSocial(nome)
    redeSocialDAO = RedeSocialDAO()
    idRedeSocial = redeSocialDAO.inserirRedeSocial(redeSocial)

'''
    Criação do Usuário.
'''
def criarUsuario(usuario: Usuario):
    pass

'''
    Listar os Usuários.
'''
def listarUsuarios():
    pass

'''
    Remover um Usuário.
'''
def removerUsuario(id: int):
    pass

def main(args = []):

    # Exibição do Menu de Opções.
    exibirMenu()

    continuar = True

    while continuar:
        try:
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                criarRedeSocial()

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



