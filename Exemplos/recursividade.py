def imprima(valor):
    print(valor)

def soma(x, y):
    resultado = x + y
    imprima(resultado)
    if (resultado<=500):
        soma(1, resultado)

def somaTotal(x):
    total = 0
    for i in range(1, x+1):
        total+=i
    return total

def main(args=[]):
    x = int(input("Digite o valor de x: "))
    total = somaTotal(x)
    imprima(total)

if (__name__ == "__main__"):
    main()