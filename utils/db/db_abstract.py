# This is the abstract class for the database connection


class DBAbstract:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        pass

    def close(self):
        pass

    def execute(self, query):
        pass

    def fetchall(self):
        pass

    def fetchone(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass