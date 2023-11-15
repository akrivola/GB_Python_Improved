'''
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные
варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной
 вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
'''
from random import randint


def generate_boards():
    board_list = []
    while len(board_list) < 4:
        board = []
        i = 0
        overload = False
        while len(board) < 8:
            i += 1
            x = randint(1, 8)
            y = randint(1, 8)
            if all(x != c[0] and y != c[1] and abs(x - c[0]) != abs(y - c[1]) for c in board):
                board.append((x, y))
            if i > 1000:
                overload = True
                break

        if not overload and not board in board_list:
            board_list.append(board)
    return board_list


board_list = generate_boards()
print(board_list)
for i in board_list:
    print(len(i), i)
