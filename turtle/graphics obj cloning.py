import turtle as t

t.begin_poly()
t.fd(100)
t.left(20)
t.fd(30)
t.left(60)
t.fd(50)
t.end_poly()
print(t.get_poly())

m=t.clone()
m.fd(100)
