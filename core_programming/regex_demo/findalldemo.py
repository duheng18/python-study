import re

# print(re.findall('car', 'car'))
print(re.findall('car', 'scary'))
print(re.findall('car', 'carry the barcardi to the car'))

s = 'This and that.'
# [('This', 'that')]
# print(re.findall(r'(th\w+) and (th\w+)', s, re.I))
# # ('This', 'that')
# print(re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().groups())
# # This
# print(re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().group(1))
# # that
# print(re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().group(2))
# # [('This', 'that')]
# print([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)])
# # ['This', 'that']
# print(re.findall(r'(th\w+)', s, re.I))
it = re.finditer(r'(th\w+)', s, re.I)
g = it.__next__()
# This
print(g.group())
# ('This',)
print(g.groups())
# This
print(g.group(1))
#
g = it.__next__()
# that
print(g.group())
# ('that',)
print(g.groups())
# that
print(g.group(1))
# ['This', 'that']
print([g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)])
