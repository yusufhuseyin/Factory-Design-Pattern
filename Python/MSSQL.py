from DB import DB

class MSSQL(DB):
    def selectData(self):
        print("Mssql veritabaninda veri cekme islemi gerceklestirilmistir.")

    def insertData(self):
        print("Mssql veritabaninda veri ekleme islemi gerceklestirilmistir.")
