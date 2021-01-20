import turtle as t
import random

for i in range(500):
    r=random.randint(0,1)
    g=random.randint(0,1)
    b=random.randint(0,1)

    ra=(r,g,b)
    t.speed(0)
    t.bgcolor(ra)

    r=random.randint(0,1)
    g=random.randint(0,1)
    b=random.randint(0,1)

    rb=(r,g,b)

    t.fillcolor(rb)
    t.begin_fill()
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.end_fill()

