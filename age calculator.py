##########Python Age calculator using tkinter#########

# importing necessary libraries 

import tkinter
from tkinter import *
from tkinter import messagebox

import datetime
from datetime import date

# Creating clearAll function for clearing the contents of entry boxes
def clearAll():
    dayfield.delete(0, END)
    monthfield.delete(0,END)
    yearfield.delete(0, END)
    rslagefield.delete(0,END)
 
# Creating checkError function for display the Error if any entry box is empty
def checkError():
    if(dayfield.get()=="" or monthfield.get()=="" or yearfield.get()==""):
        messagebox.showerror('Input Error')
        return -1

# Creating GUI window
gui=Tk()
# Title of the GUI window
gui.title('Age Calculator')    
gui.geometry('550x280')

#Age calculator function
def calAge():
    value=checkError()
    
    if value==-1:
        return
    else:
        today=date.today()
        birthdate=date(int(yearfield.get()),
                       int(monthfield.get()), 
                       int(dayfield.get()))
        age=today.year-birthdate.year-((today.month, today.day)<(birthdate.month, birthdate.day))
        rslagefield.insert(10, str(age)) 

# Creating labels for Entry boxes
Label(text='Enter your Birth date: ').grid(row=1, column=1)
Label(text='Year').grid(row=2, column=0, padx=90)
Label(text='Month').grid(row=3, column=0)
Label(text='Day').grid(row=4, column=0)
Label(text='Your age is : ').grid(row=8, column=0)

# Creating text enty boxes for filling information
yearfield=Entry(gui)
monthfield=Entry(gui)
dayfield=Entry(gui)
rslagefield=Entry(gui)

# Pleasing the widgets at respective positions by using grid method
yearfield.grid(row=2, column=1)
monthfield.grid(row=3, column=1)
dayfield.grid(row=4, column=1)
rslagefield.grid(row=8, column=1)

# Creating buttons for claculating age and clearing the boxes
Button(text='Calculated age', command=calAge, bg='green').grid(row=6, column=1,pady=10)
Button(text='Clear All', bg='red', command=clearAll).grid(row=9, column=1, pady=10)

gui.mainloop()
        