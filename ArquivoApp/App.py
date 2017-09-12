from model.Pessoa import Pessoa

import json

def main(args=[]):
    while True:
        try:
                # Leitura do Arquivo.
                f = open("pessoas.txt", encoding="utf8")

                # Parser do JSON em Objeto.
                jsonObjs = json.loads(f.read())
                print(jsonObjs)

                # Iteração dos elementos do JSON.
                for jsonObj in jsonObjs:
                    print("Nome da pessoa: " + jsonObj["nome"])
                    nome = jsonObj["nome"]
                    nascimento = jsonObj["nascimento"]
                    pessoa = Pessoa(nome, nascimento)


                with open('data.txt', 'w', encoding='utf-8') as f:
                    json.dump(jsonObjs, f, ensure_ascii=False)

        except FileNotFoundError:
            print("Arquivo não encontrado!")

if __name__ == '__main__':
    main()