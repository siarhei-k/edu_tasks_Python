'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, 
после чего на dd строках указываются эти слова. Затем передаётся количество 
ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. 
Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''

d = input()
s = []
for i in range(int(d)):
    a = input()
    s.append(a).lower()

l = input()
t = []
for i in range(int(l)):
    b = input()
    t.append(b.lower())

m = []
for i in t:
    f = i.split()
    for j in f:
        if j not in s:
            m.append(j)


for i in(set(m)):
    print(i)



