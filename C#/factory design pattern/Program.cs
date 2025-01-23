using System;

public class MainClass{
    public static void Main(){
        DBFactory factory = new MYSQLFactory();
        DBFactory factory1 = new MSSQLFactory();
        DBFactory factory2 = new ORACLEFactory();

        DB mysql = factory.CreateDB();
        mysql.SelectData();
        mysql.InsertData();

        DB mssql = factory1.CreateDB();
        mssql.SelectData();
        mssql.InsertData();

        DB oracle = factory2.CreateDB();
        oracle.SelectData();
        oracle.InsertData();
    }
}
