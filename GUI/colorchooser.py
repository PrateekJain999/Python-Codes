from tkinter import *
from tkinter import colorchooser

def call_me():
    clr=colorchooser.askcolor(title='select color')
    print(clr)
    root.configure(bg=clr[1]) #chose either hex value or rgb value
    
root=Tk()

B1=Button(root,text='Select color',command=call_me).pack()

root.geometry('300x300+100+100')
root.mainloop()
