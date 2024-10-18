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
        #_print(data)
        #_print(data['message'])
        #_print(data['status'])
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
            img_size_from_spinbox = (int(width_sp.get()), int(height_sp.get()))
            img.thumbnail(img_size_from_spinbox)
#_4_1_вместо img.thumbnail((300, 300)) устанавливаем размер spb,
#_получаем .get(), string преобр в int
            img = ImageTk.PhotoImage(img)
# _1.5_обрабатываем для tkinter
            #_new_window = Toplevel(window)
            #_new_window.title('Carpe_Diem_Dog')
#_5.1_изменили 2 строки выше на:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f'Doggie {notebook.index('end') + 1}')
            #_new_window.iconbitmap('dog.ico')
            new_win_label = ttk.Label(tab, image=img)
#_5.2_отправляем не в new_window, а в tab (раньше было new_window на месте tab выше)
            new_win_label.pack(padx=10, pady=10)
            new_win_label.image = img
# помещали в label window (ниже коммент), a теперь в new_win_label (выше)
            #label.config(image=img)
            #label.image=img
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
prog_bar = ttk.Progressbar(window, mode = 'determinate', length=300)
prog_bar.pack()

#_4 и см 4.1 выше
width_l_spb = ttk.Label(window, text = 'Width')
width_l_spb.pack(side='left', padx=(10,0))
width_sp = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_sp.pack(side='left', padx=(0,10))
width_sp.set(250)

height_l_spb = ttk.Label(window, text = 'Height')
height_l_spb.pack(side='left', padx=(10,0))
height_sp = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_sp.pack(side='left', padx=(0,10))
height_sp.set(250)

#_5_создаем виджет notebook_картинки в закладках
toplevel_window = Toplevel(window)
toplevel_window.title('Dog_of_the_Day')
notebook = ttk.Notebook(toplevel_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)
#_fill = both - растягивается и по x и по y
window.mainloop()