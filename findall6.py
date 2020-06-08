"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова,
состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
Sample Output:
There’ll be no more "argh"
argh AaAaAaA
"""

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'\b([Aa]+)\b', 'argh', line, 1)
    print(line)
