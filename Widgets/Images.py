from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.title("Image Window")
window.geometry('800x800')

image1 = Image.open("bg.jpg")

imageupload = ImageTk.PhotoImage(image1)
def display():

    global Message
    message= "Congrats on pressing the button!" + "\n"

    textbox.insert(END,message)

lbl = Label(window, image=imageupload, height=280, width=250)
btn = Button(window, command=display, text="Click Here", bg="lightgreen")
textbox = Text(window, height=5, width=50)
textbox.insert(END, "Image has been inserted")

lbl.pack()
btn.pack()
textbox.pack()

window.mainloop()
