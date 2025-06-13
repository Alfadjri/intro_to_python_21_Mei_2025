class Ibu:
    panggilan = "Ini punya kelas ibu"
    _sifat = "Pengayom"
    def memanggil(self):
        print("Iya, Ada Apa ?")
    
    def setSifat(self,sifat):
        self._sifat = sifat
    
    def getSifat(self):
        print(f"Memiliki sifat {self._sifat}")
        

class Anak(Ibu): #ini di sebutnya Inheritace atau pewarisan sifat
    def suruh(self):
        print("Nanti dulu deh !!!!")



toni = Anak()
toni.panggilan = "Ton Ton!!!"
print(f"Panggilan dari Toni : {toni.panggilan}")
toni.getSifat()