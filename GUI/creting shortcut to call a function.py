from tkinter import *
from tkinter import messagebox

def call_me(event=""): #event='' unless when button pressed it give error
    messagebox.showinfo("trying","this is something important")

root=Tk()

root.bind('<Control-c>',call_me)
B1=Button(root,text='call_me',command=call_me).pack()

root.geometry('300x300+100+100')
root.mainloop()
