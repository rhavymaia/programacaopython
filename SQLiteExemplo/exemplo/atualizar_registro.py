import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id = 1
nome = 'Semana Nacional de Ciência e Tecnologia'
data_inicio = '2017-01-01 08:00:00'
data_fim = '2017-01-03 18:00:00'

# alterando os dados da tabela
cursor.execute("""
    UPDATE evento
    SET nome = ?, data_inicio = ?, data_fim = ?
    WHERE id = ?
""", (nome, data_inicio, data_fim, id))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()