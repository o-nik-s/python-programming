# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке,
# как показано в примере (здесь n=5).

n = int(input())
a = [[0 for j in range(n)] for l in range(n)]
i, j = 0, 0
for k in range(1, n * n + 1):
        a[i][j] = k
        print('k', k)
        if i <= j + 1 and i + j < n - 1:
            j += 1
            print('j', j)
        elif i < j and i + j >= n - 1:
            i += 1
            print('i', i)
        elif i >= j and i + j > n - 1:
            j -= 1
            print('j', j)
        elif i > j + 1 and i + j <= n - 1:
            i -= 1
            print('i=', i, 'j=', j)
for i in a: print(*i)

# Матрица поворота - поворот вектора заполнения матрицы на 90 градусов: dx,dy=(-dy,dx)




'''Решения других пользователей'''


'''n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])'''

'''n, x, l, t = int(input()), 1, 0, 0
r, d, a = n-1, n-1, [[0 for j in range(n)] for i in range(n)]
while x <= n**2:
    for j in range(l, r+1, 1): a[t][j], x = x, x + 1
    for i in range(t+1, d+1, 1): a[i][r], x = x, x + 1
    for j in range(r-1, l-1, -1): a[d][j], x = x , x + 1
    for i in range(d-1, t, -1): a[i][l], x = x, x +1
    l, t, r, d = l+1, t+1, r-1, d-1
for y in a: print(*y)'''


'''n = int(input())
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
'''


'''n = int(input())
x, y, dx, dy, m = 0, 0, 0, 1, [[0] * n for i in range(n)]
for i in range(n * n):
    m[x][y] = str(i + 1)
    if x + dx >= n or x + dx < 0 or y + dy >= n or y + dy < 0 or m[x + dx][y + dy]:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
print("\n".join([" ".join(i) for i in m]))
'''



'''n = int(input())
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
'''



''''mas=int(input())
#создание квадратного массива из "mas" элементов, заполненного нулями
arr=[[0 for j in range(mas)] for i in range(mas)]
#инициализация переменных для смещения (rem), счетчик (k)
rem,i,k=0,0,1
#наполненеие массива по спирали
for m in range (mas,0,-1):
    for j in range (rem,m):
        arr[i][j]=k;k+=1
    for i in range (rem+1,m):
        arr[i][j]=k;k+=1
    for j in range (m-2,rem-1,-1):
        arr[i][j]=k;k+=1
    for i in range (m-2,rem,-1):
        arr[i][j]=k;k+=1
    rem+=1
#вывод на экран
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
'''



'''n = int(input())
array, increment, k, x, y = [[0]*n for j in range(n)], (0, 1, 0, -1), 1, 0, -1
for i in range(1, 2*n):
    for j in range(1,(2*n-i+3)//2):
        x += increment[(i-1)%4]
        y += increment[i%4]
        array[x][y] = k
        k += 1
for i in range(n): print(*array[i])
'''

