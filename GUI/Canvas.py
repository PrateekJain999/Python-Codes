from tkinter import *

root=Tk()

F1=Frame(root,cursor="man",width=100,height=100).pack()
F1=Frame(root,cursor="heart",width=100,height=100).pack(side='bottom')

#=============================canvas===============================================
"""
C1=Canvas(F1,bd=10,bg='purple',cursor='circle',highlightcolor='blue',width=300,height=300)
C1.pack()

l=C1.create_line(50,50,100,100,width=5)
o=C1.create_oval(100,100,200,300,fill='red')#(initial point,initial point,final point,final point

arc=C1.create_arc(300,300,350,210,extent=150,fill='orange') #starting point,final point
l2=C1.create_line(300,300,350,210,width=5)

img=PhotoImage(file='354637.png')
image=C1.create_image(300,300,image=img,anchor=NW)

"""

C2=Canvas(F1,bd=10,bg='red',cursor='circle',highlightcolor='blue',width=300,height=300)
C2.pack()

#R=C2.create_rectangle(100,100,300,250,fill='yellow')

points=[100,100,300,250,200,50,100,100]

P=C2.create_polygon(points)

root.mainloop()
