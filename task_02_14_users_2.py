n, x, l, t = int(input()), 1, 0, 0
r, d, a = n-1, n-1, [[0 for j in range(n)] for i in range(n)]
while x <= n**2:
    for j in range(l, r+1, 1): a[t][j], x = x, x + 1
    for i in range(t+1, d+1, 1): a[i][r], x = x, x + 1
    for j in range(r-1, l-1, -1): a[d][j], x = x , x + 1
    for i in range(d-1, t, -1): a[i][l], x = x, x +1
    l, t, r, d = l+1, t+1, r-1, d-1
for y in a: print(*y)
