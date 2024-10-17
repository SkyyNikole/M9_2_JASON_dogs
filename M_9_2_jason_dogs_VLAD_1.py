import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.geometry('500x400')
window.title('DoggyDogs')

label = Label(window)
label.pack()

btn = Button(window, text ='Get_a_Dog_of_your_Dream')
btn.pack()

window.mainloop()


