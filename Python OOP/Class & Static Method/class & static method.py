class Person:
    TITLES = ('Dr','Mr','Mrs','Ms')
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    @property
    def fullname(self):
        return "%s %s" % (self.name,self.surname)
    @classmethod
    def allowed_titles_starting_with(cls,startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]
    @staticmethod
    def allowed_titles_ending_with(endswith):
        return [t for t in Person.TITLES if t.endswith(endswith)]

jane = Person('Jane','Smith')
#akses properti
print("Full name : %s" % (jane.fullname))
print("Name : %s" % (jane.name))
print("Surname : %s" % (jane.surname))

#akses class method dari instance
print(jane.allowed_titles_starting_with("M"))
#akses class method dari class
print(Person.allowed_titles_starting_with("M"))

#akses static method dari instance
print(jane.allowed_titles_ending_with("s"))
#akses static class dari method
print(Person.allowed_titles_ending_with("s"))
