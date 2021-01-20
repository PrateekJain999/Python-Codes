from tkinter import *
from tkinter import messagebox

root=Tk()

def Info():
    messagebox.showinfo("Info",'Hello Bro')

def Error():
    messagebox.showerror('error','invalid type')

def Warning1():
    messagebox.showwarning('Warning','Invalid user')

B1=Button(root,text='info',command=Info).pack()
B2=Button(root,text='error',command=Error).pack()
B3=Button(root,text='warning',command=Warning1).pack()



root.mainloop()
