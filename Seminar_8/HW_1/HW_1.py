import os
import json
import csv
import pickle
from pathlib import Path


def traverse_directory(directory: str, total_dct: dict = None) -> dict[str, dict[str]]:
    if total_dct is None:
        total_dct = {}
        basic_path = os.path.split(os.path.abspath(directory))                                           #('C:\\Users\\Алексей\\Desktop\\GreekBrains\\СЕМИНАРЫ\\Python_advanced', 'Seminar_8')

        dct_formatter1(total_dct, os.path.join(*basic_path[:-1]), basic_path[-1], 'D')


    for item in os.listdir(directory):
        check_path = os.path.join(directory, item)
        if os.path.isfile(check_path):
            dct_formatter1(total_dct, directory, item, 'F')
        elif os.path.isdir(check_path):
            dct_formatter1(total_dct, directory, item, 'D')
            traverse_directory(os.path.join(directory, item), total_dct)
    return total_dct
def dct_formatter1(total_dct: dict[str, dict[str]], path: str, item_name: str, item_type: str) -> None:
    if item_type == 'F':
        total_dct[path] = dict(object_type='File',
                               object_name=item_name,
                               object_size=os.path.getsize(os.path.join(path, item_name)),
                               parant_directory=os.path.split(path)[-1])
    elif item_type == 'D':
        total_dct[path] = dict(object_type='Directory',
                               object_name=item_name,
                               object_size=count_size(os.path.join(path, item_name)),
                               parant_directory=os.path.split(os.path.abspath(path))[-1])
    else:
        pass


def count_size(count_path: str, dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):

        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file))for file in sub_item[2]])  # размер всех файлов в директории

        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir))for subdir in sub_item[1]])

    return dir_size


def save_results_to_json(data_dict: dict, path: str, file_name: str) -> None:                             #запись словаря в json файл
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4)


def save_results_to_csv(data_dict: dict, path: str, file_name: str) -> None:                             #запись словаря в csv файл
    file_path = os.path.join(path, file_name + '.csv')
    data = [['Path', 'object_type',  'object_name', 'object_size', 'parant_directory']]
    for key, value in data_dict.items():
        data.append([key, *value.values()])
    #print(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, dialect='excel', delimiter=' ')
        write_csv.writerows(data)


def save_results_to_pickle(data_dict: dict, path: str, file_name: str) -> None:                                #запись словаря в pickle файл
    file_path = os.path.join(path, file_name + '.pickle')
    with open(file_path, 'wb') as f:
        pickle.dump(data_dict, f)



result = traverse_directory(directory=str(Path.cwd()) + '\\directory')
print(result)
#save_results_to_json(result, os.getcwd(), 'result')
#save_results_to_csv(result, os.getcwd(), 'result')
#save_results_to_pickle(result, os.getcwd(), 'result')