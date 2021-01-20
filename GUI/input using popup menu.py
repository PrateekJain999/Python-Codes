from tkinter import *
from tkinter import simpledialog

def Get_Data():
    a=simpledialog.askstring("Title","Please enter your name : ")
    print(a)

root=Tk()

B1=Button(root,text="popup",command=Get_Data).pack()

root.geometry("300x300+100+100")
root.mainloop()
