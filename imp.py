"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Е
сли операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций,
после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000.
"""

s = input()
a = input()
b = input()
counter = 0

while True:
    if s != s.replace(a, b) or a in s:
        s = s.replace(a, b)
        counter += 1
    else:
        print(counter)
        break
    if counter >= 1000:
        print('Impossible')
        break
