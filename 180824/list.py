# 列表：Python的"苦力"
# 列表是可变的---可以改变列表的内容
# list类型
# 字符串不能像列表一样被修改，so有时根据字符串创建列表会很有用。
# 字符串转化成列表
print(list('Hello'))
# 列表转换成字符串
m = list('Hello')
n = ''.join(m)
print(n)
# 基本的列表操作
# 列表可以使用所有适用于序列的标准操作：索引、分片、连接和乘法。列表可以修改。
# 改变列表的方法：元素赋值、元素删除、分片赋值、列表方法
# 1.改变列表：元素赋值
# 注：不能为一个位置不存在的元素进行赋值
x = [1, 1, 1]
x[1] = 2
print(x)
# 2删除元素
# 元素彻底消失，列表长度也发生了改变。
# del除了删除列表中的元素，还能用于删除其他元素，字典元素、变量的删除操作。
names = ['Alice', 'Beth', 'Ceil', 'Dee-Dee', 'Earl']
del names[1]
print(names)
# 3.分片赋值
name = list('Perl')
print(name)
# 一次为多个元素赋值
name[2:] = list('ar')
print(name)
# 使用与原序列不等长的序列将分片替换
name = list('Perl')
print(name)
name[1:] = list('ython')
print(name)
# 分片赋值语句可以在不需要替换任何原有元素的情况下插入新的元素.即替换了一个空的分片。
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)
# 通过分片来删除元素。==del numbers[1:4]
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []
print(numbers)
