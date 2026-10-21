from tkinter import *
from tkinter import messagebox
import random
import json

#---------------------------- search mechnism -----------------------------------#
def search_password():

    try:
        data_file = open("data.json", "r")

    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found")

    else:
        data_dict = json.load(data_file)
        searched_entry = website_entry.get()
        try:
            email = data_dict[searched_entry]["email"]
            password = data_dict[searched_entry]["password"]
        except :
            messagebox.showinfo(message=f"No details for website: {searched_entry}")
        else:
            messagebox.showinfo(title=searched_entry, message=f"Email; {email}\npassword: {password}")

    finally:
        data_file.close()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for j in range(nr_numbers)]
    password_list += [random.choice(symbols) for k in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()

    new_data = {
        website: {
           "email": email,
            "password": password
        }
    }

    if password == "" or website == "":
        messagebox.showinfo(message="Dont leave any fields empty!!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\n"
                                                      f"Is the information ok?")

        if is_ok:
            try:
                with open(r"data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                #creating the json file
                with open(r"data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # updating old data with new data
                data.update(new_data)
                with open(r"data.json", "w") as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                password_entry.delete(0, "end")
                website_entry.delete(0,"end")
                website_entry.focus()
                messagebox.showinfo(message="Sucessfully Added")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200 )
logo_path = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_path)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",fg="black")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", fg="black")
email_label.grid(row=2,column=0)

email_entry = Entry(width=35)
email_entry.insert(END,string="adarsheluri143@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password", fg="black")
password_label.grid(row=3,column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1, columnspan=2)

Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4,column=1, columnspan=2)

search_button = Button(text="search", command=search_password)
search_button.grid(row=1, column=2)


window.mainloop()