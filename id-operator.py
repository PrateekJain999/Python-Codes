a = 2
# Output: id(2)= 1915013264
print('id(2) =', id(2))

# Output: id(a) = 1915013264
print('id(a) =', id(a))


b = 2

# Output: id(b) = 1915013264
print('id(b) =', id(b))

b = b+1

# Output: id(b) = 1915013280
print('id(b) =', id(b))

# Output: id(3) = 1915013280
print('id(3) =', id(3))

b = 2

# Output: id(2)= 1915013264
print('id(2) =', id(2))
