'''
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
и возвращает транспонированную матрицу.
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for j in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed


transposed_matrix = transpose(matrix)
print(transposed_matrix)
print(transpose(matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]))
