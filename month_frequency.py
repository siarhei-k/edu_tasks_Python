import datetime as dt

from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)[1:]

date_format = '%m/%d/%y %H:%M'

for row in potus:
    appt_start_date = row[2]
    row[2] = dt.datetime.strptime(appt_start_date, date_format)

visitors_per_month = {}

for row in potus:
    dt_object = row[2]
    dt_string = dt_object.strftime('%B, %Y')
    if dt_string not in visitors_per_month:
        visitors_per_month[dt_string] = 1
    else:
        visitors_per_month[dt_string] += 1

print(visitors_per_month)
