'''Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой: 
f(x)=1−(x+2)**2 при x≤−2,
f(x)=-x/2 при −2<x≤2,
f(x)=(x−2)**2+1 при 2<x.
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.'''

def f(x):
    if x <= -2:
        return 1 - (x + 2)**2
    elif -2 < x <= 2:
        return -x / 2
    elif 2 < x:
        return (x - 2)**2 + 1