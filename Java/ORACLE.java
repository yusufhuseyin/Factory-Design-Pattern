public class ORACLE implements DB {
    @Override
    public void selectData() {
        System.out.println("Oracle veritabaninda veri cekme islemi gerceklestirilmistir.");
    }

    @Override
    public void insertData() {
        System.out.println("Oracle veritabainda veri ekleme islemi gerceklestirilmistir.");
    }
}