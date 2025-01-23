public class ORACLEFactory : DBFactory{
    public DB CreateDB(){
        return new ORACLE();
    }
}
