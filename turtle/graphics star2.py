import turtle as t

t.speed(50)
t.bgcolor("white")
t.color("red","black")

t.penup()
t.goto(-200,100)
t.pendown()
def star(t,size):
    if size<=10:
        return
    else:
        t.begin_fill()
        for i in range(5):
            t.forward(size)
            star(t,size//3)
            t.left(216)
        t.end_fill()

star(t,360)
