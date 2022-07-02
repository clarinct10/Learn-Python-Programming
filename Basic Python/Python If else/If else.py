print('=== if else ===')
a = 45
b = 67
if a < b:
    print('b lebih besar dari a')

a = 22
b = 22
if a < b:
    print('b lebih besar dari a')
elif a == b:
    print('a sama dengan b')
else:
    print('a lebih besar dari b')

a = 98
b = 56
if a < b:
    print('b lebih besar dari a')
elif a == b:
    print('a sama dengan b')
else:
    print('a lebih besar dari b')

print('=== short hand ===')
if a > b : print('a lebih besar dari b')

a = 45
b = 78
print('Hebat') if a < b else print('jago')

a = 30
b = 45
print('a') if a > b else print('u') if a == b else print('i')

# And
a = 45
b = 78
c = 90
if b > a and c > a:
    print('ok')

if a > b or c > b:
    print('ok')

print('=== nested if ===')
x = 30
if x > 10:
    print('ha')
    if x > 20:
        print('ha')
    else:
        print('he')
