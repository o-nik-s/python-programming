n = int(input())
array, increment, k, x, y = [[0]*n for j in range(n)], (0, 1, 0, -1), 1, 0, -1
for i in range(1, 2*n):
    for j in range(1,(2*n-i+3)//2):
        x += increment[(i-1)%4]
        y += increment[i%4]
        array[x][y] = k
        k += 1
for i in range(n): print(*array[i])
