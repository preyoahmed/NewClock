
import sys
from tkinter import *
import time
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(300, tick)

root = Tk()
clock=Label(root, font=("times", 50, "bold"), bg= "red")
clock.grid(row=3, column=4)
tick()

mainloop ()
