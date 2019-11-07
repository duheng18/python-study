# 3、对字典的访问与操作

# 1.查：通过key来访问对象value->dict.get("key")
# 2.增：插入key=
# 3.改：更新已有key的value=
# 4.删：删除一个key-->del
# 5.如果键在字典dict里返回true，否则返回false
# 6.字典中键值遍历方法：遍历的（键，值），值，键

# 把key循环出来
# for key in D:
#     print(key,'=>,D[key]')

# 只循环value
# for value in D.values():
#     print(value)

# 把key和vaule都循环出来
# for key,value in D.items():
#     print(key,":",value)
#     assert D[key]==value
print(dir(dict))
# ['__class__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'clear', 'copy',
# 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']
ages = {
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
print(ages.get("linda", 88))
ages["dalu"] = 33
ages["yujian"] = 55
print(ages)
del ages['leimeng']
print(ages)
# key in dict
D = {'username': 'linda', 'age': 12, "salary": 1000000}
print("循环出来key，再通过key可能输入值")
for key in D:
    print(key, '=>', D[key])

print("只循环出值")
for value in D.values():
    print(value)

print("同时循环出key与value,断言返回key的值与...通常用在接口测试中json的响应断言")
for key, value in D.items():
    print(key, ":", value)
    assert D[key] == value
