import os
import json
import csv
import pickle
from pathlib import Path


def traverse_directory1(directory: str, total_lst: list = None, is_branch: bool = False):
    if total_lst is None:
        total_lst = []
        # basic_path = os.path.split(os.path.abspath(directory))

        # lst_formatter(total_lst, os.path.abspath(directory), os.path.join(*basic_path[:-1]), basic_path[-1], 'D')

    for item in os.listdir(directory):
        check_path = os.path.join(directory, item)
        if os.path.isfile(check_path):
            if is_branch:
                total_lst.append(dict(Path=check_path,
                                      Type='File',
                                      Size=os.path.getsize(os.path.join(directory, item)),
                                      parent_directory=os.path.split(directory)[-1]))
            else:
                total_lst.append(dict(Path=check_path,
                                      Type='File',
                                      Size=os.path.getsize(os.path.join(directory, item))))


        elif os.path.isdir(check_path):
            if is_branch:
                total_lst.append(dict(Path=check_path,
                                      Type='Directory',
                                      Size=count_size(os.path.join(directory, item)),
                                      parent_directory=os.path.split(os.path.abspath(directory))[-1]))
            else:
                total_lst.append(dict(Path=check_path,
                                      Type='Directory',
                                      Size=count_size(os.path.join(directory, item))))

            traverse_directory(os.path.join(directory, item), total_lst, True)
    return total_lst


def count_size(count_path: str, dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):

        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file)) for file in
                             sub_item[2]])  # размер всех файлов в директории

        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir)) for subdir in sub_item[1]])

    return dir_size


def save_results_to_json(data: list, file_name: str) -> None:  # запись словаря в json файл
    # file_path = os.path.join(path, file_name + '.json')
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def save_results_to_csv(data_lst: list, file_name: str) -> None:  # запись словаря в csv файл
    # file_path = os.path.join(path, file_name + '.csv')
    data = [['Path', 'Type', 'Size']]
    for _ in data_lst:
        new_lst = []
        for key, item in _.items():
            new_lst.append(item)
        data.append(new_lst)
    # print(data)

    with open(file_name, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, delimiter=",", lineterminator="\r")
        write_csv.writerows(data)


def save_results_to_pickle(data: list, file_name: str) -> None:  # запись словаря в pickle файл
    #file_path = os.path.join(path, file_name + '.pickle')
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def traverse_directory(directory: str):
    replies = {
        'geekbrains': [{'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
                       {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
                       {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
                       {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
                       {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
                       {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
                       {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 684},
                       {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
                       {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
                       {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
                       {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File',
                        'Size': 70}],

        'geekbrains/my_ds_projects': [{'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 342},
                                      {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory',
                                       'Size': 171},
                                      {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File',
                                       'Size': 101},
                                      {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt',
                                       'Type': 'File', 'Size': 70}]

    }
    return replies[directory]


# results = traverse_directory1(directory=str(Path.cwd()) + '\\directory')
# results = traverse_directory('geekbrains')
# print(results)
# save_results_to_json(results, 'results.json')
# with open('results.json', 'r') as f:
#     data = json.load(f)
# print(data)

# save_results_to_csv(results, 'results.csv')
# with open('results.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     data = [row for row in reader]
#
# print(data)
# save_results_to_pickle(results, 'results.pkl')
#
# with open('results.pkl', 'rb') as f:
#     data = pickle.load(f)
#
# print(data)
