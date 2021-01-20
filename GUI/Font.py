from tkinter import *
from tkinter.font import Font
    
root = Tk()

my_font=Font(family="Times New Roman",size=20,slant='italic',underline=2,overstrike=2,weight='bold')
L1=Label(root,text="PRATEEK JAIN",font=my_font,fg='red').pack()

root.mainloop()
