import turtle as t

c=["red","blue","gray","green","pink","black","white","sky blue","orange"]

t.speed(10)
for i in range(8,-1,-1):
    t.fillcolor(c[i])
    t.begin_fill()
    t.circle(i*15)
    t.end_fill()

t.filling()
