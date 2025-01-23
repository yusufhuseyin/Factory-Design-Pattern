public class MSSQLFactory : DBFactory{
    public DB CreateDB(){
        return new MSSQL();
    }
}
