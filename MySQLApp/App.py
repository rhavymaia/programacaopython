from Aluno import Aluno
from datetime import date

nome = "João Grilo"
email = "jg@mail.com"
matricula = "20161002007"
nascimento = date(2017, 6, 24)
aluno = Aluno(matricula, nome, email)
id = aluno.insert()
print(id)