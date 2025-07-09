from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

random_password = ''
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="please don't leave any fields empty!")
    else:
        try:
            with open('password_manager/data.json', 'r') as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('password_manager/data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open('password_manager/data.json', 'w') as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    try:
        with open('password_manager/data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="There is no password for that website.")
    else:
        website = website_entry.get()
        try:
            email = data[f"{website}"]["email"]
            password = data[f"{website}"]["password"]
            messagebox.showinfo(title="Found password", message=f"Your Email and pasword for {website} is: \nEmail: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showinfo(title="Password NOT found", message=f"No password saved for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_text = Label(text='Website:')
website_text.grid(column=0, row=1)

website_entry = Entry(width=27)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_text = Label(text='Email/Username:')
user_text.grid(column=0, row=2)

user_entry = Entry(width=45)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, 'jellepelle213@hotmail.com')

password_text = Label(text='Password:')
password_text.grid(column=0, row=3)

password_entry = Entry(width=27)
password_entry.insert(END, string=f'{random_password}')
password_entry.grid(column=1, row=3)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14 , command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
