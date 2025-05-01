class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            return 7
        elif self.jenis_kendaraan == "mobil":
            return 5
        else:
            return 6


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 3
        elif self.maskapai == "AirAsia":
            return 4
        else:
            return 5


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self) if self.jenis_kendaraan else 0
        waktu_udara = PengirimanUdara.estimasi_waktu(self) if self.maskapai else 0

        base_estimasi = max(waktu_darat, waktu_udara) if (waktu_darat or waktu_udara) else super().estimasi_waktu()

        if "luar negeri" in self.tujuan.lower():
            return base_estimasi + 3
        return base_estimasi

def input_pengiriman():
    asal = input("Masukkan asal pengiriman: ")
    tujuan = input("Masukkan tujuan pengiriman: ")

    jenis_kendaraan = None
    maskapai = None

    pengiriman_jenis = input("Masukkan jenis pengiriman (Darat/Udara/Internasional): ")

    if pengiriman_jenis == "Darat":
        jenis_kendaraan = input("Masukkan jenis kendaraan (truk/mobil/lain): ")
        pengiriman = PengirimanDarat(asal, tujuan, jenis_kendaraan)

    elif pengiriman_jenis == "Udara":
        maskapai = input("Masukkan maskapai (Garuda/AirAsia/lain): ")
        pengiriman = PengirimanUdara(asal, tujuan, maskapai)

    elif pengiriman_jenis == "Internasional":
        jenis_kendaraan = input("Masukkan jenis kendaraan (truk/mobil/lain) (opsional): ")
        maskapai = input("Masukkan maskapai (Garuda/AirAsia/lain) (opsional): ")
        pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

    else:
        print("Jenis pengiriman tidak dikenali.")
        return None

    if pengiriman:
        print(f"Estimasi waktu pengiriman: {pengiriman.estimasi_waktu()} hari")

input_pengiriman()
