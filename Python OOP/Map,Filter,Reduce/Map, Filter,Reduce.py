print('==== Map ====')
#fungsi map() untuk mengeksekusi fungsi yang ditentukan untuk setiap item didalam iterable.Item dikirim ke fungsi sebagai paramater
# Syntax : map(func, *iterables)
def myfunc(a):
    return len(a)

x = map(myfunc,('apple','banana','orange'))
print(x)
print(list(x))

#two iterable object into the function
def myfunc(a,b):
    return a + b
x = map(myfunc,(2,4,5),(1,2,3))
print(list(x))

numbers = (1,2,3,4)
result = map(lambda x: x + x,numbers)
print(list(result))

number1 = [1,2,3]
number2 = [3,4,5]

x = map(lambda x,y: x + y,number1,number2)
print(list(x))

l = ['hey','you','can']
x = list(map(list,l))
print(x)

print('== Reduce ==')
#importing functools for reduce()
import functools
lis = [1,5,3,8,6]

print('Jumlah dari list adalah ', end="")
print(functools.reduce(lambda a,b: a + b, lis))

print("Maksimum dari list adalah ", end="")
print(functools.reduce(lambda a,b: a if a > b else b, lis))

#using operator functions
import functools
import operator

lis = [1,3,5,2,4]
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add,lis))

print("The product of list elements is : ",end="")
print(functools.reduce(operator.mul,lis))
print(functools.reduce(operator.add, ['clarin ', 'as ', 'a Data scientist']))

from functools import reduce
#10 sebagai initial yang bersifat opsional
numbers = [3,4,6,9,34,12]
def custom_sum(first,second):
    return first + second
result = reduce(custom_sum,numbers,10)
print(result)

print('===Filter===')
score = [66,90,68,59,76,60,88,74,81,65]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student,score))
print(over_75)

drome = ['demogod','rewire','madam','freer','anutforajaroftuna','kiosk']
palindromes = list(filter(lambda word: word == word[::-1], drome))
print(palindromes)

print('=== zip ===')
my_string = ['a','b','c','d','e']
my_numbers = [1,2,3,4,5]
hasil = list(zip(my_string,my_numbers))
print(hasil)

z = zip()
print(z)

#Bila ada dua iterable maka akan digabungkan menjadi 1 iterable
y = zip([1,2,3], [4,5,6,7,8])
print(list(y))

#bila argumennya kosong maka akan mengembalikan iterator kosong
result = zip()
result_list = list(result)
print(result_list)

from functools import reduce
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59 ]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x**2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(map_result)
print(filter_result)
print(reduce_result)

print()
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
"""Jika modul Anda adalah program utama, maka ia akan melihat bahwa __name__memang diatur ke "__main__"dan memanggil dua fungsi, mencetak string "Function A"dan "Function B 10.0".
Hanya Saat Modul Anda Diimpor oleh Orang Lain

( Sebaliknya ) Jika modul Anda bukan program utama tetapi diimpor oleh yang lain, maka __name__akan menjadi "foo", bukan "__main__", dan itu akan melewati badan if pernyataan"""

#modul one.py
#modul two.py
#Kesimpulan
"""Setiap modul dalam Python memiliki atribut khusus yang disebut __name__. Nilai dari__name__ atribut diatur ke "__main__"ketika modul dijalankan sebagai program utama. Jika tidak, nilai__name__ diatur untuk memuat nama modul.
Kami menggunakan blok if __name__ == “__ main__ ” untuk mencegah kode (tertentu) dijalankan saat modul diimpor."""

print('=== sep parameter in print() ===')
print('w','o','i','i', sep='$')
print('happy', 5, 'new year', sep='')

print('=== end paramater ===')
print('G','F', sep='', end='')
print('G')
print('semangat','belajar', sep=' ',end=' yeah ')
print('go!')
print(1,2,3,4,sep='#',end='?')
print()



