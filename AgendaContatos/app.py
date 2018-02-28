from model.Agenda import Agenda
from model.Pessoa import Pessoa
from model.Contato import Contato
from model.Telefone import Telefone

'''
    Função para exibir o menu.
'''
def exibirMenu():
    print("Agenda Telefônica \n"
          " 1 - Iniciar a Agenda \n"
          " 2 - Criar Contato \n"
          " 6 - Sair")

'''
    Criação de Pessoa
'''
def criarPessoa():
    # Dados do proprietário
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    nascimento = input("Digite sua data de nascimento: ")

    pessoa = Pessoa(nome, nascimento, email)

    return pessoa

def criarContato():
    pessoa = criarPessoa()
    criacao = input("Criacao: ")
    contato = Contato(pessoa, criacao)

    return contato

def criarAgenda():
    proprietario = criarPessoa()
    agenda = Agenda(proprietario)

    return agenda

def main(args = []):

    # Agenda.
    agenda =  None

    # Exibição do Menu de Opções.
    exibirMenu()

    continuar = True

    while continuar:
        try:
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                agenda = criarAgenda()

            elif (opcao == 2):
                contato = criarContato()
                agenda.contatos.append(contato)

            elif (opcao == 6):
                continuar = False
            else:
                print("Ops! Opção inválida!")

            print(agenda)
        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    #comentario de Manel!
    main()
