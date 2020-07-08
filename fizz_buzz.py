"""
Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел)
в диапазоне от begin до end включительно. При этом:

Если число делится без остатка на 3, то вместо него выводится слово Fizz
Если число делится без остатка на 5, то вместо него выводится слово Buzz
Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
В остальных случаях в строку добавляется само число
Функция принимает два параметра (begin и end), определяющих начало и конец диапазона (включительно).
Если диапазон пуст (в случае, когда begin > end), то функция возвращает пустую строку.
"""

import unittest


def fizz_buzz(begin, end):
    l = ''
    if begin > end:
        return ''
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            l += ' FizzBuzz'
        elif i % 3 == 0:
            l += ' Fizz'
        elif i % 5 == 0:
            l += ' Buzz'
        else:
            l += (' ' + str(i))
    return l.strip()


class TestFizzBuzz(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(fizz_buzz(1, 0), '')
        self.assertEqual(fizz_buzz(7, 7), '7')
        self.assertEqual(fizz_buzz(11, 20), '11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz')
