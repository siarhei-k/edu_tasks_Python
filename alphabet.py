alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

# convert to histogram
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# checking for duplicates
def has_duplicates(s):
    s = histogram(s) # calling for histogramm
    for i in s:
        if int(s[i]) > 1:
            return True
    return False

# loop for test_dups
print('Checking for duplicates:')
for i in test_dups:
    if has_duplicates(i): # calling for duplicates function
        print(i + ' has duplicates')
    else:
        print(i + ' has no duplicates')

# check for missing letters
def missing_letters(s):
    s = histogram(s) # calling for histogramm
    mis_let = list(alphabet)
    for i in s:
        if int(s[i]) >= 1:
            if i in mis_let:
                mis_let.remove(i)
    return ''.join(mis_let)

# loop for test_miss
print('')
print('Checking for missing :')
for i in test_miss:
    if missing_letters(i) == '': # calling missing letters to check for using of all letters
        print(i, 'uses all the letters')
    else:
        print(i, 'is missing letters', missing_letters(i)) # calling missing letters



