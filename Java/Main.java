public class Main {
    public static void main() {
        DBFactory factory = new MYSQLFactory();
        DBFactory factory1 = new MSSQLFactory();
        DBFactory factory2 = new ORACLEFactory();
        DB mysql = factory.createDB();
        mysql.selectData();
        mysql.insertData();
        DB mssql = factory1.createDB();
        mssql.selectData();
        mssql.insertData();
        DB oracle = factory2.createDB();
        oracle.selectData();
        oracle.insertData();
    }
}
