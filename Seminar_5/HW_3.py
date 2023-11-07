'''
Создайте функцию генератор чисел Фибоначчи fibonacci.
'''


def fibonacci():
    a = 0
    b = 1
    while (True):
        yield a
        a, b = b, a + b


f = fibonacci()
for i in range(10):
    print(next(f))
