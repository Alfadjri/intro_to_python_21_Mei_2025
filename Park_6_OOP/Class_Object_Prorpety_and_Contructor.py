# case mobil

class Mobil: # Mobil merukan class atau cetak birunya
    #instansiace menyiapkan komputer atau object yang akan di pakai
    roda = 4 # ini di sebut object roda dengan property(Sifat) public
    _merek = None # ini di sebut obejct merek dengan property(Sifat) private sibol (_)
    __seris = None # ini di sebut object seris dengan property(Sifat) protected simbo (_ _)
    
    def __init__(self,warna,merek = None,seris = None ): #ini di sebut consturctor
        self._merek = merek
        self.__seris = seris
        self.waran = warna
        
    
    def getDetail(self): #method
        print(f"Merek mobil : {self._merek}")
        print(f"Seris Mobil : {self.__seris}")
        print(f"Warna Mobil : {self.waran}")
    
# Cara memanggil 
supra = Mobil("Hitam","Toyota","Supra") #ini cara memanggil class dengan constructor
civic = Mobil("Biru","Honda","Civic Turbo")

print(f"Berapa jumlah ban : {supra.roda}") # memanggil object dengan propery public
# cara memanggil metode
supra.getDetail() #cara memanggil methode