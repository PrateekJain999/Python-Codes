import re

#res=[x for x in re.findall('[]','agbsg')]
str = "Hi i am yogesh mehra and 28 year old yogesh"
"""x = re.findall("[g-z]", str)
print(x,sep='')
for i in x:
    print(i,end="")
x = re.findall("[0-9]", str)
print(x)
x = re.findall("[^0-9]", str)
print(x)
"""
x = re.findall("[a-z0-9A-Z ]", str)
print(x)
for i in x:
    print(i,end="")

x = re.findall("y.g", str)
print(x)
x = re.findall("^Hi", str)
print(x)
if (x):
  print("Welcome")
else:
  print("No match")
x = re.findall("yogesh|kumar", str)

print(x)

if (x):
  print("welcome!")
else:
  print("No match")
"""
x = re.findall("\D", str)
print(x)
x = re.findall("\S", str)
print(x)
x = re.findall("\W", str)
print(x)
x = re.findall("\b", str)
print(x)
x = re.subn("mehra","kumar", str)
print(x)"""
