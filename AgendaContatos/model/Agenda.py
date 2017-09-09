'''
    Agenda - reprensenta a agenda telefônica.
'''
class Agenda():
    def __init__(self, proprietario, contatos = []):
        self.proprietario = proprietario
        self.contatos = contatos

    def __str__(self):
        return "Agenda[proprietario: %s, contatos: %s]"%(self.proprietario, self.contatos)

    def contarContatos(self):
        return 0

    def listarContatos(self):
        return []

    def incluirContato(self, contato):
        # Incluir contato numa lista.
        pass

    def excluirContato(self, nome):
        # Excluir contato da lista.
        pass

    def buscarContato(self, nome):
        # Buscar contato pelo nome
        pass