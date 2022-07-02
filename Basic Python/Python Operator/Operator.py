# Operator Python
print('==Operator Python==')
x = 16
y = 2
a = 5 / 11
b = x * y
c = x + y
d = x - y
e = y % x
f = x ** y
g = 5 // 11
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# Operator assignment pada biner
print('== Operator assignment pada biner ==')
l = 10
l &= 9
k = 11
k |= 12
print(l)
print(k)

#Operator comparison
print('== Operator Comparison ==')
print(9 == 8)
print(10 != 11)
print(4 < 1)
print(19 > 18)
print(17 >= 16)
print(18 <= 20)

#operator logical
print('== Operator Logical==')
x = 7
print(x < 8 and x < 10)
print(x < 3 or x > 5)
print(not(x < 8 and x < 10))

#Identity operators
print('== Idnetity operators ==')
x = ['lemon','apel']
y = ['lemon','apel']
z = x

print(x is y)
print(x is z)
print(x == y)
print( x is not y)
print(x is not z)
print(x != y)

#Membership operator
print('==Membership operator==')
s = ['lemon', 4]
print('lemon' in s)
print(4 not in s)
