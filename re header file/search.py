import re

line=' pra4tee7k is a g9oo1d boy'

print('eek : ',re.search('ee7',line))
print('\d : ',re.search('\d',line))
print('\D : ',re.search('\D',line))
print('\s : ',re.search('\s',line))
print('\S : ',re.search('\S',line))
print('\w : ',re.search('\w',line))
print('\W : ',re.search('\W',line))
