my_tuple = ("python", 12, 2.3, 9.7)
# 元组元素建立后不可修改；元组访问速度快；元组可以作为字典的key
# print(type(my_tuple))
# print(help('tuple'))
# 串联多个元组
tuple2 = (4, 6)
print(my_tuple + tuple2)
print(id(my_tuple))
print(id(tuple2))
print(id(my_tuple + tuple2))
# 快速复制多个元组
