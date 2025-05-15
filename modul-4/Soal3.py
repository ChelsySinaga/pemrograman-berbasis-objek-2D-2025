class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def set_nama(self, nama):
        self.__nama = nama

    def set_umur(self, umur):
        self.__umur = umur

    def set_keluhan(self, keluhan):
        self.__keluhan = keluhan

    def tampilkan(self):
        print(f"Nama: {self.get_nama()}, Umur: {self.get_umur()}, Keluhan: {self.get_keluhan()}")
class Klinik:
    def __init__(self):
        self.daftar_pasien = []

    def tambah_pasien(self):
        nama = input("Masukkan Nama Pasien: ")
        umur = int(input("Masukkan Umur Pasien: "))
        keluhan = input("Masukkan Keluhan: ")
        self.daftar_pasien.append(Pasien(nama, umur, keluhan))

    def tampilkan_semua(self):
        for pasien in self.daftar_pasien:
            pasien.tampilkan()

klinik = Klinik()
while True:
    print("\n=== MENU KLINIK ===")
    print("1. Tambah Pasien")
    print("2. Lihat Daftar Pasien")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        klinik.tambah_pasien()
    elif pilih == "2":
        klinik.tampilkan_semua()
    elif pilih == "3":
        break
    else:
        print("Pilihan tidak valid.")
