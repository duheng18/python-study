# 1.多态（Polymorphism）：意味着可以对不同类的对象使用相同的操作
# 多态可以让用户对于不知道是什么类（对象类型）的对象进行方法调用。
from random import choice

x = choice(['Hello,world!', [1, 2, 'e', 'e', 4]])
print(x)
print(x.count('e'))
print(len(x))


def length_message(x):
    print("The length of", repr(x), 'is', len(x))


length_message('Fornd')
length_message([1, 2, 3])
