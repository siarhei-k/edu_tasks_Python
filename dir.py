'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''

import os.path
import zipfile
import urllib.request

os.chdir('C:/Users/Siarhei K/Downloads')

# скачиваем файл
file = urllib.request.urlopen("https://stepik.org/media/attachments/lesson/24465/main.zip").read()
d = open('main.zip', 'wb')
d.write(file)

# распаковываем файл
z = zipfile.ZipFile('main.zip', 'r')
z.extractall()

# создаем файл для ответа
l = []
t = open('list_files.txt', 'w')

# ищем ответа в директории-задании
for cur_dir, dir, f in os.walk('.'):
    for el in f:
        if el[-3:] == '.py':
            l.append(cur_dir[2:].replace('\\', '/'))

# записываем ответ
for el in sorted(list(set(l))):
    t.write(el + '\n')

t.close()


