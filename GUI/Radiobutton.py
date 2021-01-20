from tkinter import *

root=Tk()

def call():
    print(i.get())

i=IntVar()

#it return value without button bcoz we call the fun using command directly
R1=Radiobutton(root,text='male',value=1,activeforeground='red',variable=i,
               activebackground='purple',command=call).pack()

#it return value after clicking of button bcoz we can not call the command option
R2=Radiobutton(root,text='female',value=2,bg='yellow',
               variable=i,width=5,height=5).pack()

B1=Button(root,text='Button 1',command=call).pack()

root.mainloop()
