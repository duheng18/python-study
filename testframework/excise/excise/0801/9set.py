print(dir(set))
['__and__', '__class__', '__contains__',
 '__delattr__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__',
 '__iand__', '__init__', '__init_subclass__',
 '__ior__', '__isub__', '__iter__', '__ixor__',
 '__le__', '__len__', '__lt__', '__ne__',
 '__new__', '__or__', '__rand__', '__reduce__',
 '__reduce_ex__', '__repr__', '__ror__',
 '__rsub__', '__rxor__', '__setattr__',
 '__sizeof__', '__str__', '__sub__',
 '__subclasshook__', '__xor__', 'add',
 'clear', 'copy', 'difference',
 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset',
 'issuperset', 'pop', 'remove',
 'symmetric_difference',
 'symmetric_difference_update', 'union', 'update']

set1={1,2,3}
set2=set1
set3=set("hello")
print(set3)
print(set1,set3)
print(set1)
# set3.clear()
de=set3.pop()
print(de)
set3.remove("l")
a=set1 & set3
print(a)
a=set1 | set3
print(set1)
print(set3)
print(a)
# 4、对集合的访问与操作
# 增：创建集合和新增一个元素add
# 改：update可以添加多个元素到集合，参数为iterable.
# 删：
#   1.pop随机删除集合中一个元素，可以通过变量来获取删除的元素
#   2.remove(self,*args,**kwargs)删除集合中指定的元素，如果该集合内没有该元素就报错
#   3.discard(self,*args,**kwargs)删除集合中指定的元素，如果该集合内没有该元素也不会报错
# intersection &: 交集；
# union |: 并集合；
# difference-: 差集
