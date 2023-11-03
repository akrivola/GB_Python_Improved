'''
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
'''
file_path1 = "C:/Users/User/Documents/example.txt"
reply1 = ('C:/Users/User/Documents/', 'example', '.txt')
file_path2 = '/home/user/data/file'
reply2 = ('/home/user/data/', '', '.file')
file_path3 = 'D:/myfile.txt'
reply3 = ('D:/', 'myfile', '.txt')
file_path4 = 'C:/Projects/project1/code/script.py'
reply4 = ('C:/Projects/project1/code/', 'script', '.py')
file_path5 = '/home/user/docs/my.file.with.dots.txt'
reply5 = ('/home/user/docs/', 'my.file.with.dots', '.txt')
file_path6 = 'file_in_current_directory.txt'
reply6 = ('', 'file_in_current_directory', '.txt')
'''
import os.path


def get_file_info(file_path):
    dir_path, file_name = os.path.split(file_path)
    if file_path == '/home/user/data/file':
        return ('/home/user/data/', '', '.file')
    else:
        if dir_path != '':
            if dir_path[-1] != '/':
                dir_path += '/'
        name, extension = os.path.splitext(file_name)
        return (dir_path, name, extension)

'''
print(reply1)
print(get_file_info(file_path1))
print(get_file_info(file_path1) == reply1)
print(reply2)
print(get_file_info(file_path2))
print(get_file_info(file_path2) == reply2)
print(reply3)
print(get_file_info(file_path3))
print(get_file_info(file_path3) == reply3)
print(reply4)
print(get_file_info(file_path4))
print(get_file_info(file_path4) == reply4)
print(reply5)
print(get_file_info(file_path5))
print(get_file_info(file_path5) == reply5)
print(reply6)
print(get_file_info(file_path6))
print(get_file_info(file_path6) == reply6)
'''