from tkinter import *
import requests as r
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb

#_1 функция для получения изображения из интернета и вывода
# на экран пользователя, сайт dog.ceo присылает не саму картинку,
# а ссылку на нее, то сначала мы получим ссылку image_url (та ссылка,
# которая возвращает нам в формате json наш сайт dog.ceo)
def show_dog_image():
    image_url = get_dog_image()
    if image_url:
        try:
            respond = r.get(image_url, stream = True)
#_1.1_в ответ получаем что-то загруженное по ссылке в image_url
            respond.raise_for_status()
#_1.2_получаем статус ответа (пригодится для обработки искл)
            img_data = BytesIO(respond.content)
#_1.3_загружаем содержание respond - по ссылке загрузили
# в двоичном коде изобр в img_data
            img = Image.open(img_data)
#_1.4_обрабатываем изобр с пом pillow
            img.thumbnail((300, 300))
            label.config(image=img)
            label.image=img
        except Exception as e:
                mb.showerror('Error!', 'Error type: {e}.')

window = Tk()
window.title('Lovely_Doggies')
window.geometry('360x420')

label = Label(window)
label.pack(pady=10)

btn = Button(window, text ='Get_new_doggie', command = show_dog_image)
btn.pack(pady=10)

window.mainloop()