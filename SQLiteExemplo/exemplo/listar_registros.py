import sqlite3
from model.Evento import Evento
from database.config import database

def listarEventos():
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
          SELECT * FROM evento;
        """)

        eventos = []

        for linha in cursor.fetchall():
            nome = linha[1]
            dataInicio = linha[2]
            dataFim = linha[3]
            evento = Evento(nome, dataInicio, dataFim)
            eventos.append(evento)

        conn.close()
    except sqlite3.Error:
        print("Problema com o banco de dados")

    return eventos

def main(arg = []):
    eventos = listarEventos()

    for evento in eventos:
        print(evento)

if (__name__ == "__main__"):
    main()