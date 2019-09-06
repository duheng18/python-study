import re

patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@xxx.com').group())
print(re.match(patt, 'nobody@www.xxx.com').group())

patte = '\w+@(\w+\.)*\w+\.com'
print(re.match(patte, 'nobody@www.xxx.yyy.zzz.com').group())

print(re.match('\w\w\w-\d\d\d', 'abc-123').group())  # 字母字符串-数字
print(re.match('\w\w\w-\d\d\d', '123-123').group())  # 数字字符串-数字
print(re.match('\w\w\w-\d\d\d', '2sa-123').group())  # 字母数字字符串-数字
# print(re.match('\w\w\w-\d\d\d','sdd-ass').group())

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())  # abc-123
print(m.group(1))  # abc
print(m.group(2))  # 123
print(m.groups())  # ('abc', '123')

n = re.match('ab', 'ab')
print(n.group())  # ab
print(n.groups())  # ()

o = re.match('(ab)', 'ab')
print(o.group())  # ab
print(o.group(1))  # ab
print(o.groups())  # ('ab',)

p = re.match('(a)(b)', 'ab')
print(p.group())  # ab
print(p.group(1))  # a
print(p.group(2))  # b
print(p.groups())  # ('a', 'b')

q = re.match('(a(b))', 'ab')
print(q.group())  # ab
print(q.group(1))  # ab
print(q.group(2))  # b
print(q.groups())  # ('ab', 'b')

a=re.search('^The','The end.')
if a is not None:
    print('a'+a.group())

b=re.search('^The','end.The')
if b is not None:
    print('b'+b.group())

c=re.search(r'\bthe','bite the dog')
if c is not None:
    print('c'+c.group())

d=re.search(r'\bthe','bitethe dog')
if d is not None:
    print('d'+d.group())

e=re.search(r'\Bthe','bitethe dog')
if a is not None:
    print('e'+e.group())
