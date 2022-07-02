#List length
print('== List Length ==')
x = ['3','2','3']
print(len(x))

list = ['aku',3,True]
print(list)

#Access list
print('==Access List==')
list = ['buku','pulpen','pensil','botol','tas']
print(list[2])
print(list[-1])

#Range of index / Slicing
print(list[1:4])
print(list[:4])
print(list[2:])
print(list[-4:-1])

if 'pulpen' in list:
    print('yeah, thats great!!')

list[1] = 'penggaris'
print(list)

list[1:3] = ['jam','Rautan']
print(list)
list[1:2] = ['kacamata','kotak pensil']
print(list)
list[2:4] = ['kalender']
print(list)

# Add list items
list.insert(0,'payung')
print(list)

list.append('sandal')
print(list)

bunga = ['mawar', 'sakura']
buah = ['lemon','jeruk']
bunga.extend(buah)
print(bunga)

alat = {'HP' : 'Samsung', "TV" : 'Sharp'}
bunga.extend(alat)
print(bunga)

# Remove list Items
bunga.remove('mawar')
print(bunga)

bunga.pop(2)
print(bunga)
bunga.pop()
print(bunga)

del bunga[1]
print(bunga)

#del bunga
#print(bunga)

list.clear()
print(list)

# Loop For
print('== Loop For ==')
barang = ['Tas','payung','celana']
for x in barang:
    print(x)

for c in range(len(barang)):
    print(barang[c])

fruits = ['apel', 'jambu', 'kiwi', 'pepaya']
new_list = []

for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)

# While loop
print('== While Loop ==')
barang = ['Tas','payung','celana']
i = 0
while i < len(barang):
    print(barang[i])
    i += 1

print('==List Comprehension==')
fruit = ['apel', 'jambu', 'kiwi', 'jeruk']
new_list = [x for x in fruit if 'a' in x]
print(new_list)

new_list = [x for x in fruit if x != 'apel']
print(new_list)

new_list = [x for x in range(10)]
print(new_list)

new_list = [x for x in range(10) if x < 5]
print(new_list)

new_list = [x.upper() for x in fruit]
print(new_list)

new_list = ['hello' for x in fruit]
print(new_list)

new_list = [x if x != 'banana' else 'orange' for x in fruit]
print(new_list)

sentence = 'the quick brown fox jump over the lazy dog'
words = sentence.split()
word_length = [len(word) for word in words if word != 'the']
print(words)
print(word_length)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [int(x) for x in numbers if x > 0]
print(new_list)

# Sort List
print('== Sort List ==')
animals = ['cat', 'dog', 'bird', 'panda']
animals.sort()
print(animals)

num = [40, 25, 65, 10, 55]
num.sort()
print(num)

animals.sort(reverse=True)
print(animals)


def func(n):
    return abs(n - 50)

x = [50, 30, 45, 67, 100]
x.sort(key=func)
print(x)

fruit1 = ["banana", "Orange", "Kiwi", "cherry"]
fruit1.sort(key=str.lower)
print(fruit1)

fruit1.reverse()
print(fruit1)

print('==copy list==')
buah = ["grape", "Orange", "Kiwi", "cherry"]
listbuah = buah.copy()
print(listbuah)

mylist = listbuah
print(mylist)

print('==Join List==')
list1 = ['clarin', 'celsia', 'tanoko']
list2 = [1, 2, 3, 4]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
list4.extend(list5)
print(list4)

