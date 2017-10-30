
from tkinter import *

paper = Tk()
# Code to add widgets will go here...

li = ['C','python','php','html','SQL','java']

listbox = Listbox(paper)
for item in li:
    listbox.insert(0, item)

listbox.pack()
paper.mainloop()
