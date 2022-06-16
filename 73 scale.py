from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

scale=Scale(window,from_=0,to=100)
scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval = 10,
              showvalue = 0,
              resolution =5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black')

scale.set(scale['from']-scale['to']/2+scale['to'])
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()