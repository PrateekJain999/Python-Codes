from tkinter import *
from tkinter import filedialog

def open_file():
    result=filedialog.askopenfile(initialdir="C:/Users/prateek jain/Documents/python/GUI",title="Select_file",filetypes=(("text files",".txt"),('all files','*.*')))
    print(result)

    for i in result:
        print('file data : ',i)

root=Tk()

B1=Button(root,text='file open',command=open_file).pack()

root.geometry("300x300+100+100")
root.mainloop()
