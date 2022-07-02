print('== Python JSON ==')
import json
x ='{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x) #Konversi JSON string ke dict python
print(y['age'])

import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x) #Konversi python object ke JSON
print(y)
print()
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print()
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
print()
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print()
print(json.dumps(x, indent=4, sort_keys = True))