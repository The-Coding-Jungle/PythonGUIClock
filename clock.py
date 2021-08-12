#importing time to get realtime data for clock
import time
#importing everything from tkinter for GUI part of clock
from tkinter import *

'''live function is taking realtime data from time.strftime and setting 
label text as data. 1000ms or 1s is time to update
'''
def live():
    tm = time.strftime("%H:%M:%S")
    label.config(text=tm)
    label.after(1000, live)
    
#initializing tkinter, small gui window
root = Tk()
#Setting title of GUI window to Cool Clock, default is Tk
root.title("Cool Clock")

#Setting data for label. Setting font properties, background color and foreground color
label = Label(root, font=("", 100, "bold"),
              background="black", foreground="green")
label.pack(anchor="center")
#live function to get data and load in GUI, also updating time data 1000ms
live()
#mainloop from tkinter
mainloop()
