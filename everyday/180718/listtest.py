# 定义一个空列表lt
lt = list()
print(lt)
# 向lt新增5个元素
ls = [11, 12, 13, 14, 15]
lt += ls
print(lt)
# 修改lt中第2个元素
lt[1] = 22
print(lt[1])
# 向lt中第2个位置增加一个元素
lt.insert(1, 33)
print(lt[1])
# 从lt中第1个位置删除一个元素
del lt[0]
print(lt[0])
print(lt)
# 删除lt中第1-3位置元素
del lt[:3]
print(lt)
# 判断lt中是否包含数字0
print(0 in lt)
# 向lt新增数字0
lt.append(0)
print(lt)
print(0 in lt)
# 返回数字0所在lt中的索引
print(lt.index(0))
# lt的长度
print(len(lt))
# lt中最大元素
print(max(lt))
# 清空lt
print(lt.clear())


# 序列是基类类型，扩展类型包括：字符串、元组和列表
# 元组用()和tuple()创建，列表用[]和list()创建
# 元组操作与序列操作基本相同
# 列表操作在序列操作基础上，增加了更多的灵活性
# 序列类型、列表类型是重点
