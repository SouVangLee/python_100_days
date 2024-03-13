from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

WHITE = "#FFFFFF"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.config(bg=WHITE)
window.minsize(width=600, height=400)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(LETTERS) for _ in range(nr_letters)]
    password_symbols = [choice(SYMBOLS) for _ in range(nr_symbols)]
    password_numbers = [choice(NUMBERS) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_or_username_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all fields!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email}"
            f"\nPassword: {password} \nIs it ok to save?",
        )
    

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

website_label = Label(text="Website: ", font=("Serif", 12), bg=WHITE)
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_or_username_label = Label(text="Email/Username: ", font=("Serif", 12), bg=WHITE)
email_or_username_label.grid(row=2, column=0)

email_or_username_input = Entry(width=35)
email_or_username_input.grid(row=2, column=1, columnspan=2)
email_or_username_input.insert(END, "random_email@somewhere.com")

password_label = Label(text="Password: ", font=("Serif", 12), bg=WHITE)
password_label.grid(row=3, column=0)

password_input = Entry(width=16)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
