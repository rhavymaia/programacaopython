import sqlite3
from model.Evento import Evento
from database.config import database

class EventoDAO():
    def __init__(self):
        pass

    def inserir(self, evento: Evento):
        pass

    def listar(self):
        try:
            conn = sqlite3.connect(database,
                                   detect_types=sqlite3.PARSE_DECLTYPES
                                                | sqlite3.PARSE_COLNAMES)
            cursor = conn.cursor()

            # lendo os dados
            cursor.execute("""
              SELECT * FROM evento;
            """)

            eventos = []

            for linha in cursor.fetchall():
                nome = linha[1]
                dataInicio = linha[2]
                print(type(dataInicio))
                dataFim = linha[3]
                evento = Evento(nome, dataInicio, dataFim)
                eventos.append(evento)

            conn.close()
        except sqlite3.Error:
            print("Problema com o banco de dados")

        return eventos

    def atualizar(self, evento: Evento):
        pass

    def remover(self, id: int):
        pass
