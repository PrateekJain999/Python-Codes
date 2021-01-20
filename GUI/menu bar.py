from tkinter import *

root=Tk()

def Print():
    print("Print")

Head=Menu(root)
root.config(menu=Head)

fileMenu= Menu(Head)
Head.add_cascade(label='file',menu=fileMenu)

fileMenu.add_command(label='New',command=Print)
fileMenu.add_separator()
fileMenu.add_command(label='add data')

#====================more than one files============================
editMenu= Menu(Head)
Head.add_cascade(label='edit',menu=editMenu)

 #adding labels on file
editMenu.add_command(label='edit_file')
editMenu.add_command(label='edit data')

#further adding

save_menu=Menu(root)
fileMenu.add_cascade(label='save',menu=save_menu)
save_menu.add_command(label='save q')
save_menu.add_command(label='save w')

root.mainloop()
