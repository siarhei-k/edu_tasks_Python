'''
Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

﻿Пример использования:
mod_3 = mod_checker(3)
print(mod_3(3)) # True
print(mod_3(4)) # False
'''

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

# mod_checker = lambda x, mod=0: lambda y: y % x == mod
