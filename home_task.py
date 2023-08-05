# Напишите функцию группового переименования файлов. Она должна: ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер. ✔ принимать параметр количество цифр в порядковом
# номере. ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
# внутри каталога. ✔ принимать параметр расширение конечного файла. ✔ принимать диапазон сохраняемого оригинального
# имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое
# конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках # домашнего задания функций пакет для работы с файлами.
import os
import random
from pathlib import Path
from random import sample, randint, choice
from string import ascii_letters


def makefiles(nums):
    names = set()
    ext = ['doc', 'txt', 'mp3', 'md']
    for i in range(nums):
        names = f"{''.join(sample(ascii_letters, 10))}.{random.choice(ext)}"
        with open(names, 'w', encoding='utf-8') as file:
            file.write(names)


makefiles(10)


def rename_files(beg_ext, fin_ext, count_oldname, rename_file='', name_part=None):
    if name_part is None:
        name_part = [0, -1]
    count = 1
    path = os.getcwd()
    files = os.listdir(os.path.join(os.getcwd()))
    filtered_files = [f for f in files if f.endswith(beg_ext)]
    for i, file in enumerate(filtered_files, 1):
        old_name = os.path.splitext(file)[0][name_part[0]:name_part[1]]
        re_name = f'{old_name[count_oldname[0]:count_oldname[1]]}{rename_file}{count}.{fin_ext}'
        count += 1
        old_path = os.path.join(os.getcwd(), file)
        new_path = os.path.join(os.getcwd(), re_name)
        os.rename(old_path, new_path)


rename_files('mp3', 'bin', (3, 6), '00new00')
