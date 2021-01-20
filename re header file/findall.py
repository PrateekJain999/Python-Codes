import re

line='pratekek is a go8@od kboy'

'''print('0-9 : ',re.findall('[0-9]',line))
print()
print('a-f : ',re.findall('[a-f]',line))
print()
print('a-f,0-9 : ',re.findall('[a-f,0-6]',line))
print()
print('d : ',re.findall('\d',line))
print()
print('\D : ',re.findall('\D',line))
print()
print('\w : ',re.findall('\w',line))
print()
print('\W : ',re.findall('\W',line))
print()
print('pr : ',re.findall('pr',line))
print()
print('x* : ',re.findall('x*',line))
print()
print('^pr : ',re.findall('^pr',line))
print()
print('^0-9 : ',re.findall('[^0-9]',line))
print()
print('\w+ : ',re.findall('\w+',line))
print()'''
x = re.findall("p\w+k",line)
print(x)
x = re.findall("^is", line)
if (x):
  print("Welcome")
else:
  print("No match")
x = re.findall("p\.k", line)
print(x)
