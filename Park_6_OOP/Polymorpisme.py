from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def suara(self):
        print("INI punya class Animal")

class Kucing(Animal):
    def suara(self):
        print("Meow !!!!")
class Dog(Animal):
    def suara(self):
        print("Wofffff !!!!")
class Tikus(Animal):
    def suara(self):
        print("Cit !!!!")
        

def suara(Animal): #polymorpisme
    Animal.suara()

# Cara manggil
Tom = Kucing()
Spike = Dog()
Jeri = Tikus()


suara(Jeri)