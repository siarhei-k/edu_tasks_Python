'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический
факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''

import requests

answ = open('/home/sk/Downloads/answ.txt', 'a')
with open('/home/sk/Downloads/dataset_24476_3 (9).txt', 'r') as file:
    for line in file.readlines():
        n = line.replace('\n', '')
        res = requests.get(f'http://numbersapi.com/{n}/math?json=true')
        data = res.json()
        print(data)
        if data['found'] == False:
            answ.write('Boring\n')
            print('Boring')
        else:
            answ.write('Interesting\n')
            print('Interesting')
answ.close()

