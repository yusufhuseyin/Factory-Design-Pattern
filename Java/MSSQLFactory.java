public class MSSQLFactory implements DBFactory {

    @Override
    public DB createDB() {
        return new MSSQL();
    }
}
