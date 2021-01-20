from tkinter import *

def Open_New_Window():
    Win=Toplevel(bg='red',bd=10,cursor='heart',width=10,height=10)
    Win.title("top Window")
    Win.geometry("300x300+100+100")
    B2=Button(Win,text='close',command=Win.destroy).pack()

root=Tk()
B1=Button(root,text="New Window",command=Open_New_Window).pack()

root.geometry("300x300+100+100")
root.mainloop()
