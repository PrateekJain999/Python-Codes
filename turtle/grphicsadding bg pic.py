import turtle as t

#t.bgpic("354637.png")
t.speed(10)
l=["red","purple","black","blue","orange"]

for i in range(200):
    t.color(l[i%5])
    t.pensize(i//10)
    t.forward(i)
    #t.lt(60)
    t.lt(48)
