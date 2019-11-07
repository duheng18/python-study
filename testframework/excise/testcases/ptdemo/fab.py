'''
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题，许多初学者都可以轻易写出如下函数：
 1. 简单输出斐波那契數列前 N 个数
'''

# no1

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#
#
# print(fab(4))
'''
要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。
以下是 fab 函数改写后的第二个版本：
 2. 输出斐波那契數列前 N 个数第二版
'''

# no2
# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return L
# print(fab(5))

'''
利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class，以下是第三个版本的 Fab：
'''

# no3
# class Fab(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# for n in Fab(5):
#     print(n)

'''
使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。
如果我们想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，
yield 就派上用场了：
'''


# no4
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print(b)
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)

# from inspect import isgeneratorfunction
#
# print(isgeneratorfunction(fab))  # True

# import types
#
# print(isinstance(fab, types.GeneratorType))  # False
# print(isinstance(fab(5), types.GeneratorType))  # True

from collections import Iterable

print(isinstance(fab, Iterable))  # False
print(isinstance(fab(5), Iterable))  # True

f1 = fab(3)
f2 = fab(5)
print('f1:', f1.__next__())
print('f2:', f2.__next__())
print('f1:', f1.__next__())
print('f2:', f2.__next__())
print('f1:', f1.__next__())
print('f2:', f2.__next__())
print('f2:', f2.__next__())
print('f2:', f2.__next__())


def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


file = read_file('/Users/duheng/Documents/project/excise/testcases/ptdemo/fab.py')
for f in file:
    print(f)
