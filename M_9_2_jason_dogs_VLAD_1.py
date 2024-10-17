import requests as r
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def image_dogs_in_tk():
    url_image = get_json_dog()
#_4_присваиваем адрес переменной url_image


def get_json_dog():
    api_answer = r.get('https://dog.ceo/api/breeds/image/random')
    json_dog = api_answer.json()
    return json_dog['message']

#_1_получаем ответ на наш запрос-request по api и ответ запоминаем в переменной
#_2_json получаем из ответа (message : значение, status : success)
#_3_возвращаем на функцию адрес - значение по ключу message

window = Tk()
window.geometry('500x400')
window.title('DoggyDogs')


label = Label(window)
label.pack()

btn = Button(window, text ='Get_a_Dog_of_your_Dream', command = image_dogs_in_tk)
btn.pack()

window.mainloop()


