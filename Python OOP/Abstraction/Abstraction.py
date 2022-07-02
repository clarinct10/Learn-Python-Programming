print('== Abstraction ==')
#abstraksi berfungsi untuk menyembunyikan detail komplek dari pengguna
from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print('I have 3 sides')
class Pentagon(Polygon):
    def noofsides(self):
        print('I have 5 sides')
R =  Triangle()
R.noofsides()
p = Pentagon()
p.noofsides()


import abc
class Shapes(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass
class Rectangle(Shapes):
      def __init__(self,x,y):
          self.x = x
          self.y = y
      def area(self):
          return self.x * self.y

r = Rectangle(10,20)
print(r.area())

from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi
    @abstractmethod
    def keliling(self):
        return 4 * self.__sisi

class Persegi(Bentuk):
    def __init__(self,sisi):
        self.__sisi = sisi
    def luas(self):
        return self.__sisi*self.__sisi
    def keliling(self):
        return 4 * self.__sisi

persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())

import abc
class parent:
    def geeks(self):
        pass
class child(parent):
    def geeks(self):
        print("child class")

print(issubclass(child,parent)) #Issubclass untuk mengecek class child apakah subclass dari parent
print(isinstance(child(),parent)) #Isinstance untuk mengecek tipe dari object dan mengecek instansiasi dari child pada parent
