from tkinter import *

class MY:
    def __init__(self,t):
        pri= Button(t,text="print",command=self.fun)
        pri.pack(side=LEFT)

        qui= Button(t,text="Quit",command=t.quit)
        qui.pack(side=LEFT)

    def fun(self):
        print("PRATEEK")

root=Tk()

A=MY(root)
root.mainloop()
