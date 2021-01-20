from tkinter import *

def click():
    print(s.get())

root= Tk()

s=StringVar()

C1=Checkbutton(root,text='h;',bd=10,bg='red',activebackground='purple',activeforeground='yellow',font=('arial',20,'bold'),variable=s,
               offvalue='unchecked',onvalue='checked').pack()

B1=Button(root,text='Button',command=click).pack()

root.mainloop()
