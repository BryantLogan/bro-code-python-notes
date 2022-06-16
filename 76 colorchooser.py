from tkinter import *
from tkinter import colorchooser
from turtle import color #submodule

def click():
    color = colorchooser.askcolor()
    #print(color)
    colorHex=color[1]
    #print(colorHex)
    window.config(bg=color[1]) #change background color

window = Tk()
window.geometry("420x420")
button = Button(text="click me",command=click)
button.pack()
window.mainloop()