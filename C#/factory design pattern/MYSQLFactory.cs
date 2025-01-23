public class MYSQLFactory : DBFactory{
    public DB CreateDB(){
        return new MYSQL();
    }
}
