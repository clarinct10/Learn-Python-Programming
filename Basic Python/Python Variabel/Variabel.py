# Unpack a Collection
a,s,d = ['pandas','numpy','matplotlib']
print(a)
print(s)
print(d)

language = ['Python','golang','Ruby']
a,s,d =  language
print(a)
print(s)
print(d)

# One Value to Multiple Variables
a = k = u = 'aku'
print(a)
print(k)
print(u)


# Output Variables
x = 'buku'
print('saya suka baca ' + x)

x = 'saya suka baca '
y = 'komik'
z = x + y
print(z)

x = 10
y = 11
print(x+y)

# Global Variables
x = 'Python'
def language():
    x = 'Sql'
    print('saya belajar ' + x)
language()

print('saya belajar '+ x)

def language():
     global x
     x = 'Python'
language()
print(x)

# Python Comments
print('Hello world') # This is comment

# Multi Line Comments
'''
Python adalah bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. 
Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, 
filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan.
'''
print('Hello world')

