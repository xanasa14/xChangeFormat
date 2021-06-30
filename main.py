from tkinter import *

color = "white"
entry1 = None
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
#Define a function to Change the color of the label widget
def change_color(color):
   if (color== ""):
      color = "white"
   L1.config(bg= "red", fg= "black")
   L2.config(bg= "red", fg= "black")
#
def clicked():
    #Input = entry1.get()
    #FileName = str(Input + ".txt")
    #TextFile = open(FileName,"w")

    """
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button",command=newFile)
    button.pack()"""
    filewinsecond= Toplevel(root)

    entry1 = Entry(filewinsecond)
    button1 = Button(filewinsecond, text="Press to create text file", command=newFile)
    entry1.pack()
    button1.pack()
def newFile():
    filewin2 = Toplevel(filewinsecond)

    Input = entry1.get()
    FileName = str(Input + ".txt")
    TextFile = open(FileName,"w")

    filewin = Toplevel(root)
    button = Button(filewin2, text="Do nothing button")
    button.pack()
root = Tk()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=clicked)
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

redbutton = Button(topframe, text="Red", fg='red',command=change_color("red"))
redbutton.pack()

greenbutton = Button(topframe, text="Brown", fg="brown",command=change_color('brown'))
greenbutton.pack()

bluebutton =Button(topframe,text="Blue",fg="blue",command=change_color("blue"))
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black",fg="Black")
blackbutton.pack(side= LEFT)





#Create a Button
Button(bottomframe, text="Change Color", command=change_color("Black")).pack(pady=20)

root.mainloop()
