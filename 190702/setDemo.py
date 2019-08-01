a = {}
print(type(a))
b = set()
print(type(b))
myset = {1, 2, 3}
set1 = {4, 5, 6, 10}
set2 = {4, 5, 6, 3}
# 集合里面的元素是不可重复的
# 合并多个set
# print(myset.union(set1))
# 获取2个set的交集
# print(set1.intersection(set2))
# 获取2个set的差集
# print(set2.difference(set1))
# 获取2个set的对称差集
# print(set2.symmetric_difference(set1))

set2.discard()
print(set2)
set2.remove(3)
print(set2)
