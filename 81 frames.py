# frame =   a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame= Frame(window,bg="pink",bd=5,relief=RAISED)
#frame.pack()
frame.place(x=100,y=100)


Button(frame,text="W",font=("Consolas",25),width=3).pack(side=BOTTOM)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)


window.mainloop()