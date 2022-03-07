''' На прошлой неделе мы сжимали строки, используя кодирование повторов. 
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, 
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" 
у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, 
чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, 
используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, 
надо отправить в качестве ответа на эту задачу. '''


def reconstr_dictionary(line):  # reconstruction
    dict, key, value = {}, "", 0
    for symb in line:
        if symb.isalpha():
            if symb != '' and key != '':
                if key not in dict:
                    dict[key] = value
                elif key in dict:
                    dict[key] = dict[key] + value
            key = symb
            value = 0
        elif symb.isdigit():
            if value == 0:
                value = int(symb)
            else:
                value = 10**value + int(symb)
    if key not in dict:
        dict[key] = value
    elif key in dict:
        dict[key] = dict[key] + value
    return dict


def reconstr_string(line):  # reconstruction
    str, s, d = "", "", 0
    for symb in line:
        if symb.isalpha():
            if d != 0:
                str += s * d
            s = symb
            d = 0
        elif symb.isdigit():
            if d > 0:
                d = 10**d + int(symb)
            else:
                d = int(symb)
    str += s * d
    return str


dict = {}
with open('dataset_3363_2.txt', "r") as inpt:
# with open('task_03_06_input.txt', "r") as inpt:
    line = inpt.readline().strip()
print(line)
str = reconstr_string(line)
print(str)
with open('task_03_06_output.txt', "w") as oupt:
    oupt.write(str)


'''Решения пользователей'''

'''Один из ответов пользователей
import re
print(''.join(i[0] * int(i[1:]) for i in re.findall('[a-zA-Z]?\d+', str(input()))))'''

'''Другой ответ
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j'''

'''a = list(input())
c = str()
char = ''
for i in range(len(a)):
    if a[i] < 'a' and a[i] < 'A':
        c += a[i]
    else:
        if c != '':
            print(char*int(c),end='')
            c = ''
        char = a[i]
print(char*int(c))'''

'''import re
with open('dataset_3363_2.txt') as file:
    t = file.readline()
for i in re.compile(r"(\w)(\d+)").finditer(t):
    print (i.group(1) * int(i.group(2)), end="")'''

'''import re
fin=open('zzz.txt')
fou=open('yyy.txt','w')
for s in re.findall('\D\d+',fin.readline().strip()):
    fou.write(s[0]*int(s[1:]))'''

'''import re
with open('input.txt', 'r') as file:
    string = file.readline().strip
r = re.findall('(\w)(\d+)', string)
for c, n in r:
    print(c * int(n), end='')'''