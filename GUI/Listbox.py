from tkinter import *

#fetching data from List

def Print():
    clicked_items=L4.curselection()
    print(clicked_items)

    for i in clicked_items:
        print(L4.get(i))

def Delete_Data():
    clicked_items=L4.curselection()
    print(clicked_items)

    for i in clicked_items:
        print(L4.delete(i))

root=Tk()

L1=Listbox(root,selectmode=SINGLE,width=20,height=5)
L1.insert(1,'c')
L1.insert(2,'c++')

L2=Listbox(root,selectmode=BROWSE,width=20,height=5)
L2.insert(1,'java')
L2.insert(2,'c#')

L3=Listbox(root,selectmode=EXTENDED,width=20,height=5)
L3.insert(1,'R')
L3.insert(2,'python')

L4=Listbox(root,selectmode=MULTIPLE,width=20,height=5)
L4.insert(1,'AI')
L4.insert(2,'machine ')
L4.insert(3,'machine learning')
L4.insert(4,'machine 1')
L4.insert(5,'machine 2')

B1=Button(root,text='Print',command=Print).pack()
B2=Button(root,text='Delete',command=Delete_Data).pack()

L1.pack()
L2.pack()
L3.pack()
L4.pack()

root.geometry("400x400+100+100")

root.mainloop()
