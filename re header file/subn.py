import re

line='prateek is a good boy'


print(re.subn('e','7',line))
print()
print(re.subn('[a-f]','7',line))
