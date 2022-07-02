print('== Polymorphism Inheritance ==')
class Bird:
    def intro(self):
        print('There are many types of birds')
    def flight(self):
        print('Most of the birds can fly but some cannot')
class Sparrow(Bird):
    def flight(self):
        print('Sparrows can fly')
class Ostrich(Bird):
    def flight(self):
        print('Ostriches cannot fly')

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_ostrich.intro()
obj_ostrich.flight()

print('=== Polymorphism class ===')
class Kucing:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def bersuara(self):
        print('Meow')
class Dog:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def bersuara(self):
        print('Guk..Guk')

kucing = Kucing('Tom',3)
anjing = Dog('Spike',4)
for hewan in (kucing,anjing):
    hewan.bersuara()