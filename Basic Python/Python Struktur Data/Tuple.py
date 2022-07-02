# Update Tuple
L = ("apple", "banana", "cherry")
y = list(L)
y[1] = "kiwi"
L = tuple(y)
print(L)

thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("grape")
thistuple = tuple(z)
print(thistuple)

variabel = ("apple", "banana", "cherry")
c = list(variabel)
c.remove('banana')
variabel = tuple(c)
print(variabel)

nama = ('ayu','vivi','ayu','jaja')
print(nama)

# Access Tuple Items
tuple = ('aku','kamu','dia')
print(tuple[1])
print(tuple[-2])

print(nama[1:3])
print(nama[:3])
print(nama[1:])
print(nama[-4:-1])

# Check Items
fruit = ('apel','mangga','jeruk','semangka')
if 'mangga' in fruit:
    print('it is mangga')

print('=== Unpacking ===')
fruits = ('Apel','Pisang','Ceri')
(Hijau,Kuning,Merah) = fruits
print(Hijau)
print(Kuning)
print(Merah)

print('=== Using Aterisk ===')
fruit1 = ('mango','banana','cherry','apple','strawberry')
(hijau,kuning,*merah) = fruit1
print(hijau)
print(kuning)
print(merah)

print('')
fruit2 = ('apple','mango','papaya','pineapple','cherry')
(green, *tropic, red) = fruit2
print(green)
print(tropic)
print(red)

print('Loop Tuple')
fruit1 = ('mango','banana','cherry','apple','strawberry')
for x in fruit1:
    print(x)

print('')
for c in range(len(fruit1)):
    print(fruit1[c])

print('== While Loop ==')
i = 0
while i < len(fruit1):
    print(fruit1[i])
    i = i + 1

print('=== join tuple ===')
nama1 = ('a','b','c')
nama2 = (1,2,3,4)
join = nama1 + nama2
print(join)

print('=== multiply tuple ===')
print(nama1 * 2)

print('=== Index Method ===')
index = nama1.index('b')
print(index)

print('=== count method ===')
x = (1,3,4,5,6,3,4,3,3,3)
y = x.count(3)
print(y)