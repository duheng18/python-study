# 字典
# 字典的使用
items = [('name', 'Gumby'), ('age', '42')]
d = dict(items)
print(d)
d = dict(name='Gumby', age='42')
print(d)
d = dict()
print(d)
# 基本操作
# len(d)返回d中项（键-值对）的数量；
# d[k]返回关联到键k上；
# d[k]=v将值v关联到键k上；
# del d[k]删除键为k的项；
# k in d 检查d中是否有键为k的项。
# 键类型：键可以是任意的不可变类型：浮点型、字符串、元组
# 自动添加：即使键在字典中不存在，也可以为它赋值，这样算建立新的项。
# 成员资格：k in d 查找的是键而不是值。
x = {}
x[42] = 'Foobar'
print(x)
# 字典格式化字符串
# 在每个转换说明符中的%字符后面，可以加上键（用圆括号括起来），后面再跟上其他说明元素。
# 4.2.4字典方法
# 1.clear  clear方法清除字典中所有的项。
x = {}
y = x
x['key'] = 'value'
print(y)
print(x)
x = {}
print(y)
print(x)

x = {}
y = x
x['key'] = 'value'
print(y)
x.clear()
print(x)
print(y)

# copy
# copy方法返回一个具有相同键-值对新字典（这种方法实现对是浅复制，因为指本身就是相同对，而不是副本。）
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print(y)
# 替换值时原始字典不受影响
y['username'] = 'mlh'
# 如果修改了某个值，原始的字典也会修改
y['machines'].remove('bar')
print(y)
print(x)
# 深复制，复制其包含的所有值
# deepcopy
from copy import deepcopy

d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(c)
d['names'].append('Clive')
print(c)
print(dc)
print(d)
# 3.framkeys 使用给定的键建立新的字典，每个键都对应一个默认的值None。
print({}.fromkeys(['name', 'age']))
# {'name': None, 'age': None}
print(dict.fromkeys(['name', 'age']))
# {'name': None, 'age': None}
print(dict.fromkeys(['name', 'age'], '(unknown'))
# {'name': '(unknown', 'age': '(unknown'}

#4.get 更宽松的访问字典项的方法，试图访问字典中不存在的项时不会出错。
print(d.get('name'))
print(d.get('name','N/A'))
#5.has_key 可以检查字典中是否又特定的键d.has_key k in d
#6.items字典中都每一项都以列表形式返回  iteritems会返回一个迭代器对象而不是列表
#7.keys和iterkeys keys方法将字典中都键以列表形式返回，而iterkeys则返回对键对迭代器。
#8.pop 获得对应于给定键对值，然后将这个键-值对从字典中移除。
#9.popitem 弹出随机项
#10.setdefault 能够获得与给定键相关联对键值，不含有给定键对情况下设定相应对键值。
#11.update 可以利用一个字典项更新另外一个字典：


