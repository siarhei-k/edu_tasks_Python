"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"
3
"""

s = input()
t = input()


def occurrences(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i:].startswith(b):
            counter += 1
    return counter


def test():
    try:
        assert occurrences('abababa', 'aba') == 3, 'should be 3'
        assert occurrences('abababa', 'abc') == 0, 'should be 0'
        assert occurrences('abc', 'abc') == 1, 'should be 1'
        assert occurrences('aaaaa', 'a') == 5, 'should be 5'
        print('Tests passed')
    except AssertionError as er:
        print("With\n", s, '\n', t, '\n', er)


print(occurrences(s, t))
test()
