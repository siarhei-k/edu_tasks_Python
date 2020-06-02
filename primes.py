"""
Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""

import itertools
import math


def primes():
    a = 1
    while True:
        a += 1
        '''
        Теорема Вильсона (Натуральное число p > 1,  является простым тогда и только тогда, когда (p-1)! + 1 делится на p)
        '''
        if (math.factorial(a - 1) + 1) % a == 0:
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))  # x - до какого числа ищем простые
