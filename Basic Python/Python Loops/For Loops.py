print('=== For ===')
co = ['apel','jeruk','mangga']
for x in co:
    print(x)

for x in 'banana':
    print(x)

print('== Break Statement ==')
co = ['apel','jeruk','mangga']
for x in co:
    if x == 'jeruk':
        break
    print(x)

print('== Continue Statement ==')
co = ['apel','jeruk','mangga']
for x in co:
    if x == 'jeruk':
        continue
    print(x)

# Range Function
for x in range(6):
    print(x)
print()
for v in range(2,5):
    print(v)
print()
for v in range(2,20,2):
    print(v)
print()
for x in range(3):
    print(x)
else:
    print('Nothing')

print('== Break ==')
for q in range(5):
    print(q)
    if q == 2: break
else:
    print('Nothing')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for v in adj:
    for k in fruits:
        print(v,k)