import time
from tkinter import *

def live():
    tm = time.strftime("%H:%M:%S")
    label.config(text=tm)
    label.after(1000, live)
    
root = Tk()
root.title("Cool Clock")

label = Label(root, font=("", 100, "bold"),
              background="black", foreground="green")
label.pack(anchor="center")
live()
mainloop()
