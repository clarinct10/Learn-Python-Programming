import datetime
x = datetime.datetime.now()
print(x.strftime('%Y'))
print(x.strftime('%A'))
print(x.strftime('%D'))
print(x.strftime('%d'))
print(x.strftime("%m/%d/%Y, %H:%M:%S"))

import datetime
x = datetime.datetime(2018,6,1)
print(x.strftime('%B'))
print(x)
