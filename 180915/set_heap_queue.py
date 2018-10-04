# 1.集合
set(range(10))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set([0, 1, 2, 3, 0, 1, 2, 3, 4, 5])
# {0, 1, 2, 3, 4, 5}
set(['fee', 'fie', 'foe'])
# {'foe', 'fee', 'fie'}
# 找出两个集合的并集
a = set([1, 2, 3])
b = set([2, 3, 4])
a.union(b)
# {1, 2, 3, 4}
a | b
# {1, 2, 3, 4}
c = a & b
c.issubset(a)
# True
c <= a
# True
c.issuperset(a)
# False
c >= a
# False
a.intersection(b)
# {2, 3}
a & b
# {2, 3}
a.difference(b)
# {1}
a - b
# {1}
a.symmetric_difference(b)
# {1, 4}
a ^ b
# {1, 4}
a.copy()
# {1, 2, 3}
a.copy() is a
# False

# 一个函数用于查找并且打印两个集合的并集，可以使用来自set类型的union方法的未绑定版本

from functools import reduce

mySets = []
for i in range(10):
    # 将set(range(i,i+5))集合放入到mySets列表中。
    mySets.append(set(range(i, i + 5)))
# 返回mySets中所有集合的并集
print(reduce(set.union, mySets))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# 集合是可变的，所以不能用做字典中的键。集合本身只能包含不可变（可散列的）值，所以也就不能包含其他集合。
# frozenset类型，用于代表不可变（可散列）的集合。frozenset构造函数创建给定集合的副本，不管是将集合
# 作为其他集合成员还是字典的键，frozenset都很有用。
a = set()
b = set()

# 2.堆 heapq（queue队列）模块包含一些堆操作函数的模块，包括6个函数，4个直接和堆操作有关。
# heapq模块中重要的函数
# heappush(heap,x)将x入堆
# heappop(heap)将堆中最小的元素弹出
# heapify(heap)将heap属性强制应用到任意一个列表
# heapreplace(heap,x)将堆中最小的元素弹出，同时将x入堆。
# nlargest(n,iter)返回iter中第n大的元素
# nsmallest(n,iter)返回iter中第n小的元素
from heapq import *
import random

data = range(10)
random.shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print(heap)
print(heappush(heap, 0.5))
print(heap)
