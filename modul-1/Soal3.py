class Kucing:
    def __init__(self, nama, warna, usia):
        self.nama = nama
        self.warna = warna
        self.usia = usia

    def suara(self):
        return "Meow"

    def tampilkan_info(self):
        print(f"Kucing: {self.nama}, Warna: {self.warna}, Usia: {self.usia}, Suara: {self.suara()}")


class Sapi:
    def __init__(self, nama, ras, usia):
        self.nama = nama
        self.ras = ras
        self.usia = usia

    def suara(self):
        return "MOOOOOO"

    def tampilkan_info(self):
        print(f"Sapi: {self.nama}, Ras: {self.ras}, Usia: {self.usia}, Suara: {self.suara()}")


class Burung:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def suara(self):
        return "Cuit cuit"

    def tampilkan_info(self):
        print(f"Burung: {self.nama}, Jenis: {self.jenis}, Warna: {self.warna}, Suara: {self.suara()}")


kucing_list = [
    Kucing("Milo", "Oren", "7 bulan"),
    Kucing("Luna", "Belang", "1 tahun"),
    Kucing("Simba", "Putih", "4 bulan")
]

sapi_list = [
    Sapi("Sambo", "Limousin", "9 tahun"),
    Sapi("Dodo", "Brahman", "7 tahun"),
    Sapi("Mumu", "Simental", "5 tahun")
]

burung_list = [
    Burung("Ciko", "Beo", "Hijau"),
    Burung("Geo", "Merpati", "Putih"),
    Burung("Bara", "Dara", "Coklat")
]

for kucing in kucing_list:
    kucing.tampilkan_info()

for sapi in sapi_list:
    sapi.tampilkan_info()

for burung in burung_list:
    burung.tampilkan_info()
