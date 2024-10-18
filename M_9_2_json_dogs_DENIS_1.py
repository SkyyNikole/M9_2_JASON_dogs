from tkinter import *
from tkinter import ttk
import requests as r
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb


#_2_функция загрузки ссылки на изображения,
#_будем по ссылке обращаться к сайту dog.ceo
def get_dog_image():
    try:
        respond_json = r.get('https://dog.ceo/api/breeds/image/random')
#_2.1_ответ в виде json ({'message' : 'http - адрес изобр', 'status' : 'success'})
        respond_json.raise_for_status()
#_2.2_узнали статус, если ок = code 200, если 404 - page not found
        data = respond_json.json()
#_2.3_получили ответ в формате json и ниже возращаем https - значение ключа
        return data ['message']
    except Exception as e:
        mb.showerror('Error!', f'API request error : {e}.')
        return None
#_если ошибка, то возвращаем None - пустоту


#_1 функция для загрузки изображения из интернета в метку,
# сайт dog.ceo присылает не саму картинку,
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
            img = ImageTk.PhotoImage(img)
#_1.5_обрабатываем для tkinter
            label.config(image=img)
            label.image=img
        except Exception as e:
                mb.showerror('Error!', f'Image loading error: {e}.')
    prog_bar.stop()

def progress_bar_funct():
    prog_bar['value'] = 0.0
    prog_bar.start(30)
#3_один раз в 30 мл сек увелич
    window.after(3000, show_dog_image)

window = Tk()
window.title('Lovely_Doggies')
window.geometry('360x420')
window.iconbitmap('dog.ico')

label = ttk.Label(window)
label.pack(pady=10)

btn = ttk.Button(window, text ='GetA_New_Doggie', command = progress_bar_funct)
btn.pack(pady=10)

#_2_mode determinate - меняется в зависимости от value, уставн в функц выше
prog_bar = ttk.Progressbar(mode = 'determinate', length=300)
prog_bar.pack()

window.mainloop()