# 1.整数
a = 10
print(type(a))
# 2.python3没有long类型
# 3.浮点型
b = 3.1415
print(type(b))
# 4.字符串
str = "you are right"
print(type(str))
# 5.列表
list = ["python", 12, 2.3, 9.7]
print(type(list))
# 6.元组
tup = ("python", 12, 2.3, 9.7)
print(type(tup))
# 7.字典
dic = {"name": "xiaozhang", "company": "baidu", "grade": "T7"}
print(type(dic))
# 8.集合
set1 = {1, 2.3, 3}
print(type(set1))
# 9.布尔型 bool True False
#
var = "a"
print(ord(var))
# 不同数据类型的转换
# 字符串转换为整形
var2 = "15"
var3 = int(var2)
print(var3)
print(var2)
print(type(var2))
# 整形转换浮点型
var4 = float(var3)
print(var4)
print(type(var4))
# 列表转元组(mysql-列表形  sel-元组)
list1 = ["a", "l", "c"]
print(type(list1))
var5 = tuple(list1)
print(var5)
print(type(list1))
print(list1)
print(type(var5))
# 嵌套元组转化为字典
a = (("name", "zhangsan"), ("sex", "male"))
var6 = dict(a)
print(var6)
# 小数处理
print(int(8.9567))
print(round(8.9567))
# 列表元组不相等
list2 = [1, 2, 3]
tuple3 = (1, 2, 3)
list3 = [1, 2, 3]
print(list2 == list3)
print(list2 == tuple3)
# python定义变量不需要定义变量类型
# 不同进制转换
# 10->8
print(oct(int(18)))
# 10->2
print(bin(int(8)))
