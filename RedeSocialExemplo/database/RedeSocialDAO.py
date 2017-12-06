import mysql.connector
from model.RedeSocial import RedeSocial
from database.configDB import config

class RedeSocialDAO():

    def inserirRedeSocial(redeSocial: RedeSocial):

        # Id da Rede Social inserida.
        idRedeSocial = 0
        # Script de Inserção.
        query = "INSERT INTO redesocial(nome) " \
                "VALUES(%s)"
        # Valores.
        values = (redeSocial.nome)

        try:
            # Conexão com a base de dados.
            conn = mysql.connector.connect(**config)  # Nome do BD.
            # Preparando o cursor para a execução da consulta.
            cursor = conn.cursor()
            cursor.execute(query, values)
            # Último id da redesocial inserida no banco.
            if cursor.lastrowid:
                idRedeSocial = cursor.lastrowid
            # Finalizando a persistência dos dados.
            conn.commit()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
        # Retornar id da rede social.
        return idRedeSocial