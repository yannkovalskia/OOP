class Persegipanjang:
    def __init__(self, panjang=0, lebar=0):
        self.panjang = panjang
        self.lebar = lebar
        print("Objek Persegipanjang telah dibuat")
    def __del__(self):
        print("Objek Persegipanjang telah dihapus")
    def hitung_luas(self, *args):
        if len(args) == 0:
               hasil = self.panjang * self.lebar
               print(f"menggunakan atribut {self.panjang} * {self.lebar} = {hasil}")
               return hasil
        elif len(args) == 1:
                sisi = args[0]
                hasil = sisi * sisi
                print(f"menghitung luas persegi {sisi} * {sisi} = {hasil}")
                return hasil
        elif len(args) == 2:
                panjang, lebar = args
                hasil = panjang * lebar
                print(f"menghitung luas persegi panjang {panjang} * {lebar} = {hasil}")
                return hasil
        else:
              print("Error: Jumlah argumen tidak valid")
              return None
objl1 = Persegipanjang(4, 5)
print("Luas dengan atribut:", objl1.hitung_luas())
print("Luas dengan 1 argumen:", objl1.hitung_luas(6))
print("Luas dengan 2 argumen:", objl1.hitung_luas(3, 7))
del objl1