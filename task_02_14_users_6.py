mas=int(input())
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

