class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja Per Hari: {self.jam_kerja} jam")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()
            

def input_karyawan():
    print("Pilih jenis karyawan:")
    print("1. Karyawan Tetap")
    print("2. Karyawan Harian")
    pilihan = input("Masukkan pilihan (1 atau 2): ")

    nama = input("Masukkan nama karyawan: ")
    gaji = int(input("Masukkan gaji karyawan: "))
    departemen = input("Masukkan departemen karyawan: ")

    if pilihan == '1':  
        tunjangan = int(input("Masukkan tunjangan karyawan tetap: "))
        return KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif pilihan == '2': 
        jam_kerja = int(input("Masukkan jam kerja per hari: "))
        return KaryawanHarian(nama, gaji, departemen, jam_kerja)
    else:
        print("Pilihan tidak valid!")
        return None


if __name__ == "__main__":
    manajemen = ManajemenKaryawan()

    while True:
        karyawan = input_karyawan()
        if karyawan:
            manajemen.tambah_karyawan(karyawan)
        lanjut = input("Apakah Anda ingin menambahkan karyawan lagi? (ya/tidak): ").lower()
        if lanjut != 'ya':
            break

    print("\nInformasi Semua Karyawan:")
    manajemen.tampilkan_semua_karyawan()
