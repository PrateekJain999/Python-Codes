from tkinter import *
from tkinter.ttk import Combobox

def Print():
    print(C2.get())
    
root = Tk() 

v1=['c++','python','java','R']
v2=list(range(1,51))

C1=Combobox(root,values=v1,height=4,width=10).pack()
C2=Combobox(root,values=v2,height=4,width=10)
C2.set("select")
C2.pack()

B1=Button(root,text='Button 1',command=Print).pack()

root.mainloop()
