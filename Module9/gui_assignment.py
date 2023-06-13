"""
Program: gui_assignment.py
Author: Bobby Parsons

Program that displays a GUI asking what your favorite meal of the day is
"""
import tkinter

def breakfast():
    label.config(text="You picked: Breakfast")

def second_breakfast():
    label.config(text="You picked: Second Breakfast")

def lunch():
    label.config(text="You picked: Lunch")

def dinner():
    label.config(text="You picked: Dinner")

m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=breakfast).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=second_breakfast).grid(row=1)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=lunch).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=dinner).grid(row=4)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen