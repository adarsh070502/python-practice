from tkinter import *

def miles_to_km():
    mile = miles_input.get()
    km = int(mile) * 1.609
    Kilometer_result_label.config(text=km)

window = Tk()
window.title("Mile to Kilometer")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1 , row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2 ,row=0)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(column=0 ,row=1)

Kilometer_result_label = Label(text="0")
Kilometer_result_label.grid(column=1 ,row=1)

Kilometer_label = Label(text="km")
Kilometer_label.grid(column=2 ,row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1 ,row=2)



window.mainloop()