'''
Лотерея Класс

На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать
числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.
'''


class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        count = 0
        matching_numbers = []
        for number in list1:
            if number in list2:
                count += 1
                matching_numbers.append(number)
        if count == 0:
            print("Совпадающих чисел нет.")
        else:
            print("Совпадающие числа:", matching_numbers)
            print("Количество совпадающих чисел:", len(matching_numbers))


# Пример использования:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
