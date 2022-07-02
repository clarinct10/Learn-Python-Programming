print('=== while loop ===')
i = 1
while i < 6:
    print('Butter')
    i +=1

print('=== Break statement ===')
i = 1
while i < 6:
    print('Hello')
    if i == 3:
        break
    i += 1

print('=== continue statement ===')
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print('=== Else ===')
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')
