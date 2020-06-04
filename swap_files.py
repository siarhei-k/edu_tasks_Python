
with open('dataset_24465_4.txt') as org, open('swap.txt', 'w') as sw:
    original = org.read().splitlines()
    for line in original[::-1]:
        sw.write(line +'\n')
