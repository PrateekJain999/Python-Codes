from tkinter import *

def Name():
    print("PRATEEK JAIN")


root=Tk()

F1=Frame(root,bg='red',height=300,width=300)
F1.pack()

B1=Button(F1,text='Click Me',command=Name)
B1.pack()

root.mainloop()
