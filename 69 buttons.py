# button = you click it, then it does stuff

from tkinter import *

count = 0


def click():
    global count
    count+=1
    print(count)

window =Tk()

#photo = PhotoImage(file='file.png')
#image = photo, in Button 

button = Button(window,
                text='click me!',
                command =click,
                font=("comic sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE) #DISABLED
button.pack()

window.mainloop()