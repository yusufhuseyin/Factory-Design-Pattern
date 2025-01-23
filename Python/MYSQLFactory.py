from DBFactory import DBFactory
from MYSQL import MYSQL

class MYSQLFactory(DBFactory):
    def createDB(self):
        return MYSQL()
