import tkinter as tk
import pygame

from PIL import Image as Pilimage
from PIL import ImageTk

# Константы
VER = 0.02
WIDTHWIN = 600
HEIGTHWIN = 600
X = 0
Y = 0

# Кортеж с английскими буквами
ENG_ALPHABET = ('Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj',
                'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt',
                'Uu', 'Vv', "Ww", 'Xx', 'Yy', 'Zz')
# Словарь где ключ это английская буква а значение цифра которая означает индекс картинке в списке list_image
tople_eng_alphabet = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
    's': 18, 't': 19, 'u': 20, 'v': 21, "w": 22, 'x': 23, 'y': 24, 'z': 25
}
# Список в котором сохраняются объекты картинок
list_image = []
# Список в котором сохраняется объекты КНОПКИ с буквами алфавита
list_buttot_alphabet = []

delete_addit = False
img_addit = None
audi_addit = None

def create_additional(event):
    global delete_addit, img_addit, audi_addit
    text = event.widget['text']
    print(text)
    if delete_addit:
        img_addit.grid_forget()
        audi_addit.grid_forget()
        img_addit = tk.Label(win_additional, image=list_image[tople_eng_alphabet[text[-1]]])
        audi_addit = tk.Button(win_additional, image=img_audio)
        img_addit.grid()
        audi_addit.grid()
    else:
        img_addit = tk.Label(win_additional, image=list_image[tople_eng_alphabet[text[-1]]])
        audi_addit = tk.Button(win_additional, image=img_audio)
        img_addit.grid()
        audi_addit.grid()
        delete_addit = True

def start_audio(event, letter):
    pass


# Настройка окна
win = tk.Tk()
win.title(f'Учебник по Английскому v{VER}')
win.geometry(f'{WIDTHWIN}x{HEIGTHWIN}+{X}+{Y}')
win.resizable(False, False)
win.iconbitmap('img_prog/icon/eng_icon.ico')

# Настройка разделения окна
win_main = tk.LabelFrame(win, text='Алфавит', width=WIDTHWIN / 3 * 2, height=HEIGTHWIN) # bg='red' width=WIDTHWIN / 3 * 2, height=HEIGTHWIN
win_main.grid(row=0, column=0, sticky=tk.N, padx=10, )
win_additional = tk.LabelFrame(win, text='Транскрипция', width=WIDTHWIN / 3, height=HEIGTHWIN) # bg='blue' width=WIDTHWIN / 3 * 2, height=HEIGTHWIN
win_additional.grid(row=0, column=1)

img_audio = Pilimage.open('img_prog/image/audi.png')
img_audio = ImageTk.PhotoImage(img_audio)

number = 0
for leb in ENG_ALPHABET:
    # Сохранение объектов изображений в списках
    img = Pilimage.open(f'img_prog/translete/{leb[-1]}.PNG')
    img = img.resize((250, 60))
    img_tk = ImageTk.PhotoImage(img)
    list_image.append(img_tk)

    # Создание объектов КННОПКИ для каждой буквы алфавита
    lebl = tk.Button(master=win_main, text=leb, relief=tk.SUNKEN,  width=2,)
    lebl.bind('<Button-1>', create_additional)
    list_buttot_alphabet.append(lebl)
    number += 1

# Выведение созданых кнопок по заданным координатам
row = 0
column = 0
for but in list_buttot_alphabet:
    but.grid(row=row, column=column, padx=2, pady=3)
    column += 1
    if column == 10:
        row += 1
        column = 0

win.mainloop()