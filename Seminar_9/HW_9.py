'''
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
'''
import csv
import json
import random
import math
import functools


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            writer.writerow([random.randint(1, 100) for _ in range(3)])


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def from_csv_decorator(func):
    @functools.wraps(func)
    def wrapper(filename):
        results = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                results.append([a, b, c, func(a, b, c)])
        return results

    return wrapper


def save_to_json(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        # data = {
        #     "result": result
        # }

        with open("results.json", 'w') as jsonfile:
            json.dump(result, jsonfile, indent=4)

    return wrapper


@save_to_json
@from_csv_decorator
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = (-b) / (2 * a)
        return x1
    else:
        return None


generate_csv_file("input_data.csv", 1500)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==1500)
