from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def suara(self):
        print("INI punya class Animal")

class Kucing(Animal):
    def suara(self):
        print("Mbeeeee !!!!")
        


# animal = Animal()
animal = Kucing()
animal.suara()