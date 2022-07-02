print('==Python RegEx == ')
import re
txt = 'The rain in Spain'
x = re.search('^The.*Spain$', txt)

if x:
    print('Yes, we match')
else:
    print('No match')

c = re.findall('ai',txt)
print(c)

c = re.findall('yo',txt)
print(c)

import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print("The first white-space character is located in position:", x.start())

import re
txt = 'The rain in Spain'
x = re.split('\s',txt)
print(x)

x = re.split('\s',txt,1)
print(x)

x = re.sub('\s','9',txt)
print(x)

x = re.sub('\s','9',txt,2)
print(x)

x = re.search('ai',txt)
print(x)

x = re.search(r'\bS\w+',txt)
print(x.span())

x = re.search(r'\bS\w+',txt)
print(x.string)

x = re.search(r'\bS\w+',txt)
print(x.group())

import re
nomor_telepon_regex = re.compile(r'\d\d\d \d\d\d\d\d\d\d')
mo = nomor_telepon_regex.search('Nomor telepon saya: 061 7984611')
print('Nomor telepon ditemukan : ' + mo.group())

print('=== Pengelompokan dengan tanda kurung () ===')
import re
no_telp_regex = re.compile(r'(\d\d\d) (\d\d\d\d\d\d\d)')
mo = no_telp_regex.search('Nomor telepon saya 021 8273467')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
kode_area, no_telepon = mo.groups()
print(kode_area)
print(no_telepon)

no_telp_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d\d\d\d)')
mo = no_telp_regex.search('Nomor telepon saya (021) 8273467')
print(mo.group(1))
print(mo.group(2))

print('== mencocokkan kelompok dengan Tanda pipa | pada regex ==')
hero_regex = re.compile(r'Superman|Spiderman')
mo1 = hero_regex.search('Superman dan Spiderman')
print(mo1.group())

mo2 = hero_regex.search('Spiderman dan Superman')
print(mo2.group())

bat_regex = re.compile(r'Bat(man|copter|mobile|bat)')
mo = bat_regex.search('Batcopter sedang rusak')
print(mo.group())
print(mo.group(1))

he_regex = re.compile(r'(He){3}')
mo1 = he_regex.search('HeHeHe')
print(mo1.group())

mo2 = he_regex.search('He')
print(mo2 == None)

la_regex = re.compile(r'(la){3,5}')
v1 = la_regex.search('lalalalala')
print(v1.group())

la_regex = re.compile(r'(la){3,5}?')
v2 = la_regex.search('lalalalala')
print(v2.group())

string = 'Rumah: 021 8237371 Kantor: 021 8237432'
no_telp_regex = re.compile(r'\d{3} \d{7}') #tanpa grup
mo = no_telp_regex.findall(string)
print(mo)

no_telp_regex = re.compile(r'(\d{3}) (\d{7})') #dengan grup
mo1 = no_telp_regex.findall(string)
print(mo1)

sesuatu_regex = re.compile(r'\d+\s\w+')
c = sesuatu_regex.findall('11 sepeda, 10 mobil, 9 pesawat, 8 komputer, 7 handphone')
print(c)

vokal_regex = re.compile(r'[aiueoAIUEO]')
x = vokal_regex.findall('Learning Python is VERY FUN')
print(x)

konsonan_regex = re.compile(r'[^aiueoAIUEO]')
b = konsonan_regex.findall('Learnig Python is VERY FUN')
print(b)
