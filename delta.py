'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4
'''

import datetime

date = list(map(int, input().split()))
days = int(input())

date = datetime.date(date[0], date[1], date[2])
delta = datetime.timedelta(days=days)
new_date = date + delta

print(new_date.strftime('%Y %#m %#d'))  # for Unix systems ('%Y %-m %-d')
