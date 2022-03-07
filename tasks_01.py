# task_01_01 - Коля каждый день ложится спать ровно в полночь и недавно узнал, что
# оптимальное время для его сна составляет XX минут. Коля хочет поставить
# себе будильник так, чтобы он прозвенел ровно через XX минут после полуночи,
# однако для этого необходимо указать время сигнала в формате часы, минуты.
# Помогите Коле определить, на какое время завести будильник.
#
# Часы и минуты в выводе программы должны располагаться на разных строка

X = int(input())
print(X // 60)
print(X % 60)


# task_01_02 - Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится
# спать после полуночи в H часов и M минут. Помогите Кате определить,
# на какое время ей поставить будильник, чтобы он прозвенел ровно через
# XX минут после того, как она ляжет спать.
#
# На стандартный ввод, каждое в своей строке, подаются значения X, H и M.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник:
# в первой строке часы, во второй — минуты.

X = int(input())
H = int(input())
M = int(input())

print(H + (M + X) // 60)
print((M + X) % 60)


# task_01_03 - Выполните код в интерпретаторе Python 3 и вставьте в поле ответа результат вычисления.
# Постарайтесь разобраться, почему интерпретатор выдал именно такой ответ. Помните,
# что любые арифметические операции выше по приоритету операций сравнения и логических операторов.

x = 5
y = 10
y > x * x or y >= 2 * x and x < y

print(y > x * x or y >= 2 * x and x < y)


# task_01_o4 - Найдите результат выражения для заданных значений aa и bb. Учитывайте регистр символов при ответе.

a = True
b = False
a and b or not a and not b

print(a and b or not a and not b)


# task_01_05 - Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов
# в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас
# Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям
# передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее A часов,
# выведите “Недосып”, если же более B часов, то выведите “Пересып”.
#
# Получаемое число A всегда меньше либо равно B.
#
# На вход программе в три строки подаются переменные в следующем порядке:
# A, B, H.

A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Это нормально")
elif H <= A:
    print("Недосып")
elif B <= H:
    print("Пересып")


# task_01_06 - Требуется определить, является ли данный год високосным.
#
# Напомним, что високосными годами считаются те годы, порядковый номер которых
# либо кратен 4, но при этом не кратен 100, либо кратен 400 (например, 2000-й
# год являлся високосным, а 2100-й будет невисокосным годом).
#
# Программа должна корректно работать на числах 1900≤n≤3000.
#
# Выведите "Високосный" в случае, если считанный год является високосным и
# "Обычный" в обратном случае (не забывайте проверять регистр выводимых
# программой символов).


n = int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Високосный")
else:
    print("Обычный")


# task_01_07 - Формула Герона для вычисления площади треугольников

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
print(S)


# task_01_08 - Напишите программу, принимающую на вход целое число, которая выводит True,
# если переданное значение попадает в интервал
# (−15,12]∪(14,17)∪[19,+∞) и False в противном случае.

x = int(input())
if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
    print(True)
else:
    print(False)

x = int(input())
print(-15 < x <= 12 or 14 < x < 17 or 19 <= x)


# task_01_09 - Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

x1 = float(input())
x2 = float(input())
op = input()

if op == 'mod':
    if x2 == 0:
        print('Деление на 0!')
    else:
        print(x1 % x2)
elif op == 'pov':
    print(x1 ** x2)
elif op == 'div':
    if x2 == 0:
        print('Деление на 0!')
    else:
        print(x1 // x2)
elif op == "+":
    print(x1 + x2)
elif op == "-":
    print(x1 - x2)
elif op == "/":
    if x2 == 0:
        print('Деление на 0!')
    else:
        print(x1 / x2)
elif op == "*":
    print(x1 * x2)


# task_01_10 - Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты
# бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять
# жилплощадь, требуется написать программу, на вход которой подаётся тип
# фигуры комнаты и соответствующие параметры, которая бы выводила площадь
# получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.

t = input()
if t == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
elif t == "прямоугольник":
    a = float(input())
    b = float(input())
    S = a * b
elif t == "круг":
    pi = 3.14
    r = float(input())
    S = pi * r**2
print(S)


# task_01_11 - В институте биоинформатики по офису передвигается робот. Недавно студенты
# из группы программистов написали для него программу, по которой робот,
# когда заходит в комнату, считает количество программистов в ней
# и произносит его вслух: "n программистов".
#
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать
# верное окончание слова.
#
# Напишите программу, считывающую с пользовательского ввода целое число nn
# (неотрицательное), выводящее это число в консоль вместе с правильным образом
# изменённым словом "программист", для того, чтобы робот мог нормально
# общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
#
# В комнате может быть очень много программистов. Проверьте, что ваша
# программа правильно обработает все случаи, как минимум до 1000 человек.

n = int(input())
print(n, end="")
while k <= 1000:
    n = k % 100
    if n % 10 == 0 or 5 <= n <= 20 or 5 <= n % 10 <= 9:
        print(" программистов")
    elif n % 10 == 1:
        print(" программист")
    elif 2 <= n % 10 <= 4:
        print(" программиста")
    k += 1


# task_01_12 - В институте биоинформатики по офису передвигается робот. Недавно студенты
# из группы программистов написали для него программу, по которой робот,
# когда заходит в комнату, считает количество программистов в ней
# и произносит его вслух: "n программистов".
#
# Для того, чтобы это звучало правильно, для каждого nn нужно использовать
# верное окончание слова.
#
# Напишите программу, считывающую с пользовательского ввода целое число nn
# (неотрицательное), выводящее это число в консоль вместе с правильным образом
# изменённым словом "программист", для того, чтобы робот мог нормально
# общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
#
# В комнате может быть очень много программистов. Проверьте, что ваша
# программа правильно обработает все случаи, как минимум до 1000 человек.

n = int(input())
print(n, end="")
while k <= 1000:
    n = k % 100
    if n % 10 == 0 or 5 <= n <= 20 or 5 <= n % 10 <= 9:
        print(" программистов")
    elif n % 10 == 1:
        print(" программист")
    elif 2 <= n % 10 <= 4:
        print(" программиста")
    k += 1


# task_01_13 - Паша очень любит кататься на общественном транспорте, а получая билет,
# сразу проверяет, счастливый ли ему попался. Билет считается счастливым,
# если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать
# программу, которая проверит равенство сумм и выведет "Счастливый", если
# суммы совпадают, и "Обычный", если суммы различны.
#
# На вход программе подаётся строка из шести цифр.
#
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.


n = int(input())

n1 = n // 10**5
n2 = n // 10**4 - n1 * 10
n3 = n // 10**3 - (n1 * 100 + n2 * 10)
n4 = n // 10**2 - (n1 * 1000 + n2 * 100 + n3 * 10)
n5 = n // 10 - (n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10)
n6 = n % 10
if (n1 + n2 + n3) == (n4 + n5 + n6):
    print("Счастливый")
else:
    print("Обычный")
