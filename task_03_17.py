'''Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть 
от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, 
но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого 
по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.'''

height = list()
classHeight = [[0 for j in range(2)] for i in range(0, 11)]
# with open('task_03_17_input.txt', "r") as inpt:  # encoding="UTF-8"
with open('dataset_3380_5.txt', "r") as inpt:
    for line in inpt:  # line будет принимать значения строки
        lineList = line.strip().split("\t")  # strip() убирает все служебные символы при члении строки
        height.append(lineList)
        print(int(lineList[0]))
        classHeight[int(lineList[0])-1][0] += int(lineList[2])
        classHeight[int(lineList[0])-1][1] += 1
        print(classHeight)
for i in range(11):
    if classHeight[i][1] == 0:
        print(i+1, "-")
    else:
        print(i+1, classHeight[i][0]/classHeight[i][1])


'''Решения других'''

'''d = {i:[] for i in range(1, 12)}
with open('dataset_3380_5.txt') as f: [d[int(line.split()[0])].append(int(line.split()[2])) for line in f]
[print(i, sum(d[i])/len(d[i]) if d[i] != [] else ' ') for i in range(1, 12)]'''