import sqlite3
from database.config import database

conn = sqlite3.connect(database,
                               detect_types=sqlite3.PARSE_DECLTYPES
                                            | sqlite3.PARSE_COLNAMES)
conn.close()