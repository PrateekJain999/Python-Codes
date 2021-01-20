

i=IntVar()

def click1():
    print(i.get())

#gives either 0,1 or unchecked,checked
    
C1=Checkbutton(root,text="item",variable=i)
C1.pack()
B1=Button(root,text='Button',command=click1)
B1.pack()
root.mainloop()
