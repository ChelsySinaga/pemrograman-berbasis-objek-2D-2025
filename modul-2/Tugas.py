class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            raise ValueError("SKS tidak valid! Hanya boleh 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} | {self.nama} ({self.sks} SKS)"

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(" NIM tidak valid! Harus dimulai dengan '23' dan terdiri dari 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul.append(matkul)

    def tampilkan_biodata(self):
        print(f"\nNama : {self.nama}")
        print(f"NIM  : {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for m in self.matkul:
            print(f" - {m}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10


class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama(nama):
            raise ValueError(" Nama kampus tidak valid! Tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, kampus_obj):
        print("\n====== INFO KAMPUS ======")
        print(f"Nama Kampus : {kampus_obj.nama}")
        print(f"Alamat      : {kampus_obj.alamat}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")
        print(f"Nama kampus valid? {'Ya' if Kampus.validasi_nama(kampus_obj.nama) else 'Tidak'}")

    @staticmethod
    def validasi_nama(nama):
        return not any(char.isdigit() for char in nama)


print("=== Input Data Kampus ===")
while True:
    nama_kampus = input("Nama Kampus: ")
    if Kampus.validasi_nama(nama_kampus):
        break
    else:
        print(" Nama kampus tidak boleh mengandung angka!")

alamat_kampus = input("Alamat Kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)


daftar_matkul = []
print("\n=== Input Data Mata Kuliah (minimal 8) ==")
jumlah_mk = int(input("Berapa mata kuliah yang ingin dimasukkan? "))
while jumlah_mk < 8:
    print(" Minimal harus 8 mata kuliah.")
    jumlah_mk = int(input("Berapa mata kuliah yang ingin dimasukkan? "))

for i in range(jumlah_mk):
    print(f"\nMata Kuliah ke-{i+1}")
    kode = input("Kode: ")
    nama = input("Nama: ")
    while True:
        try:
            sks = int(input("SKS (2 atau 3): "))
            mk = MataKuliah(kode, nama, sks)
            daftar_matkul.append(mk)
            break
        except ValueError as e:
            print(e)

daftar_mahasiswa = []
print("\n=== Input Data Mahasiswa (minimal 6) ===")
jumlah_mhs = int(input("Berapa mahasiswa yang ingin dimasukkan? "))
while jumlah_mhs < 6:
    print(" Minimal harus 6 mahasiswa.")
    jumlah_mhs = int(input("Berapa mahasiswa yang ingin dimasukkan? "))

for i in range(jumlah_mhs):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    while True:
        nim = input("NIM : ")
        if Mahasiswa.validasi_nim(nim):
            break
        else:
            print(" NIM tidak valid! Harus mulai dengan '23' dan 10 digit.")

    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)

    
    print(f"\nPilih minimal 4 mata kuliah untuk {nama}:")
    for idx, mk in enumerate(daftar_matkul):
        print(f"{idx+1}. {mk}")
    jumlah_ambil = int(input("Berapa mata kuliah yang diambil? (minimal 4): "))
    while jumlah_ambil < 4:
        print(" Minimal 4 mata kuliah.")
        jumlah_ambil = int(input("Berapa mata kuliah yang diambil? "))

    for j in range(jumlah_ambil):
        while True:
            pilih = int(input(f"Masukkan nomor mata kuliah ke-{j+1}: "))
            if 1 < pilih <= len(daftar_matkul):
                mhs.tambah_matkul(daftar_matkul[pilih-1])
                break
            else:
                print(" Nomor tidak valid.")
    daftar_mahasiswa.append(mhs)


print("\n DATA MAHASISWA ")
for mhs in daftar_mahasiswa:
    mhs.tampilkan_biodata()


Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa
Kampus.tampilkan_info_kampus(kampus)
