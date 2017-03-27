def calcularMedia(notas):
    # Calcular média aritmética.
    total = 0
    for nota in notas:
        total = nota + total

    media = total / len(notas)

    return media

def adicionarTurma(turmas, identificador, alunos):
    # Adicionar a turma ao dicionário.
    turmas[identificador] = alunos
    return turmas

def adicionarAlunosNotas():
    # Adicionar a lista de Notas de um Aluno.
    return None

def main(args=None):
    # Método principal
    turmas = {}

    identificador = str(input("Digite o identificador (1BINFO): "))
    alunos = []

    notas = [7, 7, 8]
    aluno = {"201610040029": notas}
    alunos.append(aluno)

    turmas = adicionarTurma(turmas, identificador, alunos)
    print(calcularMedia(notas))

    print(turmas)

if __name__ == "__main__":
    main()

