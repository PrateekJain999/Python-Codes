import turtle as t

t.screensize(50,50)
t.speed(10)
t.goto(-50,-50)
for i in range(11,0,-1):
    if (i%2==0):
        t.fillcolor("blue")
    if (i%2!=0):
        t.fillcolor("red")
    t.begin_fill()
    t.circle(i*15)
    t.end_fill()

t.filling()
t.reset()
