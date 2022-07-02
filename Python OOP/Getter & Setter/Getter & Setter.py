print('=== getter dan setter ===')
#jika ingin mengubah dan mengakses variabel privat maka dapat menggunakan metode pengakses (getter) dan metode penyetel (setter) karna keduanya bagian dari kelas
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
    def display(self):
        print(self.name)
        print(self.__age)
    def getAge(self):
        print(self.__age)
    def setAge(self,age):
        self.__age = age

person = Person('V',10)
person.display()
person.setAge(9)
person.getAge()
