'''
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные
варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной
 вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
'''
from random import randint
from itertools import combinations


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


def get_new_queen():
    return randint(1, 8), randint(1, 8)


board_list = []
while True:
    new_set = []
    for i in range(8):
        new_set.append(get_new_queen())
    print(check_queens(new_set))
    if check_queens(new_set) == False:
        continue
    else:
        break

print(new_set)
print(check_queens(new_set))