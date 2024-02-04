'''
Напишите код, который запускается из коммандной строки и получает на вход
путь до директории на ПК
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл, используя
логгирование.
'''
import os
import logging
from collections import namedtuple

logging.basicConfig(filename='HW_6.log',
                    format='{levelname} - {asctime} : {msg}',
                    filemode='w',
                    encoding='utf-8',
                    style='{',
                    level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def process_directory(directory_path, parent_directory):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            name, extension = os.path.splitext(item)
            file_info = FileInfo(name, extension, False, parent_directory)
            logging.info(f'File info: {file_info}')
        elif os.path.isdir(item_path):
            directory_info = FileInfo(item, '', True, parent_directory)
            logging.info(f'Directory info: {directory_info}')
            process_directory(item_path, item)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        process_directory(directory_path, os.path.basename(os.path.dirname(directory_path)))
    else:
        print("Usage: python file_info.py <directory_path>")