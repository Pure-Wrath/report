#!  python3
#   20250212 - v1.0
#   Soma - Paste the pages of sales of the day and get the data in a sorted list.

import re

text = """
PASTE_HERE
"""

stock = r'LOJA VIRTUAL\s+([\d\.,]+)\s+(?:CARLOS MORI JUNIOR|JOSE CAPELA)'

results = re.findall(stock, text)

for value in results:
    print(value)
