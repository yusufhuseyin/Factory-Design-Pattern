public class MYSQL implements DB {
    @Override
    public void selectData() {
        System.out.println("Mysql veritabaninda veri cekme islemi gerceklestirilmistir.");
    }

    @Override
    public void insertData() {
        System.out.println("Mysql veritabainda veri ekleme islemi gerceklestirilmistir.");
    }
}