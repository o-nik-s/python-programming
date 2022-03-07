# Напишите программу, на вход которой подаётся прямоугольная матрица в виде
# последовательности строк, заканчивающихся строкой, содержащей только строку
# "end" (без кавычек)
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент
# в позиции i, j равен сумме элементов первой матрицы на позициях
# (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент
# находится с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является соседом
# по соответствующему направлению.

str = input()
i = 0
a = []
while str != "end":
    # str = str.split()
    a.append(str.split())
    # a[0].append(str.split())
    str = input()
    i += 1
rows = len(a)
columns = len(a[0])
a = [[int(a[i][j]) for j in range(columns)] for i in range(rows)]
# print(a)
b = [[0 for j in range(columns)] for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        if 1 <= i:
            b[i][j] += a[i-1][j]
        else:
            b[i][j] += a[rows-1][j]
        if i <= rows - 2:
            b[i][j] = b[i][j] + a[i+1][j]
        else:
            b[i][j] += a[0][j]
        if 1 <= j:
            b[i][j] += a[i][j-1]
        else:
            b[i][j] += a[i][columns-1]
        if j <= columns - 2:
            b[i][j] = b[i][j] + a[i][j+1]
        else:
            b[i][j] += a[i][0]
# print(b)
for i in range(rows):
    for j in range(columns):
        print(b[i][j], end=" ")
    print()
