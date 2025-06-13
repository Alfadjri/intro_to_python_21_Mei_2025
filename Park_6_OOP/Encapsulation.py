# case mobil

class Mobil: 
    roda = 4
    _merek = None  #ini yang di sebut encapsulation teknik penyembunyian nilai
    __seris = None 
    
    def __init__(self,warna,merek = None,seris = None ): #ini di sebut consturctor
        self._merek = merek
        self.__seris = seris
        self.waran = warna
        
    
    def getDetail(self): #method
        print(f"Merek mobil : {self._merek}")
        print(f"Seris Mobil : {self.__seris}")
        print(f"Warna Mobil : {self.waran}")
    
    # Set and Get
    # Set ini di gunakan untuk merubah nilai yang sudah ada 
    # Get ini di gunakan untuk mengambil nilai yang mau di tampilkan
    def getMerek(self):
        return self._merek + " Mobilnya kencang !"
    def setMerek(self,merek):
        self._merek = merek
        
# Cara memanggil 
supra = Mobil("Hitam","Toyota","Supra")
civic = Mobil("Biru","Honda","Civic Turbo")

merek = supra.getMerek()
print(f"ini merek mobil : {merek}")
# update nilainya
supra.setMerek("Honda")
merek = supra.getMerek()
print(f"ini merek mobil setelah di update : {merek}")
