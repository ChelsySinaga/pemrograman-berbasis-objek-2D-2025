
class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
     
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")


manusia1 = Manusia("Rani", 19, "Medan")
manusia2 = Manusia("Riri ", 19, "Bandung")
manusia3 = Manusia("Andi", 21, "Bogor")
manusia4 = Manusia("Chelsy ", 17, "Medan")
manusia5 = Manusia("Tamara ", 18, "Medan")

manusia4.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia1.berlari()
manusia5.berjalan()