import turtle as t

def glow(t):
    t.fillcolor("red")
def unglow(t):
    t.fillcolor("")

    
t.dot(500,"red")
t.dot(100,"blue")
print(t.position())
print(t.towards(1.732,1))
print(t.position())
print(t.xcor())
t.shape("turtle")
t.tilt(90)
t.settiltangle(270)
t.fd(60)
t.tiltangle(90)
t.fd(90)
t.onclick(glow(t),btn=100)
t.onrelease(unglow(t),btn=2000)

