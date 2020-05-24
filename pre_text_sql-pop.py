# preparing text from the assignment task for inserting to SQL easier

a = '''AppointmentID PatientID DoctorID AppointmentDate BloodPressure  Weight TreatmentNotes 
A1	P1	D2	07/01/2019	80	65	Dream to success
A2	P13	D4	01/04/2019	77	88	Good heart rate
A3	P11	D9	03/22/2019	82	95	Many spots
A4	P7	D4	02/01/2020	85	74	Fast heart rate
A5	P9	D5	04/13/2019	75	56	Reports checked
A6	P3	D6	11/12/2019	81	96	Sun light spots
A7	P10	D7	01/29/2020	80	87	Early treatment
A8	P9	D5	08/12/2019	86	92	Much better
A9	P14	D4	05/18/2019	75	75	Good heart rate
A10	P8	D3	11/18/2019	76	79	New teeth
A11	P11	D9	06/22/2019	78	71	Much better
A12	P2	D7	02/21/2020	82	86	Early treatment
A13	P4	D2	08/17/2019	81	101	Bad dreams
A14	P6	D6	06/27/2019	79	49	Sun light spots
A15	P10	D7	07/29/2020	80	83	Early treatment
A16	P7	D4	08/01/2020	78	79	Good heart rate'''

def data_convert(d):
    conv_d = list(d.split('/'))
    conv_d = str(conv_d[2]) + '-' + str(conv_d[0]) + '-' + str(conv_d[1])
    return conv_d

print(', '.join(a.split('\n')[0].split()))
for i in a.split('\n')[1:]:
    i = list(i.split('\t'))
    for j in i:
        if '/' in j:
            i[i.index(j)] = data_convert(j)
    print(tuple(i), end = '')
    print(',')

'''
Output:

AppointmentID, PatientID, DoctorID, AppointmentDate, BloodPressure, Weight, TreatmentNotes
('A1', 'P1', 'D2', '2019-07-01', '80', '65', 'Dream to success'),
('A2', 'P13', 'D4', '2019-01-04', '77', '88', 'Good heart rate'),
('A3', 'P11', 'D9', '2019-03-22', '82', '95', 'Many spots'),
('A4', 'P7', 'D4', '2020-02-01', '85', '74', 'Fast heart rate'),
('A5', 'P9', 'D5', '2019-04-13', '75', '56', 'Reports checked'),
('A6', 'P3', 'D6', '2019-11-12', '81', '96', 'Sun light spots'),
('A7', 'P10', 'D7', '2020-01-29', '80', '87', 'Early treatment'),
('A8', 'P9', 'D5', '2019-08-12', '86', '92', 'Much better'),
('A9', 'P14', 'D4', '2019-05-18', '75', '75', 'Good heart rate'),
('A10', 'P8', 'D3', '2019-11-18', '76', '79', 'New teeth'),
('A11', 'P11', 'D9', '2019-06-22', '78', '71', 'Much better'),
('A12', 'P2', 'D7', '2020-02-21', '82', '86', 'Early treatment'),
('A13', 'P4', 'D2', '2019-08-17', '81', '101', 'Bad dreams'),
('A14', 'P6', 'D6', '2019-06-27', '79', '49', 'Sun light spots'),
('A15', 'P10', 'D7', '2020-07-29', '80', '83', 'Early treatment'),
('A16', 'P7', 'D4', '2020-08-01', '78', '79', 'Good heart rate'),
'''

