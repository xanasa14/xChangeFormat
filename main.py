from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x200")
frame = Frame(root)
frame.pack()
topframe = Frame(root)
topframe.pack(side=LEFT)
L1 = Label(frame, text = "User Name")
L1.pack(side=LEFT)
E1 = Entry(frame,bd=5)
E1.pack(side=LEFT)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redbutton = Button(topframe, text="Red", fg='red',bd=5)
redbutton.pack(side = LEFT)

greenbutton = Button(topframe, text="Brown", fg="brown",bd=10)
greenbutton.pack(side=LEFT)

bluebutton =Button(topframe,text="Blue",fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black",fg="Black")
blackbutton.pack(side= LEFT)
root.mainloop()
