'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, 
удаляет из него все нечётные значения, а чётные нацело делит на два. Функция 
не должна ничего возвращать, требуется только изменение переданного списка.'''

def modify_list(l):
    for i in lst:
        # l(i) = int(l(i))
        a = 0
    else:
        l.remove(i)


lst = [20, 10, 10, 3]
print(modify_list(lst))  # None
print(lst)

test = ['0','0','1','1']
res = ['1' if x == '0' else '0' if x == '1' else x for x in test]
print(res)
