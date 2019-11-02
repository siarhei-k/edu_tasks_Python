import math

def my_sqrt(a):
    x = a
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return x

def test_sqrt():
    a = 1
    while a <= 25:
        print('a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {}'.format(a, round(my_sqrt(a), 11), round(math.sqrt(a), 11), (math.fabs((my_sqrt(a) - math.sqrt(a))))))
        a += 1

print(test_sqrt())