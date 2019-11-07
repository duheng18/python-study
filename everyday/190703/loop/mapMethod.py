#!/usr/bin/env python
# coding=utf-8

def sqr(x):
    return x ** 2


a = (4, 5, 8)
# print(tuple(map(sqr, a)))
# print(list(map(sqr,a)))
# print(set(map(sqr,a)))
# print([sqr(a[0]),sqr(a[1]),sqr(a[2])])

mylist=[]
for a_item in a:
    mylist.append(sqr(a_item))
print(mylist)


# def f(x):
#     return x * x


# print(set(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(list(map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(tuple(map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])))
