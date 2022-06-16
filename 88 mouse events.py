from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>",doSomething) #left click
#window.bind("<Button-2>",doSomething) press scroll wheel
#window.bind("<Button-3>",doSomething) right mouse click
#window.bind("<ButtonRelease>",doSomething) release click
#window.bind("<Enter>",doSomething) enter the window
#window.bind("<Leave>",doSomething) leave the window
#window.bind("<Motion>",doSomething) movements

window.mainloop()