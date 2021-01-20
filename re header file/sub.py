import re

line='pratee5k is a good boy'

print('a-f : ',re.sub('[a-f]','2',line))
print()
print('^is : ',re.sub('^is','2',line))
print()
print('\S : ',re.sub('\S','2',line))
print()
print('\s : ',re.sub('\s','2',line))
print()
print('\W : ',re.sub('\W','2',line))
print()
print('\w : ',re.sub('\w','2',line))
print()
print(r'\ba : ',re.sub(r'\ba','2',line))
print()
print('\B : ',re.sub('\B','2',line))
print()
print('5 : ',re.sub('5','2',line))
print()