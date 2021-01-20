from tkinter import *

root=Tk()

F1=Frame(root,bg='yellow')

L1=Label(F1,text="LABEL 1",fg='green',bg='orange')
L2=Label(F1,text="LABEL 2",fg='brown',bg='red')
L3=Label(F1,text="LABEL 3",fg='red',bg='purple')
L4=Label(F1,text="LABEL 4",fg='blue',bg='pink')

L1.pack()
L2.pack(fill='x')
L3.pack(side=LEFT,fill='y')
L4.pack()

F1.pack()

F2=Frame(root,bg='yellow',bd=100)

L5=Label(root,text="LABEL 5",bd=10,fg='green',bg='orange')  #for fill axis label and wigth present on window not fon frame
L6=Label(root,text="LABEL 6",fg='brown',bg='red')
L7=Label(root,text="LABEL 7",fg='red',bg='purple')
L8=Label(root,text="LABEL 8",fg='blue',bg='pink')

L5.pack()
L6.pack(fill='x')
L7.pack(side=LEFT,fill='y')
L8.pack()

F1.pack()

root.mainloop()
