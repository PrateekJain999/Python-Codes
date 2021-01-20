from tkinter import *

root=Tk()

PW=PanedWindow(root,bg='red',bd=10,width=100,height=100)
E1=Entry(PW,bd=5).pack()
PW.pack()

root.geometry('300x300+100+100')
root.mainloop()
