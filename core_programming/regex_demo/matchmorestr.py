import re

bt='bat|bet|bit'
m=re.match(bt,'bat')
if m is not None: print('-1-'+m.group())

m=re.match(bt,'blt')
if m is not None: print('-2-'+m.group())

m=re.match(bt,'He bit me!')
if m is not None:print('-3-'+m.group())


m=re.search(bt,'He bit me!')
if m is not None:print('-4-'+m.group())