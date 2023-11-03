'''
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''
lst = [1, 1, 2, 2, 3, 3]

def find_duplicates(lst):
    result = []
    for el in lst:
        if lst.count(el) > 1 and result.count(el) == 0:
            result.append(el)
    return result

print(find_duplicates(lst))