import requests as r
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def image_dogs_in_tk():

def get_json_dog():
    api_answer = r.get('https://dog.ceo/api/breeds/image/random')
    json_dog = api_answer.json()
    return json_dog['message']
#_1_получает запрос по api и переводит в формат json

window = Tk()
window.geometry('500x400')
window.title('DoggyDogs')

label = Label(window)
label.pack()

btn = Button(window, text ='Get_a_Dog_of_your_Dream', command = image_dogs_in_tk)
btn.pack()

window.mainloop()


