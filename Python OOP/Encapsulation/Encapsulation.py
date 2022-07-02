print('==Encapsulation==')
class B:
    def __init__(self):
        self._a = 2
class D(B):
    def __init__(self):
        B.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)

obj1 = D()

print()
class Pekerja:
    def __init__(self):
        self.a = "Happy"
        self.__c = "Sad"
class Kantor(Pekerja):
    def __init__(self):
        Pekerja.__init__(self)
        print('Calling private member of base class : ')
        print(self.__c)

obj = Pekerja()
print(obj.a)

class car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving.maxspeed' + str(self.__maxspeed))

    def setMaxspeed(self,speed):
        self.__maxspeed = speed

red = car()
red.drive()
red.__maxspeed = 10
red.drive()
red.setMaxspeed(320)
red.drive()

print('=== Encapsulation protected members ===')
#protected members menggunakkan '_' underscore tunggal
class Person:
    def __init__(self,name, age=0):
        self.name = name
        self._age = age
    def display(self):
        print(self.name)
        print(self._age)

person = Person('Lea',8)
person.display()
print(person.name)
print(person._age)

print('=== Encapsulation private members ===')
class Person:
    def __init__(self,name, age=0):
        self.name = name
        self.__age = age
    def display(self):
        print(self.name)
        print(self.__age)

person = Person('Leo',8)
person.display()
print(person.name)
#print(person.__age) akan menampilkan error

