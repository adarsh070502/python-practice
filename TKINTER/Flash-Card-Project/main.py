from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


#----------------to remove known card from dicionary---------------

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv(r"data\word_to_learn.csv")
    next_card()

#----------------------english_word----------------------
def english_word():
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=cardback_file)

#-----------------------read data from csv file---------------------
try :
    data = pandas.read_csv(r"data\word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"data\french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
#-----------------generating random words ------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)
    canvas.itemconfig(Title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=cardfront_file)
    flip_timer = window.after(3000, func=english_word)

#----------------------- UI -------------------------------------

window = Tk()
window.title("Flas Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=english_word)

canvas = Canvas(width=800, height=526)
cardfront_file = PhotoImage(file=r"images\card_front.png")
cardback_file = PhotoImage(file=r"images\card_back.png")

card_background = canvas.create_image(400,263, image=cardfront_file)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
Title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel",40,"bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_file = PhotoImage(file=r"images\right.png")
right_button = Button(image=right_file, command=is_known)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_file = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_file, command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()