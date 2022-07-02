print('== Python try exception ==')
#Exception Handling
try:
    print(x)
except:
    print('An exception occured')

# Many Exceptions
try:
    print(x)
except NameError:
    print('variable is not defined')
except:
    print('Something else went wrong')

# Else
try:
    print('Hello')   # else yang dijalankan karena blok try tidak menimbulkan kesalahan
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

#Finally
try:
    print(x)
except:
    print('something went wrong')
finally:
    print('The try except is finished')

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")

print('=== exception handling ===')
import sys

lists = ['a',0,4]
for each in lists:
    try:
        print('Masukan',each)
        r = 1/int(each)
        break
    except:
        print('upps', sys.exc_info()[0], 'terjadi.')
        print('Masukan berikutnya')
        print()
print('Kebalikan dari ', each, ' =', r)

# x = -1
# if x < 0:
#     raise Exception('Sorry, no numbers below zero')

# x = 'hello'
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')

