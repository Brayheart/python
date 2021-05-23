#####################################################
# CS 31, Prof. Muldrow
# Name: Tyler Bray
# Assignment: Chapter 13 Homework
# Due Date: Sunday March 23rd at 11:59PM PST
# ####################################################

import tkinter as tk

window = tk.Tk()
window.title('Long Distance Calls')
window.geometry('300x200')

var = tk.DoubleVar()

total = 0

def showcharges():
    totalCost.config(text=f'Total Cost: ${float(hours.get())*var.get():.2f}')

def showChoice():
    label.config(text=f'Hourly Rate: ${var.get():.2f}')


label = tk.Label(window, bg='white', width=20, text=f'Hourly Rate: ${var.get():.2f}')
hourslabel = tk.Label(window, bg='white', width=20, text='How many hours?')
hours = tk.Entry(window,textvariable = 10, font=('calibre',10,'normal'))
totalCost = tk.Label(window, bg='white', width=20, text=f'Total Cost: ${total:.2f}')
dis_button = tk.Button(window,text='Display Charges',command=showcharges)

tk.Radiobutton(window, text="Daytime (6:00AM - 5:59PM)",padx = 20, variable=var, value=0.07,command=showChoice).pack(anchor=tk.W)
tk.Radiobutton(window, text="Evening (6:00PM - 11:59PM)",padx = 20, variable=var, value=0.12,command=showChoice).pack(anchor=tk.W)
tk.Radiobutton(window, text="Off-Peak (midnight through 5:59AM)",padx = 20, variable=var, value=0.05,command=showChoice).pack(anchor=tk.W)
label.pack()

hourslabel.pack()
hours.pack()
dis_button.pack()
totalCost.pack()

window.mainloop()