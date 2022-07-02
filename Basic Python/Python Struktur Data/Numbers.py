# Tipe numerik python terdiri dari int, float, complex

# int
print(int(1))
print(int(5.7))
print(int('3'))

# float
print(float(6))
print(float(4.6))
print(float('3.3'))

# complex
print(type(complex(3j)))
print(type(complex(2 + 4j)))
print(type(complex(-3j)))

# str
print(str('c5'))
print(str(9))
print(str(7.0))

x = 4         # int
y = 2.5       # float
z = 3 + 8j    # complex

# Konversi int ke float
a = float(x)
print(a)
# Konversi float ke int
b = int(y)
print(b)

# Konversi int ke complex
c = complex(x)
print(c) # Tidak dapat mengubah bilangan complex menjadi tipe bilangan lain selain int

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random
print(random.randrange(1,10)) # Menampilkan nomor acak dari nomor 1 sampai 9

