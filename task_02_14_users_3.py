n = int(input())
matrix = [[0 for l in range(n)] for i in range(n)]  # строим пустую матрицу

l, t, r, b = 0, 0, n, n
x = 1
while x <= n**2:
    for i in range(l, r, 1):        # заполняем верх
        matrix[t][i] = x
        x += 1
    t += 1
    for i in range(t, b, 1):        # заполняем право
        matrix[i][r-1] = x
        x += 1
    r -= 1
    for i in range(r-1, l-1, -1):   # заполняем низ
        matrix[b-1][i] = x
        x += 1
    b -= 1
    for i in range(b-1, t-1, -1):   # заполняем лево
        matrix[i][l] = x
        x += 1
    l += 1

for x in matrix:
    print(*x)
