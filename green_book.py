""""
В единственной строке содержится два целых числа 𝑛 и 𝑘 (1 ≤ 𝑛 ≤ 105;
1 ≤ 𝑘 ≤ 109) разделенные пробелом.

Выведите единственное число: количество раз, которое число 𝑘 встречается в таблице
умножения размером 𝑛 × 𝑛.
"""

n = input().split()

# get values from input
size = int(n[0])
num = int(n[1])
count = 0

# check how long vector should be cheked
if size < num:
    lmt = size
else:
    lmt = num

for i in range(1, lmt + 1):
    # print(str(i) + ' ')
    if size * i < num:  # check if number can be in a vector
        continue
    elif num % i != 0:  # check if number can be divided by iterator
        continue
    else:
        for j in range(i, size * i + 1, i):
            # print(str(j) + ' ', end='')
            if j == num:
                count += 1
                break  # when number was founded
        # print()

print(count)
