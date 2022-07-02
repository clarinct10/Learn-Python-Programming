print('== python classes ==')
class Myclass:
    x = 5
print(Myclass)

# Create Objects
p1 = Myclass()
print(p1.x)

#__init__ function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person('felicia', 20)
print(p1.name)
print(p1.age)

# Object Methods
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('Dia bernama ' + self.name)
p1 = person('Ayu',30)
# Mengubah age
p1.age = 45
print(p1.age)
p1.myfunc()

# Delete Objects
del p1
#print(p1)

# Pass statement
class belajar:
    pass

print('=== Python Inheritance ===')
#Membuat class induk
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)
#Membuat class turunan/ derived class
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname) #untuk mempertahankan fungsi class induk
j1 = Student('Deren','Oh')
j1.printname()

print('=== Fungsi super ===')
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)
#membuat class turunan/ derived class
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname) #untuk mempertahankan fungsi class induk
        self.graduationyear = year
    def welcome(self):
        print('Welcome', self.fname, self.lname, 'to the class of ', self.graduationyear)
j1 = Student('Deren','Oh',2021)
j1.printname()
print(j1.graduationyear)
j1.welcome()


class Animals:
    atr1 = 'bird'
    atr2 = 'cat'

    def fun(self):
        print("I like " , self.atr1)
        print("I dont like " , self.atr2)

hey = Animals()
print(hey.atr1)
hey.fun()

class Person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is ',self.name)

v = Person('Chaerin')
v.say_hi()

print()

#Variabel kelas dan instance
class Dog:
    animal = 'dog'

    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

rodger = Dog('Pug','brown')
buzo  = Dog('Bulldog','black')

print('rodger is a ', rodger.animal)
print('breed : ', rodger.breed)
print('color ', rodger.color)

print('buzo is a ', buzo.animal)
print('breed : ', buzo.breed)
print('color : ',buzo.color)
print(Dog.animal)

class Dog:
    animal = 'dog'

    def __init__(self,breed):
        self.breed = breed
    def setColor(self, color):
        self.color = color
    def getcolor(self):
        return self.color

Rodger = Dog('Pug')
Rodger.setColor('brown')
print(Rodger.getcolor())