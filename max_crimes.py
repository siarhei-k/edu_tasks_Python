'''
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''

import csv

with open('Crimes.csv') as cr:
    crimes = list(csv.reader(cr))

crime_types = {}
for row in crimes[1:]:
    crime_type = row[5]
    crime_year = row[2]
    if '2015' in crime_year:
        if crime_type not in crime_types:
            crime_types[crime_type] = 1
        else:
            crime_types[crime_type] += 1

most_crimes = max([[value, key] for key, value in crime_types.items()])
print(most_crimes)
