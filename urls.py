"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть,
это последовательность символов, которая следует сразу после символов протокола, если он есть,
до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
"""

import requests
import re

#link = input()
link = 'http://pastebin.com/raw/7543p0ns' # link for testing
url = requests.get(link)
urls = re.findall(r'href\s?=\s?[\'\"][fhtp:\/s]{0,7}\/?([^.][^\"|\'|\/|:]*)', url.text)

for url in sorted(list(set(urls))):
    print(url)