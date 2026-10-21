from tkinter import *


def clicked():
    str1 = entry.get()
    my_label.config(text=str1)


# Window
window = Tk()
window.title("My First GUI application.")
window.wm_minsize(width=500, height=300)

# Lable
my_label = Label(text="My first Line", font=("Arial", 24))
my_label.grid(column = 0, row=0)

# Entry
entry = Entry()
entry.insert(END, string="Some entry text")
entry.grid(column=6, row=4)

# Button

button1 = Button(text="click me", command=clicked)
button1.grid(column=2, row=10)

button2 = Button(text = "click you", command =clicked)
button2.grid(column=10,row=0)
window.mainloop()
