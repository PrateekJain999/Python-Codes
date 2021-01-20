from tkinter import *

root=Tk()

def Right(event):
    print("Right Clicked")

def Left(event):
    print("Left Clicked")

def Middle(event):
    print("Center Clicked")

F1=Frame(root,bg="blue",width=200,height=200)
F1.bind("<Button-1>",Left)
F1.bind("<Button-2>",Middle)
F1.bind("<Button-3>",Right)

F1.pack()

root.mainloop()
 
