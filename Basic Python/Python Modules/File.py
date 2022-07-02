print('== Python Module ==')
import mymodule
mymodule.greeting('Jonathan')

a = mymodule.person1['age']
print(a)

import mymodule as mx
a = mx.person1['age']
print(a)

import platform
x = platform.system()
print(x)

c = dir(platform)
print(c)

from mymodule import person1
print(person1['age'])
