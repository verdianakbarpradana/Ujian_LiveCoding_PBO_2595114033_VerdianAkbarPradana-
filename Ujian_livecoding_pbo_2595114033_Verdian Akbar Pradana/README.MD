Kasus 1 — Sistem Kasir Minimarket
Deskripsi
Program kasir minimarket untuk menghitung subtotal belanja, menentukan diskon berdasarkan subtotal, menghitung potongan, dan menampilkan struk pembayaran.
Tujuan
Menghitung subtotal berdasarkan harga satuan dan jumlah barang.
Menentukan diskon secara otomatis.
Menghitung total pembayaran.
Menerapkan konsep Pemrograman Berorientasi Objek (PBO).
Aturan Diskon
Subtotal	Diskon
Rp500.000 atau lebih	15%
Rp250.000 sampai kurang dari Rp500.000	10%
Rp100.000 sampai kurang dari Rp250.000	5%
Kurang dari Rp100.000	0%


Konsep PBO
Class: TransaksiKasir
Objek: transaksi
Atribut: pelanggan, barang, harga satuan, dan jumlah
Konstruktor: __init__()
Method: menghitung subtotal, menentukan diskon, menghitung potongan, menghitung total, dan menampilkan struk
Enkapsulasi: harga satuan dan jumlah disimpan sebagai atribut privat
Validasi: harga satuan dan jumlah harus lebih dari nol
Persyaratan
Python 3.x
Tidak memerlukan library tambahan
Struktur Folder
kasus-1-kasir/
├── kasus_1_kasir.py
└── README.md
Cara Menjalankan
python kasus_1_kasir.py
Di Windows, jika perintah tersebut tidak berjalan, coba:
py kasus_1_kasir.py
Contoh Input
Nama pelanggan : Andi
Nama barang    : Beras 5 Kg
Harga barang   : 75000
Jumlah barang  : 4
Contoh Output
=== STRUK PEMBAYARAN ===
Pelanggan      : Andi
Barang         : Beras 5 Kg
Subtotal       : Rp300.000
Diskon         : 10%
Potongan       : Rp30.000
Total bayar    : Rp270.000
==========================
Kesimpulan
Program ini membantu menghitung pembayaran belanja dan diskon dengan otomatis. Struktur class dan method membuat kode lebih terorganisasi serta mudah dikembangkan.


Kasus 3 — Sistem Parkir Otomatis
Deskripsi
Program untuk menghitung biaya parkir kendaraan berdasarkan jenis kendaraan dan durasi parkir, lalu menampilkan tiket pembayaran.
Tarif Parkir
Kendaraan	Jam Pertama	Setiap Jam Berikutnya
Motor	Rp2.000	Rp1.000
Mobil	Rp5.000	Rp3.000


Untuk durasi lebih dari 5 jam, dikenakan biaya tambahan Rp5.000. Durasi parkir harus berupa bilangan bulat dari 1 sampai 24 jam.
Konsep PBO
Class: TiketParkir
Objek: tiket
Atribut: nomor polisi, jenis kendaraan, dan durasi
Konstruktor: __init__()
Method: menghitung tarif jam pertama, jam tambahan, biaya tambahan, total biaya, dan menampilkan tiket
Percabangan: memilih tarif sesuai jenis kendaraan dan durasi
Validasi: jenis kendaraan hanya Motor atau Mobil; durasi 1–24 jam
Persyaratan
Python 3.x
Tidak memerlukan library tambahan
Struktur Folder
kasus-3-parkir/
├── kasus_3_parkir.py
└── README.md
Cara Menjalankan
python kasus_3_parkir.py
Alternatif pada Windows:
py kasus_3_parkir.py
Contoh Input
Nomor polisi      : B 1234 CD
Jenis kendaraan   : Mobil
Durasi parkir     : 7
Contoh Output
=== TIKET PARKIR ===
Nomor polisi      : B 1234 CD
Jenis kendaraan   : Mobil
Durasi            : 7 jam
Jam pertama       : Rp5.000
Jam tambahan      : Rp18.000
Biaya tambahan    : Rp5.000
Total parkir      : Rp28.000
========================
Perhitungan
Jam pertama: Rp5.000
Enam jam tambahan: 6 × Rp3.000 = Rp18.000
Biaya tambahan karena durasi lebih dari 5 jam: Rp5.000
Total: Rp28.000
Kesimpulan
Program ini membantu menghitung tarif parkir secara otomatis dengan menerapkan class, method, percabangan, dan validasi input.