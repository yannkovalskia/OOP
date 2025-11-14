class Penyewa:
    def __init__(self, nama_penyewa, tala, alamat, kode_unik):
        self.nama_penyewa = nama_penyewa
        self.tala = tala
        self.alamat = alamat
        self.kode_unik = kode_unik

    def __str__(self):
        return f"{self.nama_penyewa} (Lahir: {self.tala}) - {self.alamat} - Kode: {self.kode_unik}"

class Mobil:
    def __init__(self, jenis_mobil, penyewa=None, status="tersedia"):
        self.jenis_mobil = jenis_mobil
        self.penyewa = penyewa 
        self.status = status

    def __str__(self):
        penyewa_info = self.penyewa.nama_penyewa if isinstance(self.penyewa, Penyewa) else "Tidak ada"
        return f"{self.jenis_mobil} | Status: {self.status} | Penyewa: {penyewa_info}"

class Admin:
    def __init__(self, nama, alamat, no_telepon):
        self.nama = nama
        self.alamat = alamat
        self.no_telepon = no_telepon
        self.mobil_list = []
        self.penyewa_list = []

    def menambahkan(self):
        print(f"{self.nama} menambahkan {len(self.mobil_list)} mobil ke daftar rental.")

    def menampilkan(self):
        print("=== Informasi Admin ===")
        print(f"Nama : {self.nama}")
        print(f"Alamat : {self.alamat}")
        print(f"No. Telepon : {self.no_telepon}\n")

        print("=== Daftar Mobil di Rental ===")
        if not self.mobil_list:
            print("Tidak ada mobil terdaftar.")
        else:
            for idx, m in enumerate(self.mobil_list, start=1):
                print(f"{idx}. {m}")

        print("\n=== Informasi Penyewa ===")
        if not self.penyewa_list:
            print("Tidak ada penyewa terdaftar.")
        else:
            for idx, p in enumerate(self.penyewa_list, start=1):
                print(f"{idx}. {p}")
penyewa1 = Penyewa("Budi Santoso", "1954", "Palengaan", "P001")
penyewa2 = Penyewa("Siti Aminah", "1960", "Pamekasan", "P002")
penyewa3 = Penyewa("Andi Wijaya", "1970", "Sampang", "P003")
penyewa4 = Penyewa("Rina Puspita", "1980", "Bangkalan", "P004")
penyewa5 = Penyewa("Taufik Hidayat", "1990", "Sumenep", "P005")

admin1 = Admin("Vio", "jl. raya Panglegur", "087750242034")

mobil1 = Mobil("Toyota Avanza (2020)", penyewa1, "disewa")
mobil2 = Mobil("Honda Jazz (2021)", penyewa2, "disewa")
mobil3 = Mobil("Suzuki Ertiga (2019)", penyewa3, "disewa")
mobil4 = Mobil("Daihatsu Xenia (2022)", penyewa4, "disewa")
mobil5 = Mobil("Mitsubishi Pajero (2022)", penyewa5, "disewa")
admin1.mobil_list = [mobil1, mobil2, mobil3, mobil4, mobil5]
admin1.penyewa_list = [penyewa1, penyewa2, penyewa3, penyewa4, penyewa5]
admin1.menambahkan()
admin1.menampilkan()