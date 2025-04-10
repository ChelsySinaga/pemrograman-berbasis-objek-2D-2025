class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, Alamat: {self.alamat}")

mahasiswa_list = []
for i in range(3):
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan/Prodi: ")
    alamat = input("Masukkan Alamat: ")
    mahasiswa_list.append(Mahasiswa(nama, nim, jurusan, alamat))

for m in mahasiswa_list:
    m.tampilkan_info()