print("animals")
print('animals')

# Menetapkan string ke variabel
a = "cat"
print(a)

# Multi line String
b = """
    Python adalah bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. 
    Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, 
    filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan.
    """
print(b)

# String arrays
a = 'Welcome to my world!'
print(a[4])

# Looping String
for x in "banana":
    print(x)

# String Length
x = 'welcome to my world!!'
print(len(x))

# Check String (in & not in)
atribut = "The best things in life are free "
print('best' in atribut)

if 'best' in atribut:
    print('OK')

print('I' not in atribut)

if 'I' not in atribut:
    print('marvelous')

# Slicing String
print('==  Slicing String  ==')
name = 'a whole new world'
print(name[4:11])
print(name[:5])
print(name[4:])
print(name[-7:-1])

# Upper dan lower case
bunga = 'SaKurA'
print(bunga.upper())
print(bunga.lower())

# Remove Whitespace
bunga = '  Lavender '
print(bunga.strip())

# Replace
bunga = 'Lavender'
print(bunga.replace('v','b'))

# Split (mengembalikan string menjadi list , memisahkan string menjadi substring jika ditemukan pemisah yaitu spasi)
z = 'Clarin, Celsia'
print(z.split(','))

# String Concatenation
print('== String Concatenation==')
l = 'Telepon'
j = 'Seluler'
k = l + j
print(k)
print(l + ' ' + j)

# String Format
print('== String Format==')
age = 18
txt = 'Saya xx dan umur saya {}'
print(txt.format(age))

apel = 30000
jeruk = 10000
sirsak = 45000
text = "Saya membeli apel Rp. {}, jeruk Rp.{}, sirsak Rp.{}"
print(text.format(apel,jeruk,sirsak))

# Escape Characters
note = "we can learn so fast when you \"focus\" on pathway"
note1 = "Just \byou know about yourself"
note2 = "Just \t you know about yourself"
note3 = "Just you know \r about yourself"
print(note)
print(note1)
print(note2)
print(note3)



