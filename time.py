'''
Сложность: 5 из 10
Напишите программу time.py, которая получает из первого аргумента командной строки количество секунд, которое прошло с начала дня. Программа должна выводить отформатированное время в формате HH:MM:SS.

SS – число секунд от 0 до 59.
MM – число минут от 0 до 59.
HH – число часов от 0 до 23.
Все значения времени должны выводится в двузначном формате, если число занимает один знак, то перед ним должен быть 0.

Если прошло меньше одного часа, то часы выводить не нужно.

Если прошло меньше одной минуты, то минуты выводить не нужно.

Пример использования:
> python time.py 17
17
> python time.py 79
01:19
> python time.py 4589
01:16:29
'''

import sys
seq_total = int(sys.argv[1])


seq = seq_total % 60

min = seq_total // 60
#if min >= 60:
while min >= 60:
    min = min - 60

hr = seq_total // (60 * 60)


if seq <= 9:
    seq = str('0' + str(seq))

if min == 60:
    min = 0
if min <= 9:
    min = str('0' + str(min))


if hr <= 9:
    hr = str('0' + str(hr))


if hr == '00' and min == '00':
    print(str(seq))
elif hr == '00' and min != '00':
    print(str(min)+':'+str(seq))
else:
    print(str(hr)+':'+str(min)+':'+str(seq))
