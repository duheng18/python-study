# 2.堆 heapq（queue队列）模块包含一些堆操作函数的模块，包括6个函数，4个直接和堆操作有关。
# heapq模块中重要的函数
# heappush(heap,x)将x入堆
# heappop(heap)将堆中最小的元素弹出
# heapify(heap)将heap属性强制应用到任意一个列表
# heapreplace(heap,x)将堆中最小的元素弹出，同时将x入堆。
# nlargest(n,iter)返回iter中第n大的元素
# nsmallest(n,iter)返回iter中第n小的元素
# coding:utf-8
from heapq import *
from random import shuffle

data = []
for i in range(10):
    data.append(i)
# shuffle() 方法将序列的所有元素随机排序
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
    # print(heap)
print(heap)
# [0, 1, 3, 2, 6, 7, 5, 9, 4, 8]
heappush(heap, 0.5)
print(heap)
# [0, 0.5, 3, 2, 1, 7, 5, 9, 4, 8, 6]
# 元素排序规则：位于i位置上的元素总比i//2位置处的元素大（反过来说就是i位置处的元素总比2*i以及2*i+1位置处的元素小。）
# 这是底层堆算法的基础，而这个特性称为堆属性。
# heappop弹出最小的元素，一般来说都是索引0处的元素，并且会确保剩余元素中最小的那个占据这个位置。即保持刚才提到的堆属性。
heappop(heap)
print(heap)
# [0.5, 2, 1, 5, 7, 4, 3, 9, 6, 8]

# heapify函数使用任意列表作为参数，并且通过尽可能少的移位操作，将其转换为合法的堆。(堆属性)
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print(heap)
# [0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

# heapreplace弹出堆的最小元素，并且将新元素推入。这样做比调用heappop之后再调用heappush更高效。
heapreplace(heap, 0.5)
print(heap)
# [0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
heapreplace(heap, 10)
print(heap)
# [1, 2, 5, 3, 6, 7, 9, 8, 4, 10]

# nlargest(n,iter)和nsmallest(n,iter)分别用来寻找任何可迭代对象iter中第n大或第n小的元素。
