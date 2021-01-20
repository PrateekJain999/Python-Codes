from tkinter import *

class MY:
    def __init__(self,master):
        self.Button1 = Button(master,text="Button 1",command=self.printMessage)
        self.Button1.pack(side=LEFT)
        self.Button2= Button(master,text="Button 2",command=master.destroy)#master.destoy or master.quit predefined
        self.Button2.pack(side=LEFT)

    def printMessage(self):
         print("Print Fun")
         

root=Tk()
B=MY(root)
root.mainloop()





    
