import os
import json
import csv
import pickle
from pathlib import Path


def traverse_directory(directory: str, total_lst: list = None, is_branch: bool = False):
    if total_lst is None:
        total_lst = []
        #basic_path = os.path.split(os.path.abspath(directory))

        #lst_formatter(total_lst, os.path.abspath(directory), os.path.join(*basic_path[:-1]), basic_path[-1], 'D')

    for item in os.listdir(directory):
        check_path = os.path.join(directory, item)
        if os.path.isfile(check_path):
#            lst_formatter(total_lst, check_path, directory, item, 'F')
            total_lst.append(dict(Path=check_path,
                                  Type='File',
                                  # object_name=item_name,
                                  Size=os.path.getsize(os.path.join(directory, item)),
                                  parent_directory=os.path.split(directory)[-1]))

        elif os.path.isdir(check_path):
#            lst_formatter(total_lst, check_path, directory, item, 'D')
            total_lst.append(dict(Path=check_path,
                                  Type='Directory',
                                  # object_name=item_name,
                                  Size=count_size(os.path.join(directory, item)),
                                  parent_directory=os.path.split(os.path.abspath(directory))[-1]))
            traverse_directory(os.path.join(directory, item), total_lst, True)
    return total_lst


def lst_formatter(total_lst: list, full_path: str, path: str, item_name: str, item_type: str) -> None:
    if item_type == 'F':
        total_lst.append(dict(Path=full_path,
                              Type='File',
                              #object_name=item_name,
                              Size=os.path.getsize(os.path.join(path, item_name)),
                              parent_directory=os.path.split(path)[-1]))
    elif item_type == 'D':
        total_lst.append(dict(Path=full_path,
                              Type='Directory',
                              #object_name=item_name,
                              Size=count_size(os.path.join(path, item_name)),
                              parent_directory=os.path.split(os.path.abspath(path))[-1]))
    else:
        pass


def count_size(count_path: str, dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):

        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file)) for file in
                             sub_item[2]])  # размер всех файлов в директории

        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir)) for subdir in sub_item[1]])

    return dir_size


def save_results_to_json(data: list, path: str, file_name: str) -> None:  # запись словаря в json файл
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def save_results_to_csv(data_lst: list, path: str, file_name: str) -> None:  # запись словаря в csv файл
    file_path = os.path.join(path, file_name + '.csv')
    data = [['Path', 'object_type', 'object_name', 'object_size', 'parent_directory']]
    for _ in data_lst:
        new_lst = []
        for key, item in _.items():
            new_lst.append(item)
        data.append(new_lst)
    #print(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, dialect='excel', delimiter=' ')
        write_csv.writerows(data)


def save_results_to_pickle(data: list, path: str, file_name: str) -> None:  # запись словаря в pickle файл
    file_path = os.path.join(path, file_name + '.pickle')
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

results = traverse_directory(directory=str(Path.cwd()) + '\\directory')
print(results)
save_results_to_json(results, os.getcwd(), 'result')
save_results_to_csv(results, os.getcwd(), 'result')
save_results_to_pickle(results, os.getcwd(), 'result')
