from tkinter import *

root=Tk()
root.geometry("500x500+0+0")
def name():
    print("PRATEEK JAIN")

photo=PhotoImage(file='354637.png')

L1=Label(root,text="LABEL1",bg="Blue",height=300,width=300,
         image= photo,font=("arial",20,"bold"))

L2=Label(root,text="LABEL2",bg='red',width=5)
L3=Label(root, text= 'LABEL3',height=5)
L1.pack()
"""L2.pack(side=LEFT)
L3.pack(side=RIGHT)"""
L2.pack(side=LEFT)
L3.pack(side=LEFT)
root.mainloop()
