"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B,
т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
"""

import requests
import re

result = False

a = input()
b = input()
a_res = requests.get(a)

for link in re.findall(r"<a href=\"(.*)\"", a_res.text):
    res = requests.get(link)
    for url in re.findall(r"<a href=\"(.*)\"", res.text):
        if b == url:
            result = True
            break

if result:
    print('Yes')
else:
    print('No')
