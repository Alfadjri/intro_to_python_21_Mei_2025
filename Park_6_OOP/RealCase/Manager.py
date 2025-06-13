from Employe import Employe

class Manager(Employe):
    def __init__(self, nama, umur,divisi,gaji,jumlah_tim = 0):
        super().__init__(nama, umur,divisi,gaji)
        self._jumlah_tim = jumlah_tim

    def getDetail(self):
        if(self._jumlah_tim == 0):
            return super().getDetail()
        
        return f"Employe : {self._nama}\nAge:{self.get_umur()}\nJob:{self._divisi}\nGaji:{self.get_Gaji()}\nJumlah tim : {self._jumlah_tim}"
    
    def work(self):
        if(self._jumlah_tim == 0):
            return super().work()
        
        return f"{self._nama} dia bekerja sebagai divisi {self._divisi} dengan jumlah tim {self._jumlah_tim}"