from tkinter import *

root=Tk()

def call_me():
    print("Fun Called")

photo=PhotoImage(file='354637.png')

B1=Button(root,text='Button 1',activebackground='red',bg='blue',command=call_me,height=1).pack()
B2=Button(root,text='Button 2',activeforeground='purple',bg='orange',font=('arial',20,'bold')).pack()
B3=Button(root,text='Button 3',image=photo,height=100,width=100).pack(pady=20)
B4=Button(root,text='Button 4',command=root.destroy).pack(fill='y')
B5=Button(root,text='Button 5').pack(fill='both')
