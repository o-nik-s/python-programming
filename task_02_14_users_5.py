n = int(input())
a = 1
w = 0
h = 0
result = [[0 for j in range(n)] for i in range(n)]
while a <= n ** 2:
    while w < n and result[h][w] == 0:
        result[h][w] = a
        a += 1
        w += 1
    w -= 1
    h += 1

    # print(h,w,result)
    while h < n and result[h][w] == 0:
        result[h][w] = a
        a += 1
        h += 1
    w -= 1
    h -= 1

    while w >= 0 and result[h][w] == 0:
        result[h][w] = a
        a += 1
        w -= 1
    h -= 1
    w += 1
    while h >= 0 and result[h][w] == 0:
        result[h][w] = a
        a += 1
        h -= 1
    w += 1
    h += 1
for i in range(n):
    print()
    for j in range(n):
        print(result[i][j], end=' ')

