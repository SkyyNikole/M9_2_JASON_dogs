import requests as r
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def progress_bar_function():
    progress_bar


def image_dogs_in_tk():
    url_image = get_json_dog()
#_4_присваиваем адрес переменной url_image
    if url_image:
        answer_img = r.get(url_image)
        img = BytesIO(answer_img.content)
        img_for_tk = Image.open(img)
        img_for_tk.thumbnail((500,350))
        img_tk = ImageTk.PhotoImage(img_for_tk)
        label.config(image=img_tk)
        label.image = img_tk


def get_json_dog():
    api_answer = r.get('https://dog.ceo/api/breeds/image/random')
    json_dog = api_answer.json()
    return json_dog['message']

#_1_получаем ответ на наш запрос-request по api и ответ запоминаем в переменной
#_2_json получаем из ответа (message : значение, status : success)
#_3_возвращаем на функцию адрес - значение по ключу message

window = Tk()
window.geometry('500x450')
window.title('DoggyDogs')


label = ttk.Label(window)
label.pack(pady = (0,10))

btn = ttk.Button(window, text ='Get_a_Dog_of_your_Dream', command = image_dogs_in_tk)
btn.pack(pady = (0,10))

progress_bar = ttk.Progressbar(window, mode = 'determinate', length = 400)
progress_bar.pack()

window.mainloop()


