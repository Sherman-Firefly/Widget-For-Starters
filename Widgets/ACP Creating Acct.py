from tkinter import *

window=Tk()

window.title("Account Creation")
window.geometry('300x300')

def submit_form():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    affirm="Account Created!"
    textbox.insert(END,affirm)

Label(window, text="Create Account", font=("Arial", 16)).pack(pady=10)

Label(window, text="Username:").pack(anchor=W, padx=10)
username_entry = Entry(window, width=30)
username_entry.pack(padx=10)

Label(window, text="Password:").pack(anchor=W, padx=10)
password_entry = Entry(window, width=30, show='*')
password_entry.pack(padx=10)

Label(window, text="Email:").pack(anchor=W, padx=10)
email_entry = Entry(window, width=30)
email_entry.pack(padx=10)
textbox=Text(height=6)

submit_btn = Button(window, text="Submit", command=submit_form)
submit_btn.pack(pady=10)
textbox.pack()
window.mainloop()