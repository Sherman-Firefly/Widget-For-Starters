from tkinter import *
import math
window=Tk()

window.title("Products")
window.geometry('300x300')

def submit_form():
    n1 = float(n1_entry.get())
    n2 = float(n2_entry.get())
    

    prodcut=n1*n2
    textbox.insert(END,prodcut)

Label(window, text="Product Calculator", font=("Arial", 16)).pack(pady=10)

Label(window, text="First Number:").pack(anchor=W, padx=10)
n1_entry = Entry(window, width=30)
n1_entry.pack(padx=10)

Label(window, text="Second Number:").pack(anchor=W, padx=10)
n2_entry = Entry(window, width=30)
n2_entry.pack(padx=10)

textbox=Text(height=6)

submit_btn = Button(window, text="Submit", command=submit_form)
submit_btn.pack(pady=10)
textbox.pack()
window.mainloop()