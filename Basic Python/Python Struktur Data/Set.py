print('=== set ===')
thisset = {'apel','duku','sukun','apel'}
print(thisset)
print(len(thisset))

item = {'apel',2,True}
print(item)
print(type(item))

item1 = set(('jeruk', 'bit', 'mangga'))
print(item1)

print('=== Access items === ')
snacks = {'candy','chocolate','chips'}
for f in snacks:
    print(f)

print('candy' in  snacks)

print("=== add sets items ===")
thisset = {'jambu','kelapa','pisang'}
thisset.add('jeruk')
print(thisset)

thisset1 = {'apel','leci','lemon'}
tropic1 = {'melon','plum','nanas'}
thisset1.update(tropic1)
print(thisset1)

file1 = {'You and I'}
file2 = ['nothing else nothing to you']
file1.update(file2)
print(file1)

print("=== remove item set ===")
number = {1,3,4,5}
number.remove(3)
print(number) # remove() ketika menghapus item diluar dari set maka akan error

number.discard(5)
print(number)# discard() ketika menghapus item diluar dari set maka tidak akan error

number.pop()
print(number)

tropic1.clear()
print(tropic1)

set1 = {1,2,3}
set2 = {'aku','dia','mereka',3}
set3 = set1.union(set2)
print(set3)

print('=== Hanya Simpan Duplikat ===')
xo = {4,5,7,9}
yo = {5,4,8,0}
xo.intersection_update(yo)
print(xo)

f = set1.intersection(set2)
print(f)

print('=== Simpan semua kecuali duplikat ===')
l = {'kuning','hitam','hijau'}
y = {'hitam','putih','abu'}
l.symmetric_difference_update(y)
print(l)

he = {'kuning','hitam','hijau'}
ho = {'hitam','putih','abu'}
print(he.symmetric_difference(ho))


lmao = {'hi','you','everybody'}
wow = {'you','low','beauty'}
u = lmao.isdisjoint(wow)
print(u)

lmao = {'hi','everybody'}
wow = {'low','beauty'}
u = lmao.isdisjoint(wow)
print(u)

warna = {'nila','jingga','ungu'}
warni = {'jingga','nila','merah'}
c = warna.issubset(warni)
print(c)

warna = {'nila','jingga','ungu'}
warni = {'ungu','jingga','nila','putih'}
print(warna.issubset(warni))

#pop() menghaspus item di bagian akhir
#pop(2) akan menghapus item dengan  index 2

warna = {'nila','jingga','ungu','putih'}
warni = {'ungu','jingga','nila'}
print(warna.issuperset(warni))
print(warni.issuperset(warna))
