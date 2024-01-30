'''
Семинар #15.
Промежуточная аттестация

Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

Взято задание 1 из семинара 6:

Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая
проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в
зависимости от результата проверки.
'''
import logging
import argparse

# описываем формат логгера

logging.basicConfig(filename='Logs/log_HW_1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno}" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# декоратор логирования для ф-ии check_date из прошлых задач, саму функцию не меняем, только оборачиваем в декоратор
def decor(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError:
            logger.error(f'Ошибка ValueError в функции: {func.__name__}() - введен некорректный аргумент {args}')
            return 'Обнаружена ошибка, посмотрите лог Logs/log_HW_1.log'
        else:
            logger.info(f'Выполнена функция: {func.__name__}() аргументы функции: {args}, результат функции: {result}')
        return result

    return wrapper

# копируем функцию из прошлых задач. Импортировать не стал, чтобы не было проблем с запуском
@decor
def check_date(date_string):
    day, month, year = date_string.split('.')

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False
    else:
        return False

    if not (1 <= month <= 12):
        return False

    if year <= 0:
        return False
    return True

if __name__ == '__main__':

    # получение аргументов из командной строки
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('numbers', metavar='N', type=str, nargs='*', help='press some numbers')
    args = parser.parse_args()
    logger.info(f'Программой получены аргументы {args}')

    print(check_date(args.numbers[0])) # проверка на переданных из строки запуска аргументах

    # теперь проверим на предустановленных внутри программы данных

    print(check_date('12.13.9999')) # некорректная дата --> False
    print(check_date('01.02.2024')) # корректная дата   --> True
    print(check_date('sdsds'))      # вообще не дата    --> False
