from DBFactory import DBFactory
from ORACLE import ORACLE

class ORACLEFactory(DBFactory):
    def createDB(self):
        return ORACLE()
