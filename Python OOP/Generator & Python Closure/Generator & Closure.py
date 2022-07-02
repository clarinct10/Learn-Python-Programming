print(' === Generator ===')
#Yield adalah ciri generator. Yield dan return sama - sama mengembalikan suatu nilai dari sebuah fungsi.
# Return menghentikan fungsi secara keseluruhan sedangkan yield hanya menghentikan sementara dan akan dilanjutkan kembali dari state tersebut
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This printed at last')
    yield n

for item in my_gen():
    print(item)

print('=== Generator dengan loop ===')
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

for char in rev_str('hello'):
    print(char)

print('=== Generator expression ===')
# list comprehension dan generator expression memiliki fungsi yang sama.
# List comprehension menggunakkan [] . Generator expression menggunakkan ()
# list comprehension langsung menghasilkan kesulurahan anggota list
#Generator expression hanya memproduksi item pada saat diminta sebanyak satu item per satu waktu

my_list = [1,3,6,10]

a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(sum(i**2 for i in my_list))
print(max(i**2 for i in my_list))

print('==Python Closure==')
#fungsi pembungkus luar
def print_msg(msg):
    # fungsi bersarang
    def printer():
        print(msg)
    printer()

print_msg('Hello')

def print_msg(msg):
    def printer():
        print(msg)
    return printer

another = print_msg('Hello')
another()

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(4))
print(times5(times3(2)))