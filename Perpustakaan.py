class Buku:
    def __init__(self, judul, penulis, stok):
        self.__judul = judul
        self.__penulis = penulis
        self.__stok = stok
    def kurangi_stok(self, jumlah):
        if self.__stok >= jumlah:
            self.__stok -= jumlah
            return True
        else:
            return False
    def tambah_stok(self, jumlah):
        self.__stok += jumlah
    def get_judul(self):
        return self.__judul
    def get_penulis(self):
        return self.__penulis
    def get_stok(self):
        return self.__stok
class Anggota:
    def __init__(self, nama, id_anggota, batas_pinjam, buku_dipinjam):
        self.__nama = nama
        self.__id_anggota = id_anggota
        self.__batas_pinjam = batas_pinjam
        self.__buku_dipinjam = buku_dipinjam
    def get_nama(self):
        return self.__nama
    def get_id_anggota(self):
        return self.__id_anggota
    def get_batas_pinjam(self):
        return self.__batas_pinjam
    def get_buku_dipinjam(self):
        return self.__buku_dipinjam
    def pinjam_buku(self, buku, jumlah):
        if self.__buku_dipinjam + jumlah <= self.__batas_pinjam:
            if buku.kurangi_stok(jumlah):
                self.__buku_dipinjam += jumlah
                print(f"{jumlah} buku '{buku.get_judul()}' berhasil dipinjam.")
            else:
                print(f"Stok buku '{buku.get_judul()}' tidak cukup.")
        else:
            print("Batas pinjam buku terlampaui.")
    def kembalikan_buku(self, buku, jumlah):
        if self.__buku_dipinjam >= jumlah:
            buku.tambah_stok(jumlah)
            self.__buku_dipinjam -= jumlah
            print(f"{jumlah} buku '{buku.get_judul()}' berhasil dikembalikan.")
        else:
            print("Jumlah buku yang dikembalikan melebihi jumlah yang dipinjam.")
class Peminjaman:
    def periksa_stok(self, buku):
        if buku.get_stok() > 0:
            print(f"Buku '{buku.get_judul()}' tersedia dengan stok {buku.get_stok()}.")
        else:
            print(f"Buku '{buku.get_judul()}' tidak tersedia.")
    def periksa_batas_pinjam(self, anggota):
        if anggota.get_buku_dipinjam() < anggota.get_batas_pinjam():
            print(f"Anggota '{anggota.get_nama()}' masih bisa meminjam buku.")
        else:
            print(f"Anggota '{anggota.get_nama()}' sudah mencapai batas pinjam buku.")
    def kurangi_stok_buku(self, buku, jumlah):
        if buku.kurangi_stok(jumlah):
            print(f"Stok buku '{buku.get_judul()}' berhasil dikurangi sebanyak {jumlah}.")
        else:
            print(f"Stok buku '{buku.get_judul()}' tidak cukup untuk mengurangi {jumlah}.")
    def tambah_jumlah_pinjam(self, anggota, jumlah):
        if anggota.get_buku_dipinjam() + jumlah <= anggota.get_batas_pinjam():
            anggota._Anggota__buku_dipinjam += jumlah
            print(f"Jumlah buku yang dipinjam oleh anggota '{anggota.get_nama()}' berhasil ditambah sebanyak {jumlah}.")
        else:
            print(f"Penambahan jumlah pinjam melebihi batas untuk anggota '{anggota.get_nama()}'.")
    def info_peminjaman_berhasil(self, anggota, buku, jumlah):
        print(f"Anggota '{anggota.get_nama()}' berhasil meminjam {jumlah} buku '{buku.get_judul()}'.")
    def stok_setelah_peminjaman(self, buku, jumlah):
        print(f"Stok buku '{buku.get_judul()}' setelah peminjaman: {buku.get_stok() - jumlah}")
class Petugas:
    def isi_stok_buku(self, buku, jumlah):
        stok_sebelum = buku.get_stok()
        buku.tambah_stok(jumlah)
        stok_setelah = buku.get_stok()
        print(f"Stok buku '{buku.get_judul()}' berhasil ditambah dari {stok_sebelum} menjadi {stok_setelah}.")

# Membuat beberapa objek buku
buku1 = Buku("Python Programming", "John Doe", 10)
buku2 = Buku("Data Science", "Jane Smith", 10)
buku3 = Buku("Machine Learning", "Alice Johnson", 10)

# Membuat beberapa anggota
anggota1 = Anggota("Budi", "A001", 3, 0)
anggota2 = Anggota("Siti", "A002", 2, 1)
anggota3 = Anggota("Andi", "A003", 4, 2)

# Menampilkan stok awal
print("=== Stok Awal Buku ===")
for buku in [buku1, buku2, buku3]:
    print(f"Buku: {buku.get_judul()}, Stok: {buku.get_stok()}")

# Melakukan 2-3 kali proses peminjaman
print("\n=== Proses Peminjaman ===")
anggota1.pinjam_buku(buku1, 2)  # Budi pinjam 2 buku1
anggota2.pinjam_buku(buku2, 1)  # Siti pinjam 1 buku2
anggota3.pinjam_buku(buku3, 2)  # Andi pinjam 2 buku3

# Menampilkan stok setelah peminjaman
print("\n=== Stok Setelah Peminjaman ===")
for buku in [buku1, buku2, buku3]:
    print(f"Buku: {buku.get_judul()}, Stok: {buku.get_stok()}")

# Petugas menambah stok
petugas = Petugas()
print("\n=== Petugas Menambah Stok ===")
petugas.isi_stok_buku(buku1, 4)
petugas.isi_stok_buku(buku2, 3)
petugas.isi_stok_buku(buku3, 2)

# Menampilkan kondisi akhir
print("\n=== Data Setelah Peminjaman dan Pengisian Stok ===")
for buku in [buku1, buku2, buku3]:
    print(f"Buku: {buku.get_judul()}, Stok: {buku.get_stok()}")