from tkinter import *

root=Tk()

def Print():
    print(E1.get())

B1=Button(root,text='click me',command=Print)
B1.pack()
E1=Entry(root,bd=5,bg='red',width=20,highlightcolor='blue',cursor='heart')
E1.pack()


root.mainloop()

