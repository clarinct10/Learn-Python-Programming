print('== Warisan python ==')
class Orang:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Karyawan(Orang):
    def isEmployee(self):
        return True

emp = Orang('Geek1')
print(emp.getName(), emp.isEmployee())

emp = Karyawan('Geek2')
print(emp.getName(), emp.isEmployee())

class Person:
    def __init__(self,name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self,name,idnumber,salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)

a = Employee('Barbie',20464265,200000,"Intern")
a.display()

print('==Multiple Inheritance==')
class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printStr(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStr()

print('==Multilevel Inheritance== ')
class Base:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age
    def getAge(self):
        return self.age

class Grandchild(Child):
    def __init__(self,name,age,country):
        Child.__init__(self,name,age)
        self.country = country
    def getCountry(self):
        return self.country
g = Grandchild('Eunwoo',23,'korea')
print(g.getName(), g.getAge(), g.getCountry())

print('=== Hierarchical Inheritance ===')
class Parent:
    def func1(self):
        print('This function is in parent class')
class child1(Parent):
    def func2(self):
        print('This function is in child 1')
class child2(Parent):
    def func3(self):
        print('This function is in child 2')

object1 = child1()
object2 = child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

print('=== Hybrid Inheritance ===')
class School:
    def func1(self):
        print('This function is in school')
class Student1(School):
    def func2(self):
        print('This function is in student 1')
class Student2(School):
    def func3(self):
        print('This function is in student 2')
class Student3(Student1,School):
    def func4(self):
        print('This function is in student 3')

object = Student3()
object.func1()
object.func4()
