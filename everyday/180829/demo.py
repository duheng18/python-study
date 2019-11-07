# x=1
# while x<=100:
#     print(x)
#     x+=1

# name=''
# while not name:
#     name=input('Please enter your name:')
# print('Hello,%s!'%name)
#
# names=''
# while not names.strip():
#     names=input('Please enter your name:')
# print('Hello,%s!'%names)

# nam = ''
# while not nam or nam.isspace():
#     nam = input('Please enter your name:')
# print('Hello,%s!' % nam)

# 循环遍历字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, "corresponds to", d[key])

for key, value in d.items():
    print(key, "corresponds to", value)
# 一些迭代工具
# 1.并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# for i in range(len(names)):
#     print(names[i], 'is', ages[i], 'years old')
ziped = zip(names, ages)
print(list(ziped))
a, b = zip(*zip(names, ages))
print(a)
print(b)

# 2.按索引迭代
strings = 'djo xx1w ddfe'
for string in strings:
    if 'xx' in string:
        index = strings.index(string)
        strings[index] = '[censored]'
print(strings)

index = 0
for string in strings:
    if 'xx' in string:
        strings[index] = '[censored]'
    index += 1
print(strings)

for index, string in enumerate(strings):
    if 'xx' in string:
        strings[index] = '[censord]'
print(strings)
# 3.翻转和排序迭代
# reversed和sorted

print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello,world!'))
print(list(reversed('Hello,world!')))
print(''.join(reversed('Hello,world!')))
