'''
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов
    внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся
    буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
'''

import os


def rename_files(desired_name, num_digits, source_ext, target_ext):
    test_folder = "test_folder"
    file_list = [file.split('.') for root, dirs, files
                 in os.walk(test_folder) for file in files]

    print(file_list)
    numr = 1
    for (name, ext) in file_list:
        if ext == source_ext:
            initial_full_name = os.path.join(test_folder, name) + '.' + ext
            changed_name = os.path.join(test_folder, desired_name + f'{numr:0{num_digits}}')
            changed_ext = target_ext
            numr += 1
            print(f'{initial_full_name} --> {changed_name}.{changed_ext}')
            # os.rename()


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
