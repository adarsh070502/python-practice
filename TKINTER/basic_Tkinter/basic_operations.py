from tkinter import *

# Window
window = Tk()
window.title("My First GUI application.")
window.wm_minsize(width=500, height=300)

# Lable
my_label = Label(text="My first Line", font=("Arial", 24))
my_label.pack()


# Button
def clicked():
    str1 = entry.get()
    my_label.config(text=str1)


button = Button(text="click me", command=clicked)
button.pack()

# Entry
entry = Entry()
entry.insert(END, string="Some entry text")
entry.pack()

#text box
text = Text(height=5, width=30)
text.focus()  #puts curser in text box
text.insert(END, "exampl of multline textbox")   # addd some text to begin with
print(text.get("1.0", END))  # here "1.0" is start at first line and character 0
text.pack()


#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
