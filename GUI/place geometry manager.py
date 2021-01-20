from tkinter import *

root=Tk()
root.geometry("300x300+100+100")

L1=Label(root,text='LABEL 1')
L2=Label(root,text='LABEL 2')

L1.place(x=100,y=100)
L2.place(x=200,y=200)

root.mainloop()
