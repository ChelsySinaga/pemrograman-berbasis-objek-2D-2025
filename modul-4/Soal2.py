class Buku:
    def __init__(self, judul, penulis, halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_halaman(self):
        return self.__halaman

    
    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_halaman(self, halaman):
        self.__halaman = halaman

    def tampilkan(self):
        print(f"Judul: {self.get_judul()}, Penulis: {self.get_penulis()}, Halaman: {self.get_halaman()}")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self):
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Penulis: ")
        halaman = int(input("Masukkan Jumlah Halaman: "))
        self.daftar_buku.append(Buku(judul, penulis, halaman))

    def tampilkan_semua(self):
        for buku in self.daftar_buku:
            buku.tampilkan()

perpus = Perpustakaan()
while True:
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        perpus.tambah_buku()
    elif pilih == "2":
        perpus.tampilkan_semua()
    elif pilih == "3":
        break
    else:
        print("Pilihan tidak valid.")
