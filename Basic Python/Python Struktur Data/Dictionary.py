print('=== Dictionary ===')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
print(thisdict)
print(len(thisdict))
#Dictionary tidak memungkinkan adanya duplikat
wow = {'nama' : 'velas',
       'nama' : 'budi'
}
print(wow)

Datadiri = {'nama' : 'lala',
            'wanita' : True,
            'usia' : 19,
            'hobi' : ['renang','balet','masak']
}
print(Datadiri)
print(type(Datadiri))
print(Datadiri['nama'])
print(Datadiri.get('nama'))

print(Datadiri.keys())
Datadiri['makanan'] = 'Keripik'
print(Datadiri.keys())

#values() = untuk menampilkan nilai dalam list
print(Datadiri.values())
Datadiri['usia'] = 20
print(Datadiri.values())
Datadiri['tinggi'] = 170
print(Datadiri.values())

#items() = untuk menampilkan kunci dan nilai dalam satu list variabel
print(Datadiri.items())

Datadiri['minuman'] = 'milk tea'
print(Datadiri.items())

if 'minuman' in Datadiri:
    print('Yes, you right')

print('=== change value ===')
game = {'PUBG' : 'game1',
        'Mobile Legend' : 'game2',
        'valorant' : 'game3'
}
game['valorant'] = 'game4'
print(game)

game.update({'PUBG' : 'game5'})
print(game)

print('=== Remove items ===')
Datadiri.pop('minuman')
print(Datadiri)

Datadiri.popitem()
print(Datadiri)

del Datadiri['hobi']
print(Datadiri)

# del Datadiri
# print(Datadiri)

game.clear()
print(game)

print('=== Loop Dictionary ===')
for x in Datadiri:
    print(x)
print()
for c in Datadiri:
    print(Datadiri[c])
print()
for l in Datadiri.values():
    print(l)
print()
for u in Datadiri.keys():
    print(u)
print()
for x,y in Datadiri.items():
    print(x,y)

print('=== copy dictionaries ===')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict1 = dict(thisdict)
print(mydict1)

print('=== nested dictionary ===')
myfamily = {
    'child1': {
        'nama' : 'brandon',
        'age'  : 4
    },
    'child2' : {
        'nama' : 'carline',
        'age'  : 9
    }
}
print(myfamily)

child1 = {
    'nama': 'brandon',
    'age': 4
}
child2 = {
    'nama': 'carline',
    'age': 9
}
x1 = {
    'child1' : child1,
    'child2' : child2
}
print(x1)