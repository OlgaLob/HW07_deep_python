# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from string import ascii_letters
from random import randint, sample, randbytes
from pathlib import Path
import os


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))
        print(names)
    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


def makefiles(**extentions):
    for extention, count in extentions.items():
        makefile(extention=extention, count=count)


def makefile_to_path(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extention)


def replace_files():
    for file in os.listdir():
        extention = file.split('.')[-1]
        if not os.path.exists(extention):
            os.mkdir(extention)
        os.replace(file, os.path.join(os.getcwd(), extention, file))


makefiles(mp3=3, txt=2)
replace_files()
