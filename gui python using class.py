from tkinter import *

class MY:
    def __init__(self,t):
        self.printButton= Button(t,text="print",command=self.fun)
        self.printButton.pack(side=LEFT)

        self.quitButton= Button(t,text="Quit",command=t.quit)
        self.quitButton.pack(side=LEFT)

    def fun(self):
        print("PRATEEK")

root=Tk()

A=MY(root)
root.mainloop()
