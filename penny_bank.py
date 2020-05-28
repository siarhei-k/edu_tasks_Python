'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать,
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
'''

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.m = 0

    def can_add(self, v):
        if self.capacity - v >= 0:
            return True
        else:
            return False


    def add(self, v):
        if self.can_add(v) == True:
            self.capacity -= v
            return self.capacity

# test
x = MoneyBox(10)
x.add(5)
x.add(5)
print(x.can_add(1))


