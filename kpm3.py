class Sepeda:
    def __init__(self, merk, kecepatan):
        self.__merk = merk
        self.__kecepatan = kecepatan
    def setMerk(self, merk):
        self.__merk = merk
    def getMerk(self):
        return self.__merk
    def setKecepatan(self, kecepatan):
        self.__kecepatan = kecepatan
    def getKecepatan(self):
        return self.__kecepatan
    def __ubah_kecepatan(self, nilai):
        self.__kecepatan += nilai
    def kayuh(self, kecepatan = 5):
        self.__ubah_kecepatan(kecepatan)
        print(f"Sepeda dikayuh! kecepatan sekarang: {self.__kecepatan} km/h")
    def rem(self, kecepatan = -5):
        if self.__kecepatan > 0:
            self.__ubah_kecepatan(kecepatan)
        print(f"Rem ditekan! kecepatan sekarang: {self.__kecepatan} km/h")
    def tampil_info(self):
        print(f"Merk Sepeda: {self.__merk}, Kecepatan: {self.__kecepatan} km/h")
vio = Sepeda("Polygon", 356)
vio.kayuh()
vio.rem()
vio.tampil_info()
vio.setMerk("United")
print(f"Merk baru sepeda: {vio.getMerk()}")