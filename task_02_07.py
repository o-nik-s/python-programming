# Узнав, что ДНК не является случайной строкой, только что поступившие
# в Институт биоинформатики студенты группы информатиков предложили
# использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
# символов исходной строки заменяются на этот символ и количество его
# повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным
# алгоритмом и выводит закодированную последовательность на стандартный вывод.
# Кодирование должно учитывать регистр символов.

s = input()
if s > "":
    snew = ""
    count = 0
    t = s[0]
    for c in s:
        if c == t:
            count += 1
        else:
            snew += t + str(count)
            t = c
            count = 1
    snew += t + str(count)
    print(snew)
else:
    print("")
