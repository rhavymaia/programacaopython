resultado = 5
print(resultado)

if (resultado >= 5):
    print("Condição verdadeira")
else:
    print("Condição falsa")
    print("Restante da condição falsa")

while (resultado >= 1 and resultado <= 5):
    print("Imprimir repetição")
    print("Ainda no while?!")
    resultado = resultado - 1
print("Pula fora!")

for item in range(1, 3):
    print("O valor do item é:", item)

alunos = ["Marcos", "Maria Eduarda", "Renan"]
for aluno in alunos:
    print(aluno)


