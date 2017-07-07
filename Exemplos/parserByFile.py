import os
import shutil
import glob
from PIL import Image

def parser():
    rootDir = str(input("Informe o diretório de origem:\n"))
    destDir = str(input("Informe o diretório de destino:\n"))

    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Diretório encontrado: %s" % dirName)
        has_image = len(glob.glob(dirName + "\*.jpg"))
        if has_image != 0:
            dirMatr = dirName.find("-")
            if dirMatr != -1:
                matricula = dirName.split("-")
                matricula = matricula[-1]
                matricula = matricula.strip()
                dirCopy = destDir + "\\" + matricula
                shutil.copytree(dirName, dirCopy)
                for fname in fileList:
                    print("\t%s" % fname)
            else:
                nomeAluno = dirName.split("\\")
                nomeAluno = nomeAluno[-1].strip()

                arquivo = open(destDir + "\\" + "alunos_sem_matricula.txt", "a")
                arquivo.write(nomeAluno + "\n")
                arquivo.close()

                print(nomeAluno, " - Não possue matrícula")

def renomearFotoPerfil():
    diretorio = str(input("Informe o diretório:\n"))
    for dirName, subdirList, fileList in os.walk(diretorio):
        if dirName != diretorio: 
            if dirName.endswith("_") == False:
                nomeFoto = dirName + "\\" + fileList[0]
                nomeFotoNovo = dirName + "\\" + "perfil.jpg"
                os.rename(nomeFoto, nomeFotoNovo)
		print("Origem - Arquivo: ", nomeFoto, ", Destino -> ", nomeFotoNovo)

def parserSemTraco():
    rootDir = str(input("Informe o diretório de origem:\n"))
    destDir = str(input("Informe o diretório de destino:\n"))

    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Diretorio encontrado: %s" % dirName)
        has_image = len(glob.glob(dirName + "\*.jpg"))
        if has_image != 0:
            dirMatr = dirName.find("-")
            if dirMatr == -1:
                matricula = dirName.split(" ")[-1]
                if matricula.isdigit():
                    matricula = matricula.strip()
                    dirCopy = destDir + "\\" + matricula
                    shutil.copytree(dirName, dirCopy)
                    for fname in fileList:
                        print("\t%s" % fname)

def redimensionarImagem():
    diretorio = str(input("Informe o diretório:\n"))
    for dirName, subdirList, fileList in os.walk(diretorio):
        if dirName != diretorio:

            qtdArquivos = len(fileList)
            print("Quantidade de arquivos: ", qtdArquivos)
            
            for file in fileList:
                width = 1024
                height = 682
                img = Image.open(dirName + "\\" + file)
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(dirName + "\\" + file)
                print(file,"redimensionado.")
                print("Tamanho: ", width, "x", height)

def main():
    pergunta = eval(input("Para acessar o parser, digite 1. Para acessar o parserSemTraço, digite 2. Para renomear as fotos de perfil, digite 3. Para redimensionar as fotos, digite 4. \n"))
    if pergunta == 1:
        parser()
    elif pergunta == 2:
        parserSemTraco()
    elif pergunta == 3:
        renomearFotoPerfil()
    elif pergunta == 4:
        redimensionarImagem()

if __name__ == "__main__":
    main()
