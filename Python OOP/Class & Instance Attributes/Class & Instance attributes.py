# instance attribute adalah atribut instan yang didefinisikan di dalam konstruktor (__init__).
# class attribute adalah atribut kelas yang didefinisikan di luar konstruktor (__init__).
class Person:
    TITLES = ('Dr','Mr','Mrs','Ms')#class attributes

    def __init__(self,title,name,surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." %title)
        self.title = title
        self.name = name
        self.surname = surname
#instansiasi
p = Person('Dr','leo','R')
#mengakses kelas attributes dari instance
print(p.TITLES)
#mengakses class attributes dari class
print(Person.TITLES)
#mengakses instance attributes dari instance
print(p.title)
print(p.name)
print(p.surname)
#mengakses instance attributes dari class
#print(Person.name)

print('==class attributes immutable==')
class Person:
    sehat = False
    def dinyatakan_sehat(self):
        self.sehat = True
#immutable = tetap
joni = Person()
eko = Person()
joni.dinyatakan_sehat()
print('Joni sehat : ' ,joni.sehat)
print('Eko sehat : ',eko.sehat)

print('<=--class attributes muttable--=>')
class Orang:
    pets = [] #tipe data yang muttable
#muttable  = tidak tetap
    def add_pet(self,pet):
        self.pets.append(pet)

joni = Orang()
eko = Orang()
joni.add_pet('Kucing')
print(joni.pets)
print(eko.pets)

# Agar tipe data joni dan eko berbeda maka class attribute di ubah menjadi instance attributes
print()
class Orang:
    def __init__(self):
        self.pets = [] #pets sebagai instance attributes
    def add_pet(self,pet):
        self.pets.append(pet)
joni = Orang()
eko = Orang()
joni.add_pet('Kucing')
print(joni.pets)
print(eko.pets)

class Orang:
    TITLES = ('Dr','Mr','Mrs','Ms') #class attributes
    #menggunakan nama class attribute sebagai variable dalam definisi
    def __init__(self,title,name,surname,allowed_titles = TITLES):
        if title not in allowed_titles:
            raise ValueError('%s is not a valid title.' %title)
        self.title = title
        self.name = name
        self.surname = surname

p = Orang('Dr','leo','R')
print("%s %s %s" % (p.title,p.name,p.surname))
