class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup.")

    def tampilkan(self):
        print(f"No Rek: {self.get_no_rek()}, Nama: {self.get_nama()}, Saldo: {self.get_saldo()}")


class Bank:
    def __init__(self):
        self.rekening = []

    def tambah_rekening(self):
        no_rek = input("Masukkan No Rekening: ")
        nama = input("Masukkan Nama Pemilik: ")
        saldo = float(input("Masukkan Saldo Awal: "))
        self.rekening.append(RekeningBank(no_rek, nama, saldo))

    def setor(self):
        no_rek = input("Masukkan No Rekening: ")
        jumlah = float(input("Masukkan Jumlah Setoran: "))
        for r in self.rekening:
            if r.get_no_rek() == no_rek:
                r.setor(jumlah)
                return
        print("Rekening tidak ditemukan.")

    def tarik(self):
        no_rek = input("Masukkan No Rekening: ")
        jumlah = float(input("Masukkan Jumlah Penarikan: "))
        for r in self.rekening:
            if r.get_no_rek() == no_rek:
                r.tarik(jumlah)
                return
        print("Rekening tidak ditemukan.")

    def tampilkan_semua(self):
        for r in self.rekening:
            r.tampilkan()

bank = Bank()
while True:
    print("\n=== MENU BANK ===")
    print("1. Tambah Rekening")
    print("2. Setor")
    print("3. Tarik")
    print("4. Tampilkan Semua Rekening")
    print("5. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        bank.tambah_rekening()
    elif pilih == "2":
        bank.setor()
    elif pilih == "3":
        bank.tarik()
    elif pilih == "4":
        bank.tampilkan_semua()
    elif pilih == "5":
        break
    else:
        print("Pilihan tidak valid.")