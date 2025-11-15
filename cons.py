class PersegiPanjang:
    def __init__(self, panjang=0, lebar=0):
        self.panjang = panjang
        self.lebar = lebar
        print("Objek persegi panjang dibuat: ")
    def __del__(self):
        print("Objek persegi panjang dihapus")
    def hitung_luas(self, *args):
        if len(args) == 0:
            hasil = self.panjang * self.lebar
            print(f"Menggunakan atribut objek: {self.panjang} x {self.lebar} = {hasil}")
            return hasil
        elif len(args) == 1:
            sisi = args[0]
            hasil = sisi * sisi
            print(f"Menghitung luas persegi: {sisi} x {sisi} = {hasil}")
            return hasil
        elif len(args) == 2:
            panjang, lebar = args
            hasil = panjang * lebar
            print(f"Menghitung luas persegi panjang: {panjang} x {lebar} = {hasil}")
            return hasil
        else:
            print("Error: terlalu banyak argumen")
            return None
objl = PersegiPanjang(4, 5)
print("\nLuas default:", objl.hitung_luas())
print("\nluas persegi:", objl.hitung_luas(6))
print("\nLuas persegi panjang:", objl.hitung_luas(6, 7))
del objl