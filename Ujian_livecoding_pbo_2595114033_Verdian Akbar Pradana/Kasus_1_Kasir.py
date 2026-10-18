class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga_satuan, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang

        # Validasi harga dan jumlah harus positif
        if harga_satuan <= 0:
            raise ValueError("Harga satuan harus lebih dari 0!")

        if jumlah <= 0:
            raise ValueError("Jumlah barang harus lebih dari 0!")

        self.__harga_satuan = harga_satuan
        self.__jumlah = jumlah

    # Method menghitung subtotal
    def hitung_subtotal(self):
        return self.__harga_satuan * self.__jumlah

    # Method menentukan diskon
    def tentukan_diskon(self):
        subtotal = self.hitung_subtotal()

        if subtotal >= 500000:
            return 15
        elif subtotal >= 250000:
            return 10
        elif subtotal >= 100000:
            return 5
        else:
            return 0

    # Method menghitung potongan harga
    def hitung_potongan(self):
        subtotal = self.hitung_subtotal()
        diskon = self.tentukan_diskon()
        return subtotal * diskon / 100

    # Method menghitung total pembayaran
    def hitung_total(self):
        return self.hitung_subtotal() - self.hitung_potongan()

    # Method menampilkan struk pembayaran
    def tampilkan_struk(self):
        print("\n=== STRUK PEMBAYARAN ===")
        print(f"Pelanggan      : {self.pelanggan}")
        print(f"Barang         : {self.barang}")
        print(f"Subtotal       : Rp{self.hitung_subtotal():,.0f}".replace(",", "."))
        print(f"Diskon         : {self.tentukan_diskon()}%")
        print(f"Potongan       : Rp{self.hitung_potongan():,.0f}".replace(",", "."))
        print(f"Total bayar    : Rp{self.hitung_total():,.0f}".replace(",", "."))
        print("==========================")


# Program utama
print("=== KASIR MINIMARKET ===")

pelanggan = input("Nama pelanggan : ")
barang = input("Nama barang    : ")

try:
    harga_satuan = int(input("Harga barang   : "))
    jumlah = int(input("Jumlah barang  : "))

    transaksi = TransaksiKasir(
        pelanggan, barang, harga_satuan, jumlah
    )

    transaksi.tampilkan_struk()

except ValueError as e:
    print("Input tidak valid:", e)


                       
          


