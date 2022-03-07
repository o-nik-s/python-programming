# Формула Герона для вычисления площади треугольников

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
print(S)
