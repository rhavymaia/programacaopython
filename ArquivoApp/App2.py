from model.Pessoa import Pessoa

import json

def main(args=[]):
        jsonString = '[{"nome": "João", "idade":"17"}]'

        jsonObjs = json.loads(jsonString)

        pedro = Pessoa("Pedro", "01/03/2017")

        # Converter o Objeto Pessoa em Json e adicionar na Lista de Jsons.



if __name__ == '__main__':
    main()