from tkinter import *

window=Tk()

window.title("New Window")
window.geometry('300x300')

lbl=Label(text="Hi",fg="green", bg="white", height=0, width="200")
lbl2=Label(text="Full name", bg="lightblue")
nameentry=Entry()

def display():
    name=nameentry.get()

    global Message
    message= "This is a window, this is a test"

    greet="Welcome " + name + "\n"

    textbox.insert(END,greet)
    textbox.insert(END,message)

textbox=Text(height=6)

btn=Button(text="Press Here", command=display, height=4, bg="yellow", fg="grey")
lbl.pack()
lbl2.pack()
nameentry.pack()
textbox.pack()
btn.pack()
window.mainloop()