from tkinter import *

root=Tk()

FL=LabelFrame(root,text='Input',bg='red',bd=5,cursor='heart',
              height=100,width=100)

E1=Entry(FL)
E1.pack()

FL.pack()
root.geometry("300x300+100+100")
root.mainloop()
