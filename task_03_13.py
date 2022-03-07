'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
'''


def procOfResults(team, result):
    if team == result[0]:
        return result[1] > result[3], result[1] == result[3], result[1] < result[3]
    elif team == result[2]:
        return result[3] > result[1], result[3] == result[1], result[3] < result[1]
    return 0, 0, 0


n = int(input())
results = []
teamsList = set()
totalResult = dict()
for i in range(n):
    results.append(input().strip().split(";"))
    teamsList.add(results[i][0])
    teamsList.add(results[i][2])
    print(results)
for team in teamsList:
    print("--------------")
    print(team)
    totalResult[team] = [0, 0, 0]  # Побед, ничьих, поражений
    for i in range(n):
        print(results[i])
        print(procOfResults(team, results[i]))
        for j in range(3):
             totalResult[team][j] += procOfResults(team, results[i])[j]
        print("totalResult:", totalResult)
print("---------------")
print(results)
print(teamsList)
print(totalResult)
print("---------------")
for key, value in totalResult.items():
    print(key, ":", value[0] + value[1] + value[2], " ", value[0], " ", value[1], " ", value[2], " ", 3 * value[0] + value[1], sep="")



'''Решения других пользователей'''

'''# put your python code here
def createScoreBase(d, team):
    if team not in d:
        d[team] = {'w': 0, 'n': 0, 'f': 0}


n = int(input())
dict = {}
for i in range(n):
    team1, score1, team2, score2 = input().split(";")
    createScoreBase(dict, team1)
    createScoreBase(dict, team2)
    if score1 > score2:
        dict[team1]['w'] += 1
        dict[team2]['f'] += 1
    elif score2 > score1:
        dict[team1]['f'] += 1
        dict[team2]['w'] += 1
    else:
        dict[team1]['n'] += 1
        dict[team2]['n'] += 1

for t in dict:
    print(t + ":", dict[t]['w'] + dict[t]['f'] + dict[t]['n'], dict[t]['w'], dict[t]['n'], dict[t]['f'],
          3 * dict[t]['w'] + dict[t]['n'])'''