from DBFactory import DBFactory
from MSSQL import MSSQL

class MSSQLFactory(DBFactory):
    def createDB(self):
        return MSSQL()
