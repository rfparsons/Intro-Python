"""
Program: gui_assignment.py
Author: Bobby Parsons

Program that displays a GUI asking what your favorite meal of the day is
"""
import tkinter
from tkinter import messagebox

def guess():
    messagebox.showinfo("number_guessed", "You win!")

m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
one_button = tkinter.Button(m, text='1', width=25, command=guess)
one_button.grid(row=1)
two_button = tkinter.Button(m, text='2', width=25, command=guess)
two_button.grid(row=1)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen