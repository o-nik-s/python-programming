'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.'''


import requests

# inpt = open('task_03_12_input.txt', 'r')
inpt = open('dataset_3378_3.txt', 'r')
url = inpt.readline().strip()
inpt.close()

path = "https://stepic.org/media/attachments/course67/3.6.3/"
print(url)
txt = requests.get(url).text
while txt[:2] != "We":
    url = path + txt.strip()
    print(url)
    txt = requests.get(url).text
print(txt)


'''# with open('dataset_3378_3.txt') as inf:
    my_link = inf.readline().strip()
r = requests.get(my_link)
while r.text.split()[0] != "We":
    r = requests.get("/".join(my_link.split("/")[:-1] + [r.text]))
print(r.text)'''

'''import requests
name = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
while name.text[:2] != "We":
    ﻿name = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + name.text)
print (name.text)﻿'''

'''a = '699991.txt'
while a[:2] != 'We':
  b = 'https://stepic.org/media/attachments/course67/3.6.3/' + a
  a = requests.get(b).text
  print(a)﻿'''