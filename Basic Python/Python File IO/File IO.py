print('== Python read file ==')
f = open('document.txt','r')
print(f.read())

#Hanya membaca 5 karakter dari file
f = open('document.txt','r')
print(f.read(5))

f = open('document.txt','r')
print(f.readline())
print(f.readline())

print()
f = open('document.txt','r')
for x in f:
    print(x)

f = open('document.txt','r')
print(f.readline())
f.close() # close() method

print('==Python file write ==')
f = open('document.txt','a')
f.write('Now the file has more contents!')
f.close()

#open and read file
f = open('document.txt','r')
print(f.read())
print()

a = open('document2.txt','w')
a.write('Woops, I have deleted the content!')
a.close()

a = open('document2.txt','r')
print(a.read())

l = open('document2.txt','wb')
print(l.name)
print(l.closed)
print(l.mode)

print('== The Input Function ==')
xx = input('Hobi : ')
print('Hobi : ' + xx)

QQ = input('Masukkan data : ')
print('Hasil : ' + QQ)

import os





