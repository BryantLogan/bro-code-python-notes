from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
         print("Youd don't agree!")

window = Tk()

x = IntVar()

#python_photo = PhotoImage(file='  ')

check_button = Checkbutton(window, 
                            text="I agree to something",
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            font=('Arial',20),
                            fg='#00FF00',
                            bg="black",
                            activebackground='black',
                            activeforeground="#00FF00",
                            padx=25,
                            pady=10)

check_button.pack()

window.mainloop()