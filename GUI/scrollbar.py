from tkinter import *

root=Tk()

F1=Frame(root)
S1=Scrollbar(F1,bg='red',activebackground='purple',bd=5,cursor='heart')
S1.pack(side=RIGHT,fill=Y)
L1=Listbox(F1,yscrollcommand=S1.set)

for i in range(1,51):
    L1.insert(END,"List "+str(i))

L1.pack(side=LEFT)
S1.config(command=L1.yview)
F1.pack()
 
root.geometry("300x300+120+120")
root.mainloop()

