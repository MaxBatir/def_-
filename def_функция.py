def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите количество строк матрицы:   '))
m = int(input('Введите количество столбцов матрицы:   '))
value = input('Введите значение матрицы:   ')
if n <=0:
    print('Неверное значение строк')
elif m <=0:
    print('Неверное значение столбцов')
else:
    print('Матрица готова:')
matrix = get_matrix(n, m, value)
print(matrix)
