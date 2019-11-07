print(dir(tuple))
['__add__', '__class__', '__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__',
 '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmul__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', 'count', 'index']

my_str = "I love Python"
my_list = ["python", "java", "language", "age"]
my_list2 = [24, 12, 2.3, 9.7]
my_tupe = ("python", 33, "java", 8.8)
my_dict = {"name": "linda", "age": 88}
my_list1 = ['a', 'a', 1, 1, 2, 3]
my_set = {1, 2, 3}

a = 10
print(type(a))

a1 = str(a)  # 强制转换从int到str
print(type(a1))
print(type(int(a1)))  # str转int

print(tuple(my_list))  # list与tuple元组转换
print(list(my_tupe))

print(set(my_list1))  # 列表转换set编程不重复的
print(set(my_dict))  # 字典转换成set只有Key值
print(set(my_dict.keys()))
print(set(my_dict.values()))

print(list(my_dict.values()))  # 字典转成列表，key,value可以单转
print(list(my_dict.keys()))
print(list(my_dict))

my_tupe1 = ('one', 1), ('two', 2), ('three', 3)
my_list_tuple = [('one', 1), ('two', 2), ('three', 3)]
print(my_tupe1)
print(type(my_list_tuple))
print(dict(my_list_tuple))
print(dict(my_tupe1))

# 将对象x转换为字符串
b = {"name": "linda", "age": 18}
str_b = repr(b)  # 转成字符串
print(str_b)
print(type(str_b))
print(str_b[0:3])

# 用来计算在字符串中的有效Python表达式，并返回一个对象
a = "[1,2,3]"
list_a = eval(a)
print(list_a[0])

# 常见的各种转换
# int(x[,base])  将x转换为一个整数
# str(x)    将对象x转换为字符串
# tuple(s)  将序列s转换为一个元组
# list(s)   将序列s转换为一个列表
# set(s)    转换为可变集合
# dic(d)    创建一个字典。d必须是一个序列（key,value）元组
# repr(x)   将对象x转换为表达式字符串
b = {"name": "linda", "age": 18}
# eval(str) 用来计算在字符串中的有效Python表达式，并返回一个对象
a = "[1,2,3]"
print(eval(a))

# Python算术运算符
# 运算符               描述              例子
#   +       2个数相加或者字符串相加    10+1 "Love"+"Python"
#   -       2个数相减               10-1输出9
#   *       2个数相乘或者复制若干个字符 2*4，"ab"*3
#   /       2个数相除               10/4,10/4.0
#   %       取模，返回除法的余数      10%7，10%7.0
#   **      幂-返回x的y次幂          2**10
#   //      取整除-返回商的整数部分    10//7,10//7.0

# Python比较运算符
#  运算符              描述                  例子
#   ==      等于-比较对象是否相等         10==11 "a"=="a"
#   !=      不等于-比较两个对象是否不相等   10!=11 "a"!="a"
#   >       大于-返回x是否大于y           10>11  "b">"a"
#   <       小于-返回x是否小于y。所有比较   (a<b)返回true。
#           运算符返回1表示真，返回0表示假。
#           这分别与特殊的变量True和False
#           等价。注意，这些变量名的大写。
#   >=      大于等于-返回x是否大于等于y     (a>=b)返回False

# Python赋值运算符
#   运算符             描述                  例子
#   =           简单的赋值运算符    a=10+11 b="Love"+""+"python"
#   +=          加法赋值运算符     c+=a等效于c=c+a
#   -=          减法赋值运算符     c-=a等效于c=c-a
#   *=          乘法赋值运算符     c*=a等效于c=c*a
#   /=          除法赋值运算符     c/=a等效于c=c/a

# Python逻辑运算符
#   运算符             描述                  例子
#   and             与运算                 x and y
#   or              或运算                 x  or y
#   not             布尔“非”               not x

# Python成员运算符
# 运算符               描述                  例子
#   in      指定序列里面是否包含指定元素  "python" in [1,2,"python",4,]
#   not in  指定序列里面没有包含指定元素  "java" not in [1,2,"python",4,]