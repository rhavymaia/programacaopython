from DAO import DAO
class Aluno(DAO):

    def __init__(self, matricula, nome, email):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        super(Aluno, self).__init__()

    def insert(self):
        query = "INSERT INTO tb_aluno (nm_matricula, nm_aluno, nm_email)" \
                " VALUES (%s, %s, %s)"
        values = (self.matricula, self.nome, self.email)
        return super(Aluno, self).insert(query, values)