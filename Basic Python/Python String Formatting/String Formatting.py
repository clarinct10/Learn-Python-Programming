print('== String Formatting ==')
price = 49
txt = 'The price is {} dollars'
print(txt.format(price))

price = 49
txt = 'The price is {:.2f} dollars'
print(txt.format(price))

txt = 'For only {price:.2f} dollars'
print(txt.format(price = 49))

quantity = 3
itemno = 567
price = 49
myorder = 'I want {} pieces of item number {} for {:.2f} dollars'
print(myorder.format(quantity, itemno, price))

print('== Index number ==')
age = 18
name = 'xoxo'
v = 'Hello, Im {1}. {1} as a collage student on age {0}'
print(v.format(age,name))

print('== Names Index ==')
myorder = 'I have a {carname}, it is a {model}.'
print(myorder.format(carname = 'Ford', model = 'mustang'))
