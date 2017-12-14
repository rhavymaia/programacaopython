class Evento():
    def __init__(self, nome, dataInicio, dataFim):
        self.nome = nome
        self.dataInicio = dataInicio
        self.dataFim = dataFim

    def __str__(self):
        return "<Evento: %s, %s, %s>" % (self.nome, self.dataInicio, self.dataFim)