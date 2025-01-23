from MSSQLFactory import MSSQLFactory
from MYSQLFactory import MYSQLFactory
from ORACLEFactory import ORACLEFactory


class Main:
    def main():
        factory = MYSQLFactory()
        factory1 = MSSQLFactory()
        factory2 = ORACLEFactory()

        mysql = factory.createDB()
        mysql.selectData()
        mysql.insertData()

        mssql = factory1.createDB()
        mssql.selectData()
        mssql.insertData()

        oracle = factory2.createDB()
        oracle.selectData()
        oracle.insertData()

# Ana fonksiyonu çalıştırmak için:
if __name__ == "__main__":
    Main.main()
