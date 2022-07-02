print('== Boolean ==')
print(10 > 9)
print(11 < 7)
print(11 == 12)

a = 100
b = 50
if a < b:
    print("Hebat")
else:
    print("luar biasa")

# Evaluate value and variables
c = 0
d = 'Purple'
print(bool(c))
print(bool(d))
print(bool(321))
print(bool(['better',3]))
print(bool(None))
print(bool([]))

class Sunset:
    def __len__(self):
        return 6
obj = Sunset()
print(obj.__len__())
print(bool(obj))

x = 25
print(isinstance(x,int))
