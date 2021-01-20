import re

line='prateek is a good boy'

for i in re.finditer('\W',line):
    loc=i.span()
    print(loc)
