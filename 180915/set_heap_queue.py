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
#union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
# 语法
# union() 方法语法：
# set.union(set1, set2...)
# 参数
# set1 -- 必需，合并的目标集合
# set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
# 返回值
# 返回一个新集合。
print(reduce(set.union, mySets))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数
# function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# reduce() 函数语法：
# reduce(function, iterable[, initializer])
# 参数
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
# 返回值
# 返回函数计算结果。

# 集合是可变的，所以不能用做字典中的键。集合本身只能包含不可变（可散列的）值，所以也就不能包含其他集合。
# frozenset类型，用于代表不可变（可散列）的集合。frozenset构造函数创建给定集合的副本，不管是将集合
# 作为其他集合成员还是字典的键，frozenset都很有用。
# a = set()
# b = set()


