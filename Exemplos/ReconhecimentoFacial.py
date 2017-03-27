class ReconhecimentoFacial:

    refeicaoRealizada = None

    foto = None

    def __init__(self, refeicaoRealizada, foto, *args, **kwargs):
        self.refeicaoRealizada = refeicaoRealizada
        self.foto = foto