# -*- coding:utf-8 -*-

# 1.多变量一起赋值
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, "linda"
print(a, b, c)

# 2.交换数据
# x, y = y, x

# 3.将二个列表分别组合在一起
# for a, b in zip(a, b):
#     print(a, b)

# 4.输入多个相同的值需要乘法
str = "python"
print(str * 4)

# 5.简洁写法：10以内偶数
x = [12, 3, 4, 5, 13, 19, 20]
li = [x for x in range(10) if x % 2 == 0]
print(li)

# 6.反转list列表
print(list(reversed(li)))

# 7.列表排序
print(list(sorted(li)))

# 8.列表中每个元素出现几次
from collections import Counter

my_counter = Counter(li)
print(my_counter.most_common())

# 快速添加数据的小技巧：
ls = [1, 2, 3, 4]
list1 = [i for i in ls if i > 2]
print(list1)
tuple1 = (2, 4, 6)
dict1 = {x: x ** 2 for x in tuple1}
print(dict1)
tuple2 =(2, 4, 6)
dict2 = {x: 'item' + str(x ** 2) for x in tuple2}
print(dict2)
set1 = {z for z in 'hello world' if z not in 'low level'}
print(set1)
