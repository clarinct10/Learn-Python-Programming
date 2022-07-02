# Local Scope
def func():
    x = 300
    print(x)
func()

#local variable dapat diakses dari function lain
def func():
    x = 90
    def myinnerfunc():
        print(x)
    myinnerfunc()
func()

print('== Global Scope ==')
x = 50
def myfunc():
    print(x)
myfunc()
print(x)

print('== Naming variable ==')
x = 100
def myfunc():
    x = 230
    print(x)
myfunc()
print(x)

def myfunc():
    global x
    x = 76
myfunc()
print(x)

x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)
