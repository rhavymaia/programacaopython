import mysql.connector


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class DAO(Singleton):
    def __init__(self):
        """
            Iniciar conexão com o banco de dados.
        """
        self._connect()
        return

    def _connect(self):
        """
            Criar conexão.
        """
        try:
            self.connection = mysql.connector.connect(user='root',
                                      password='ifpbinfo',
                                      host='127.0.0.1',
                                      database='escola')
        except mysql.connector.Error as err:
            print("Problema no banco de dados!")

    def _get_cursor(self):
        """
            Restabelecer a conexão e retornar o cursor.
        """
        try:
            # Restabelecer a reconexão.
            self.connection.ping()
        except:
            self._connect()
        # Cursor
        return self.connection.cursor()

    def get_row(self, query, values=()):
        """
            Retornar a primeira linha do resultado da consulta.
        """
        cursor = self._get_cursor()
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_rows(self, query, values=()):
        """
            Retornar todas as linhas do resultado da consulta.
        """
        cursor = self._get_cursor()
        cursor.execute(query, values)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def insert(self, query, values=()):
        """
            Inserir um único registro.
        """
        cursor = self._get_cursor()
        # Inserir novo registro (query e valores).
        cursor.execute(query, values)
        last_id = cursor.lastrowid

        # Certificar que os dados foram persistidos.
        self.connection.commit()
        # Encerrar o cursor.
        cursor.close()

        return last_id

    def insert_many(self, query, itens=[]):
        """
            Inserir uma lista de registro.
        """
        cursor = self._get_cursor()
        cursor.executemany(query, itens)
        self.connection.commit()
        cursor.close()
        return

    def execute(self, query, values=()):
        """
            Executar consultas para update e delete.
        """
        cursor = self._get_cursor()
        cursor.execute(query, values)
        cursor.close()
        return