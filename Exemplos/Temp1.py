from Temp2 import leiaString

def imprimir(valor):
    print("Temp1: ", __name__)
    print(valor)
    
def main(args=None):
    imprimir("Args: " + args)
    imprimir(leiaString())

if(__name__=="__main__"):
    main("IFPB")
