from tkinter import *


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

frame = Frame(root)
frame.pack(side=TOP)
L1 = Label(frame, text = "User Name")
L1.pack(side=LEFT)
E1 = Entry(frame,bd=5)
E1.pack(side=LEFT)

secondFrame = Frame(root)
secondFrame.pack()
L2 = Label(secondFrame, text = "Password  ")
L2.pack(side=LEFT)
E2 = Entry(secondFrame,bd=6)
E2.pack(side=LEFT)

topframe = Frame(root)
topframe.pack(side=LEFT)
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redbutton = Button(topframe, text="Red", fg='red',)
redbutton.pack()

greenbutton = Button(topframe, text="Brown", fg="brown")
greenbutton.pack()

bluebutton =Button(topframe,text="Blue",fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black",fg="Black")
blackbutton.pack(side= LEFT)
root.mainloop()
