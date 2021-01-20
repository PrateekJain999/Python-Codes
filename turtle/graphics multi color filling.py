import turtle as t

c=["red","blue","gray","green","pink","black","white","sky blue","orange"]

t.speed(10)
for i in range(8,0,-1):
    t.fillcolor(c[i-2])
    t.begin_fill()
    t.circle(i*15)
    t.end_fill()

t.filling()