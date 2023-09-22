from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [ choice(letters) for char in range(randint(8, 10))]
    password_symbols = [ choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [ choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_pass():
    website_to_find = entry_website.get()
    # Check if the website exists in the dictionary
    try:
        with open(r"29-30_Day\passwords.json", "r") as file:
            # reading old data 
            data = json.load(file)       
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Oops", message="No Data in File")
    else:
        if website_to_find in data:
            # Retrieve the email and password for the website
            website_info = data[website_to_find]
            email = website_info["email"]
            password = website_info["password"]
            messagebox.showwarning(title=website_to_find, message=f"Email: {email}\n"f"Password: {password}")
        else:
            messagebox.showwarning(title="Oops", message=f"No Details for {website_to_find} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()
    new_data = {website: {
                    "email":email,
                    "password":password
                    }
                }

    if len(website) < 1 or len(password) < 1:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open(r"29-30_Day\passwords.json", "r") as file:
                # reading old data 
                data = json.load(file)
        except FileNotFoundError:
            with open(r"29-30_Day\passwords.json", "w") as file:
                # create a new data file
                json.dump(new_data, file, indent=4)
        except json.decoder.JSONDecodeError:
            with open(r"29-30_Day\passwords.json", "w") as file:
                # create a new data file
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data  
            data.update(new_data)
            with open(r"29-30_Day\passwords.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally: 
            entry_website.delete(0, END)
            entry_password.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady= 50)

# Canvas
canvas = Canvas(width= 200, height=200)
logo = PhotoImage(file=r"29-30_Day\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, sticky=EW)

# Lables
lable_website = Label(text="Website:")
lable_website.grid(column=0, row=1, sticky=EW)
lable_website.config(padx=5, pady= 5)

lable_email_username = Label(text="Email/Username:")
lable_email_username.grid(column=0, row=2, sticky=EW)
lable_email_username.config(padx=5, pady= 5)

lable_password = Label(text="Password")
lable_password.grid(column=0, row=3, sticky=EW)
lable_password.config(padx=5, pady= 5)

# Buttons
button_generate_pass = Button(text="Generate Password", command= generate_pass)
button_generate_pass.grid(column=2, row=3, sticky=EW)
button_generate_pass.config(padx=5, pady= 5)

button_add = Button(text="ADD", width=36, command=save_pass)
button_add.grid(column=1, row=4, columnspan=2, sticky=EW)
button_add.config(padx=5, pady= 5)

button_search = Button(text="Search", command=search_pass)
button_search.grid(column=2, row=1, sticky=EW)
button_search.config(padx=5, pady= 5)

# Entry boxs
entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, sticky=EW)
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.grid(column=1, row=2, columnspan=2, sticky=EW)
entry_email_username.insert(0, "rishabhfriends8@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, sticky=EW)



windows.mainloop()
