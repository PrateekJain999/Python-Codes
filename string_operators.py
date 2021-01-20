a="hello world"
b="hi"
print (a+" "+b)     #hello world hi
length=len(a)
print (length)          #11
print (a[1:4])          #ell
print (a[1:])           #ello world
print (a[:7])           #hello w
print ('h' in a)        #True
print ('A' in a)        #False
print ('h' not in a)    #False
print ('A' not in a)    #True

#String formatting operator
# print "My name is %s and weight is %d kg!" % ('Zara', 21)
# print ("My name is %s and I am %d years old.")%('Nikhil',30)

print(b*5)              #hihihihihi
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

print ("PrOgRaMiZ".lower())                 #'programiz'
print ("PrOgRaMiZ".upper())                 #'PROGRAMIZ'
print ("This will split all words into a list".split())     #['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print (' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])) #'This will join all words into a string'
print ('Happy New Year'.find('ew'))                         #7
print ('Happy New Year'.replace('Happy','Brilliant'))       #'Brilliant New Year'
