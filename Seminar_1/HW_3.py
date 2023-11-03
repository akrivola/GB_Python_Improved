list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2

print("Количество совпадающих чисел:", len(common_elements))