import sqlite3
from .db_abstract import DBAbstract

# This is the class for the SQLite database connection

class SQLiteDB(DBAbstract):
    def __init__(self, db_name):
        super().__init__()
        self.__db_name = db_name

    def connect(self):
        self.__connection = sqlite3.connect(self.__db_name + '.db')
        self.__cursor = self.__connection.cursor()

    def close(self):
        self.__cursor.close()
        self.__connection.close()

    def execute(self, query):
        self.__cursor.execute(query)

    def fetchall(self):
        return self.__cursor.fetchall()

    def fetchone(self):
        return self.__cursor.fetchone()

    def commit(self):
        self.__connection.commit()

    def rollback(self):
        self.__connection.rollback()