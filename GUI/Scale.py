from tkinter import *

root=Tk()

S1=Scale(root,cursor='heart',bg='red',from_=0,to=100,
         orient=HORIZONTAL,foreground='yellow',activebackground='purple',length=200,width=18,sliderlength=25)
S1.set(50)
S1.pack()

S2=Scale(root,cursor='heart',bg='red',from_=0,to=100,
         orient=VERTICAL,foreground='yellow',activebackground='purple',length=200,width=18,sliderlength=25)
S2.set(50)
S2.pack(side=LEFT,fill=Y)

root.mainloop()
