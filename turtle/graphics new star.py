import turtle as t

t.speed(10)

d=500
angle=150
t.color("red")

for i in range(150):
    t.forward(d)
    t.left(angle)
    d=d-4
