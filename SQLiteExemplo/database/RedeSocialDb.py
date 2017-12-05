import sqlite3
from database.Connect import Connect

class RedeSocialDb(object):

    def __init__(self):
        self.db = Connect('rede_social.db')

    def close_connection(self):
        self.db.close_db()


def main(args=[]):
    redeSocial = RedeSocialDb()

if __name__ == "__main__":
    main()