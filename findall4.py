"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\\', line):
        print('\n' + line, end='')
