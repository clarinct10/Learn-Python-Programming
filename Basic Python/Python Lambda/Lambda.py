print('== python lambda ==')
x = lambda a : a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,7))

x = lambda a,b,c : a + b + c
print(x(4,7,3))
print('================')
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)
mytrippler = myfunc(5)
print(mydoubler(11))
print(mytrippler(11))
