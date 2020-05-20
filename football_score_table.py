'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''

tab = {}

total_games = 0
won = 1
equal = 2
lose = 3
score = 4

n = int(input())

for i in range(n):
    res = input()
    res = res.split(';')

    first_team = res[0]
    second_team = res[2]

    first_team_goals = int(res[1])
    second_team_goals = int(res[3])

    #count total games number
    if first_team not in tab:
        tab[first_team] = [1, 0, 0, 0, 0]
    else:
        tab[first_team][total_games] += 1
    if second_team not in tab:
        tab[second_team] = [1, 0, 0, 0, 0]
    else:
        tab[second_team][total_games] += 1

    #count won-lose-equal games + scores
    if first_team_goals > second_team_goals and first_team_goals != second_team_goals:
        tab[first_team][won] += 1
        tab[first_team][score] += 3 # scores
        tab[second_team][lose] += 1
    elif first_team_goals < second_team_goals and first_team_goals != second_team_goals:
        tab[second_team][won] += 1
        tab[second_team][score] += 3 # scores
        tab[first_team][lose] += 1
    else:
        tab[first_team][equal] += 1
        tab[second_team][equal] += 1
        tab[first_team][score] += 1 # scores
        tab[second_team][score] += 1 # scores

for i in tab:
    print(i, end = ':')
    print(*tab[i])
