from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import time
import price


operator = ''

window = Tk()
window.title("User Authentication")
window.geometry("400x150")
global window2
global root
global window3
global roo
name_var=tk.StringVar()
pass_var=tk.StringVar()

   


def registration():
    window.destroy()
    window2 = Tk()
    window2.title("booking table Form")
    window2.geometry("600x200")  

        
    
    def finish():
        window2.destroy()
        window3 = Tk()
        window3.title("Submitted")
        window3.geometry("600x200")
        def booking():
            window3.destroy()
            from price import table
            table()
        L9 = Label(window3,text="table booked Successfully!!",font="Helvetica 18 bold",bg="black",fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
        btn = Button(window3, text = 'Click me !', bd = '5',
                          command = lambda: booking())
        btn.pack(side='bottom')
        
        
    L4 = Label(window2,text="BOOKING TABLE FORM",font="Helvetica 18 bold").place(relx=0.5, rely=0.05, anchor=CENTER)
    L5 = Label(window2,text="Full Name: ",font="Helvetica 12").grid(pady=(40,0),row=0,column=0)
    E3 = Entry(window2,width=40).grid(pady=(40,0),row=0,column=1)
    L6 = Label(window2,text="phone no: ",font="Helvetica 12").grid(row=1,column=0)
    E4 = Entry(window2,width=40).grid(row=1,column=1)
    L7 = Label(window2,text="total member: ",font="Helvetica 12").grid(row=2,column=0)
    E5 = Entry(window2,width=40).grid(row=2,column=1)
    L8 = Label(window2,text="time of arriving: ",font="Helvetica 12").grid(row=3,column=0)
    E6 = Entry(window2,width=40).grid(row=3,column=1)
    button_2 = Button(window2,text="SUBMIT",width=10,command=lambda: finish()).place(relx=0.5,rely=0.74,anchor=CENTER)




def user_login():
    if name_var.get() == "xyz" and pass_var.get() == "password":
        registration()
    else:
       L3 = Label(window,text="Username or Password is incorrect, Try Again!",font="Helvetica 12",fg="red").place(relx=0.5, rely=0.75, anchor=CENTER)

L1 = Label(window,text="Login",font="Helvetica 18 bold").place(relx=0.5, rely=0.09, anchor=CENTER)
L2 = Label(window,text="Username: ",font="Helvetica 12").grid(pady=(40,10),row=0,column=0)
E1 = Entry(window,width=40,textvariable = name_var).grid(pady=(40,10),row=0,column=1)
L3 = Label(window,text="Password: ",font="Helvetica 12").grid(row=1,column=0)
E2 = Entry(window,width=40,textvariable = pass_var).grid(row=1,column=1)
button_1 = Button(window,text="SUBMIT",width=10,command=lambda: user_login()).place(relx=0.5,rely=0.92,anchor=CENTER)
window.mainloop()
