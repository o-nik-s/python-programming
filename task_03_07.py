'''Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, 
на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть 
больше одной строки) и выводит самое частое слово в этом тексте и через 
пробел то, сколько раз оно встретилось. Если таких слов несколько, 
вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.'''


def update_dictionary(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


def findMaxWord(dic):
    max, maxKey = 0, ""
    for key in dic.keys():
        if dic[key] > max:
            max = dic[key]
            maxKey = key
    return maxKey, max


dict = {}
with open('dataset_3363_3.txt', "r") as inpt:
# with open('task_03_07_input.txt', "r") as inpt:
    for line in inpt:  # line будет принимать значения строки
        lineList = line.strip().split()
        for word in lineList:
            update_dictionary(dict, word.lower())
maxWord, maxCount = findMaxWord(dict)
str = maxWord + " " + str(maxCount)
print(str)
with open('task_03_07_output.txt', "w") as oupt:
    oupt.write(str)


'''Решения пользователей'''

'''all = open('dataset.txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z >= y:
        y = z
        m = i
print(m, y)'''

'''#with open('test.txt','r') as f: s=f.read().lower().split()
g=set(s)
m = max([s.count(x) for x in g])
v = sorted([i for i in g if s.count(i) == m ])[0]
print(v,m)'''

'''D = {}
with open('input.txt', 'r') as f:
    for line in f:
        for w in line.lower().split():
            D[w] = D.get(w, 0) + 1
w = max(sorted(D), key=lambda w: D[w])
print(w, D[w])'''

'''#with open('dataset_xxx.txt') as file:
     dct = {}
     for line in file:
         lst = [i.lower() for i in line.strip().split()]
         for i in lst:
             dct.update({i: int(dct.get(i, 0)) + 1})

     m = max(dct, key=(lambda key: dct[key]))
     print(m, dct[m])'''

'''import re
from collections import Counter
word=re.findall(r'\w+',open('dataset_3363_3.txt').read().lower())
b=Counter(word).most_common(3) 
print(b)'''

'''col = dict()
with open('dataset_3363_3.txt','r') as f:
    for s in f:
      for w in s.lower().split():
          if w in col: col[w] += 1
          else: col[w] = 1

for i in sorted(col.items()):
    if i[1] == max(col.values()): print(*i)'''

