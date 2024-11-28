""" UPDATE: Updated code in Day 30 of Python"""

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    r_letters = [random.choice(letters) for _ in range(nr_letters)]
    r_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    r_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = r_letters + r_symbols + r_numbers
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)  # copies password into clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()  # gets entered data from website text-box
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please make sure to enter website and password.")
    else:
        try:
            with open("data.json", "r") as data_file:           # opens a file and reads the data
                data = json.load(data_file)                     # Reading old data

        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)                               # Updating old data with new data

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

""" Canvas """
canvas = Canvas(window, width=200, height=200, bg="white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

""" Labels """
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)

""" Entries """
website_entry = Entry(width=35, bg="white", fg="black")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35, bg="white", fg="black")
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "test@gmail.com")

password_entry = Entry(width=21, bg="white", fg="black")
password_entry.grid(column=1, row=3, columnspan=1)

""" Generate Password """
generate_password = Button(text="Generate Password", bg="white", fg="black", command=gen_password)
generate_password.grid(column=2, row=3)

""" Add Button """
add_button = Button(text="Add", bg="white", fg="black", font=("Arial", 15), width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
