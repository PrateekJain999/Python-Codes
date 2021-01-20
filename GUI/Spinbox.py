from tkinter import *

"""def Click1():
    print(S1.get())""" #not working

root=Tk()

S1=Spinbox(root,bg='red',bd=10,from_=1,to=100,cursor='heart',
           activebackground='purple',disabledbackground='yellow').pack()

B1=Button(root,text='click',command=Click1).pack()

root.geometry("300x300+100+100")
root.mainloop()
