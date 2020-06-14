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
