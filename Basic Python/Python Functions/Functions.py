print('=== Python function ===')
# Membuat function
def my_function():
    print('hello there, I like star')
# Panggil function
my_function()

def my_function(fname):
    print(fname + ' awesome')
my_function('AWS')
my_function('Google')
my_function('Facebook')

def my_function(fname,lname):
    print(fname + ' ' + lname)
my_function('Buku','Sejarah')

print('== Argumen args ==')
def my_function(*args):
    print('color of rainbow is ' + args[2])
my_function('yellow','blue','red','green')

def my_function(child1,child2,child3):
    print('The youngest child is ' + child2)
my_function(child1 = 'x1', child2 = 'x2', child3 = 'x3')

print('== Argumen Kata Kunci ==')
def my_function(**kwargs):
  print("His last name is " + kwargs["f1"])
my_function(f1 =  'Rain', f2 = "Refsnes")

print('== Parameter Default ==')
def my_function(country = 'Canada'):
    print('I am from ' + country )
my_function('Indonesia')
my_function('London')
my_function('Rusia')
my_function()

print('== Passing list as an argument ==')
def my_function(food):
    for x in food:
        print(x)
fruits = ['sirsak','pisang','kelapa']
my_function(fruits)

print('== Return value ==')
def my_function(x):
    return 5 * x

print(my_function(4))
print(my_function(6))
print(my_function(3))

def my_function():
    pass

print('== Recursion Python ==')
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)
print()

print('--------------------')
#Recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 6
print('The factorial num', num, 'is', factorial(num))

print('--------------------')
# Program to print the fibonacci series upto n_terms
# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))
n_terms = 10
# check if the number of terms is valid
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(recursive_fibonacci(i))
