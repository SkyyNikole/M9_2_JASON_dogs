import requests as r
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def progress_bar_function():
    progress_bar.config(value = 0)
    progress_bar.start(25)
    window.after(3000, image_dogs_in_tk)
#_6

def image_dogs_in_tk():
    url_image = get_json_dog()
#_4_присваиваем адрес переменной url_image
    if url_image:
        answer_img = r.get(url_image)
        img = BytesIO(answer_img.content)
        img_for_tk = Image.open(img)
        img_for_tk.thumbnail((int(spinbox_var_w.get()), int(spinbox_var_h.get())))
        #_img_for_tk.thumbnail((500,450))
#_9_изменяем после создания spinboxes - из строки делаем (т.к вводим string в spinbox) interger,
#_и методом get получаем заданный пользователем размер для картинки
#_получаем их из _
        img_tk = ImageTk.PhotoImage(img_for_tk)
        label.config(image=img_tk)
        label.image = img_tk
    progress_bar.stop()


def get_json_dog():
    api_answer = r.get('https://dog.ceo/api/breeds/image/random')
    json_dog = api_answer.json()
    return json_dog['message']

#_1_получаем ответ на наш запрос-request по api и ответ запоминаем в переменной
#_2_json получаем из ответа (message : значение, status : success)
#_3_возвращаем на функцию адрес - значение по ключу message

window = Tk()
window.geometry('500x500')
window.title('DoggyDogs')


label = ttk.Label(window)
label.pack(pady = (0,10))

btn = ttk.Button(window, text ='Get_a_Dog_of_your_Dream', command = progress_bar_function)
btn.pack(pady = (0,10))
#_5 изменяем функцию в command кнопки с image_dogs_in_tk на
#_progress_bar_function после создания ниже progress_bar

spinbox_var_w = StringVar(value=250)
spinbox_var_h = StringVar(value=250)
#_8_значения по умолчанию для spinbox

progress_bar = ttk.Progressbar(window, mode = 'determinate', length = 400)
progress_bar.pack()

width_label = Label(window, text = 'Width')
width_label.pack()
width_img = ttk.Spinbox(window, from_=250, to=500, increment=50, textvariable=spinbox_var_w)
width_img.pack()

height_label = Label(window, text = 'Height')
height_label.pack()
height_img = ttk.Spinbox(window, from_=250, to=500, increment=50, textvariable=spinbox_var_h)
height_img.pack()
#_7_сначала labels для размера по ш и в, потом spinbox

window.mainloop()


