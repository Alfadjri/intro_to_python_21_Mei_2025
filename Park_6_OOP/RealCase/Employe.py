from Person import Person

class Employe(Person):
    def __init__(self, nama, umur,divisi,gaji):
        super().__init__(nama, umur)
        self._divisi = divisi
        self.__gaji = gaji
    
    def get_Gaji(self):
        return self.__gaji 
    
    def getDetail(self):
        return f"Employe : {self._nama}\nAge:{self.get_umur()}\nJob:{self._divisi}\nGaji:{self.__gaji}\nini yang punya Empolyeeee"
    
    def work(self):
        return f"{self._nama} dia bekerja sebagai divisi {self._divisi}"