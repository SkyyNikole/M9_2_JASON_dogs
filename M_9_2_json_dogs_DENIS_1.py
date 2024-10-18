from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Lovely_Doggies')
window.geometry('360x420')

label = Label(window)
label.pack(pady=10)

btn = Button(window, text ='Get_new_doggie', command = get_dog_image)
btn.pack(pady=10)

window.mainloop()