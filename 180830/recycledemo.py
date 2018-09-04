# 跳出循环
# 1.结束循环可以使用break语句
from math import sqrt

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
# 2.continue 当前循环结束跳到下一轮循环到开始
# 跳过剩余的循环体，但是不结束循环
# for x in seq:
#     if condition1:continue
#     if condition2:continue
#     if condition3:continue
#
#     do_something()
#     do_something_else()
#     do_another_thing()
#     etc()

# for x in seq:
#     if not(condition1 or condition2 or condition3):
#         do_something()
#         do_something_else()
#         do_another_thing()

# 3.while True/break习语
# word = 'dummby'
# while word:
#     word = input('Please enter a word:')
#     print('The word was ' + word)

# word=input('Please enter a word:')
# while word:
#     print('The word was '+word)
#     word=print('Please enter a word:')

# 第一部分负责初始化；
# 第二部分负责循环条件为真的情况下使用第1部分内初始化好的数据。

# while True:
#     word=input('Please enter a word:')
#     if not word:
#         break
#     print('The word was '+word)

# 循环中的else子句
from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")

# 轻量级循环
print([x * x for x in range(10)])
print([x * x for x in range(10) if x % 3 == 0])
print([[x, y] for x in range(3) for y in range(3)])

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + '+' + g for b in boys for g in girls if b[0] == g[0]])  # b[0] c/b/a
print([b + '+' + g for b in boys for g in girls])

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    # 以女孩每一项首字母作为键，以女孩的名字作为值，构成一个字典
    # 如果键girl[0]不存在于字典中，将会添加键并将值设为默认值[]。.append(girl)给键增加对应值
    letterGirls.setdefault(girl[0], []).append(girl)
    print(girl[0])
    print(letterGirls)
    # 循环boys，找出那些和当前男孩名字首字母相同的女孩集合。
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])

# pass
# del
# 使用exec和eval执行和求值字符串
