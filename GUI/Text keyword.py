from tkinter import *

def Print1():
    ANS=T1.selection_get()
    print(ANS)
def Print2():
    ANS=T1.selection_get()
    pos=T1.search(ANS,1.0,stopindex=END)
    print(pos)
    print(ANS)
def Delete():
    T1.delete(1.0,END)
    
root=Tk()
T1=Text(root,width=20,font=('arial',10,'bold'),height=5,selectbackground='red',bd=5,bg='blue',wrap=WORD,padx=10,pady=10)#SWLECT BACKGROUND MEANS HIGHLIGHTING THE TEXT
T1.pack()

#for directly inserting text
T1.insert(INSERT,"HELLO I M PRATEEK JAIN")

B1=Button(root,text='print selected ',command=Print1).pack()
B2=Button(root,text='starting loc which text in not written',command=Print2).pack()
B3=Button(root,text='Clear',command=Delete).pack()

root.geometry("300x300+120+120")
root.mainloop()

