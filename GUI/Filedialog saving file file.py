from tkinter import *
from tkinter import filedialog

def open_file():
    f=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    if f is None:
        return
    f.write("hello prateek jain")
    f.close()

root=Tk()

B1=Button(root,text='file open',command=open_file).pack()

root.geometry("300x300+100+100")
root.mainloop()
