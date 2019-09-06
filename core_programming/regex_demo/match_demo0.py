import re

m = re.match('foo', 'foo')
if m is not None:
    print(m.group())

n = re.match('foo', 'bar')
if n is not None:
    print(n.group())

o = re.match('foo', 'foo on the table')
print(o.group())

print(re.match('foo', 'foo on the table').group())


p=re.match('foo','seafood')
if p is not None:
    print('----'+p.group())