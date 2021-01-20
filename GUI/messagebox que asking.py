from tkinter import *
from tkinter import messagebox

root=Tk()

def Info():
    messagebox.showinfo("Info",'Hello Bro')

def Error():
    messagebox.showerror('error','invalid type')

def Warning1():
    messagebox.showwarning('Warning','Invalid user')

def Question1():
    ans=messagebox.askquestion("title",'do you want to exit')  

    if ans == 'yes':
        root.destroy()
def Question2():
    ans=messagebox.askyesnocancel('exit','exit')

    if(ans):
        root.quit()

B1=Button(root,text='info',command=Info).pack()
B2=Button(root,text='error',command=Error).pack()
B3=Button(root,text='warning',command=Warning1).pack()
B4=Button(root,text='Ask1',command=Question1).pack()
B5=Button(root,text='Ask2',command=Question2).pack()

root.mainloop()
