'''Простейшая система проверки орфографии основана на использовании списка известных слов. 
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, 
оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей 
в списке известных слов, после передаётся d строк с одним словарным словом на строку, 
затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. 
Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся 
в словаре, не должны повторяться в выводе программы.
'''

n = int(input())
dic, words = set(), set()
for i in range(n):
    dic.add(input().lower())
l = int(input())
for i in range(l):
    list = input().lower().split(" ")
    for w in list:
        if w not in dic and w not in words:
            print(w)
            words.add(w)


'''Решения других пользователей'''

'''know = {input().lower() for i in range(int(input()))}
new_text = []
for j in range(int(input())):
    new_text+=(input().lower().split())
for g in set(new_text) - know:
        print(g,end='\n')'''

'''S = set(input().lower() for i in range(int(input())))
print("\n".join(set(sum([input().lower().split() for i in range(int(input()))], [])) - S))'''

'''d, s = {input().lower() for _ in range(int(input()))}, set((" ".join([input().lower() for _ in range(int(input()))])).split())
[print(x) for x in s - d]'''

'''dictionary = set(input().lower() for _ in range(int(input())))
strings_words = set(" ".join([input().lower() for _ in range(int(input()))]).split())
print("\n".join(strings_words - dictionary))'''

'''st, ln = set(input().lower() for i in range(int(input()))), set()
for i in range(int(input())): ln |= set(input().lower().split())
print('\n'.join((ln - st)))'''

'''print('\n'.join(set(map(str, filter(lambda x, y = {input().lower() for i in range(int(input()))}: x not in y, [i for j in [input().lower().split() for l in range(int(input()))] for i in j])))))'''

'''# множество словарных слов
known_words = set([input().lower() for i in range(int(input()))])
# текст для проверки преобразован в множество слов
text2check = set([ word for string in [input().lower().split() for i in range(int(input()))] for word in string])
# вывод только "несловарных" слов
[print(word) for word in text2check if word not in known_words]'''

'''dic = set(input().lower() for i in range(int(input())))
words = [w.lower() for l in [input().split() for i in range(int(input()))] for w in l]
print(*set(words).difference(dic), sep="\n")'''

'''d = {input().lower() for _ in range(int(input()))}
print(*{w for _ in range(int(input())) for w in input().strip().split() if w.lower() not in d}, sep="\n")'''

