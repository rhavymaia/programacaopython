from database.EventoDAO import EventoDAO

def listarEventos():
    eventoDAO = EventoDAO()
    eventos = eventoDAO.listar()
    return eventos


def main(arg = []):
    eventos = listarEventos()

    for evento in eventos:
        print(evento)

if (__name__ == "__main__"):
    main()