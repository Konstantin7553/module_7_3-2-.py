import os
import time

directory = r'C:\Users\konst\PycharmProjects\pythonProject2'
if os.path.isdir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formated_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.relpath(root, start=directory)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formated_time},Родительская директория: {parent_dir}')

