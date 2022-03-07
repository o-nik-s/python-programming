'''В какой-то момент в Институте биоинформатики биологи перестали понимать, 
что говорят информатики: они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали 
при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения 
на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
Программа принимает на вход две строки одинаковой длины, на первой строке записаны 
символы исходного алфавита, на второй строке — символы конечного алфавита, 
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё 
одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, 
b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. 
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac'''


alpha, beta = input(), input()
strAlpha, strBeta = input(), input()
# a,b = input().splitlines() - получит две переменные, первая и вторая строка (в данном случае)
# Модератор курса

for s in strAlpha:
    print(beta[alpha.find(s)], end="")
print()
for s in strBeta:
    print(alpha[beta.find(s)], end="")


'''Решения других'''

'''srce, fin, decodeStr, encodeStr = input(), input(), input(), input()
for c in decodeStr:
    print(fin[srce.index(c)], end = '')
print()
for c in encodeStr: 
    print(srce[fin.index(c)], end = '')
print()  '''

'''din, dout, forcrypt, fordecrypt = (input() for _ in range(4))
print ("".join([dout[din.index(x)] for x in forcrypt]), "".join([din[dout.index(x)] for x in fordecrypt]), sep="\n")'''

'''k1 = input()
k2 = input()
s1 = input()
s2 = input()

def crypt(str, key1, key2):
    k = {}
    for i in range(len(key1)):
        k[key1[i]] = key2[i]
    res = ''
    for c in str:
        res += k[c]
    return res

print(crypt(s1, k1, k2))
print(crypt(s2, k2, k1))'''

'''source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))'''

'''a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))'''