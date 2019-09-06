import re

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, patt314)
if m is not None:
    print(m.group())

m = re.match(patt314, '3014')  # .匹配0
if m is not None:
    print(m.group())

m = re.match(patt314, '3.14')  # .匹配.
if m is not None:
    print(m.group())
