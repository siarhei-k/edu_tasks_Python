'''
В первой строке содержится целое число 𝑛 (0 ≤ 𝑛 ≤ 106).
Во второй строке через пробел записаны девять
целых чисел 𝑎1, 𝑎2, … , 𝑎9 (1 ≤ 𝑎𝑖 ≤ 105) – стоимости в золоте каждой цифры (от 1 до 9 соответственно).
Выведите максимальное число, на которое игроку хватит золота. Стоимость числа равна сумме стоимостей
каждой входящей в него цифры. Если игроку не хватит золота ни на одно число, то выведите −1.
'''

# Решение задачи не прошло все автотесты!
z = int(input())
cost = input().split(' ')

price = {'0': 0}
for i in range(1, 10):
    price[str(i)] = int(cost[i-1])

for edge in range(10**5, 0, -1):
    #print('cheked number is ' + str(edge))
    if '0' in list(str(edge)):
        #print('has zero')
        continue
    total = 0
    for el in list(str(edge)):
        total += price[el]
    #print('wage is ' + str(total))
    if total <= z:
        print(edge)
        break
    if edge == 1:
        print(-1)