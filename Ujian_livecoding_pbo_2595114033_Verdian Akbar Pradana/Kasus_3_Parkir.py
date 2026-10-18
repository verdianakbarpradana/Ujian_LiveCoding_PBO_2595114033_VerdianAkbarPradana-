class TiketParkir:
    def __init__(self, nomor_polisi, jenis_kendaraan, durasi):
        self.nomor_polisi = nomor_polisi
        self.jenis_kendaraan = jenis_kendaraan.capitalize()
        self.durasi = durasi

        # Validasi jenis kendaraan
        if self.jenis_kendaraan not in ["Motor", "Mobil"]:
            raise ValueError("Jenis kendaraan harus Motor atau Mobil!")

        # Validasi durasi parkir
        if durasi < 1 or durasi > 24:
            raise ValueError("Durasi parkir harus 1 sampai 24 jam!")

    # Method menghitung tarif jam pertama
    def hitung_jam_pertama(self):
        if self.jenis_kendaraan == "Motor":
            return 2000
        else:
            return 5000

    # Method menghitung tarif jam tambahan
    def hitung_jam_tambahan(self):
        if self.jenis_kendaraan == "Motor":
            tarif_tambahan = 1000
        else:
            tarif_tambahan = 3000

        return (self.durasi - 1) * tarif_tambahan

    # Method menghitung biaya tambahan jika lebih dari 5 jam
    def hitung_biaya_tambahan(self):
        if self.durasi > 5:
            return 5000
        else:
            return 0

    # Method menghitung total biaya parkir
    def hitung_total(self):
        return (
            self.hitung_jam_pertama()
            + self.hitung_jam_tambahan()
            + self.hitung_biaya_tambahan()
        )

    # Method menampilkan tiket parkir
    def tampilkan_tiket(self):
        print("\n=== TIKET PARKIR ===")
        print(f"Nomor polisi      : {self.nomor_polisi}")
        print(f"Jenis kendaraan   : {self.jenis_kendaraan}")
        print(f"Durasi            : {self.durasi} jam")
        print(f"Jam pertama       : Rp{self.hitung_jam_pertama():,}".replace(",", "."))
        print(f"Jam tambahan      : Rp{self.hitung_jam_tambahan():,}".replace(",", "."))
        print(f"Biaya tambahan    : Rp{self.hitung_biaya_tambahan():,}".replace(",", "."))
        print(f"Total parkir      : Rp{self.hitung_total():,}".replace(",", "."))
        print("========================")


# Program utama
print("=== SISTEM PARKIR ===")

nomor_polisi = input("Nomor polisi      : ")
jenis_kendaraan = input("Jenis kendaraan   : ")

try:
    durasi = int(input("Durasi parkir     : "))

    tiket = TiketParkir(
        nomor_polisi,
        jenis_kendaraan,
        durasi
    )

    tiket.tampilkan_tiket()

except ValueError as e:
    print("Input tidak valid:", e)