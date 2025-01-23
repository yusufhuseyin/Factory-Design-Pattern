public class MSSQL implements DB {
    @Override
    public void selectData() {
        System.out.println("Mssql veritabaninda veri cekme islemi gerceklestirilmistir.");
    }

    @Override
    public void insertData() {
        System.out.println("Mssql veritabainda veri ekleme islemi gerceklestirilmistir.");
    }
}