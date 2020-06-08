"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall('cat', line)) >= 2:
        print('\n' + line, end='')
