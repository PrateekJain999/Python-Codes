from tkinter import *

root=Tk()
    
F1=Frame(root,bg='yellow',width=50,height=50)

L1=Label(F1,text='Username',fg='black',bg='Gray')
L1.pack()

Name=StringVar()
entry_box= Entry(F1,textvariable=Name,width=25,bg='red').pack()

def pr():
    print("hi "+str(Name.get()))

B1=Button(F1,text='call fun',bg='blue',command=pr)
B1.pack()

F1.pack()

root.mainloop()
