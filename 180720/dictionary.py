# 字典类型的定义： 理解"映射" 映射是一种键（索引）和值（数据）的对应  如：属性:值
# 序列类型由0...N整数作为数据的默认索引   映射类型由用户定义索引
# 字典类型是"映射"的体现 字典是键值对的集合，键值对之间无序
# 采用{}和dic()创建，键值对用冒号:表示
# 字典类型的用法 在字典变量中，通过键获得值
d = {'中国': '北京','美国': '华盛顿','法国': '巴黎'}
print(d['中国'])

# type(x)返回变量x的类型
de = {}
print(type(de))

a = set()
print(type(a))

# 字典类型操作函数和方法
# del d[k] 删除字典d中键k对应的数据值
# k in d 判断键k是否在字典d中，如果在返回True,否则返回Flase
# d.keys()返回字典d中所有的键信息
# d.values()返回字典d中所有的值信息
# d.items()返回字典d中所有的键值信息
print('中国' in d)
print(d.keys())
print(d.values())
print(d.items())
# d.get(k,<default>)键k存在，则返回相应值，不在则返回<default>值  重要&&&&
# d.pop(k,<default>)键k存在，则取出相应值，不在则返回<default>值
# d.popitem()随机从字典d中取出一个键值对，以元组形式返回type(de)
# d.clear()删除所有的键值对
# len(d)返回字典d中元素的个数
print(d.get('中国','伊斯兰堡'))
print(d.get('巴基斯坦','伊斯兰堡'))
print(d)
print(d.popitem())

