#create empty dict
my_dict = {}

# make list with items from original file
items = open('items.txt', 'r').readline().split(', ')

# make a dict from list with items from original file
for item in items:
    key = item.split(': ')[0]
    value = item.split(': ')[1]
    my_dict[key] = value

#check our dict
print('Dict was created from file:')
print(my_dict)

#function for dict inverse
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            inverse[val].append(key)
    return inverse

#check function for dict inverse
print('Inverted dict')
print(invert_dict(my_dict))

#make string from inverted list
inv_list = []
for key, val in invert_dict(my_dict).items():
    inv_list.append('{}: {}'.format(key, val))
inv_list = ', '.join(inv_list)

# check inverted list string
print('List for writing to file:')
print(inv_list)

#create new file
new_file = open('invert_items.txt', 'w')

# write inverted list to a new file
new_file.write(inv_list)