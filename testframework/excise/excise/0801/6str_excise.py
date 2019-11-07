# 数据处理
# 1.对字符串变量的访问与操作
# Python中的字符串用单引号‘或双引号’括起来，同时使用反斜杠\转义特殊字符。
# str="abcdef"
# Python字符串运算符
# 实例变量a值为字符串"Hello",b变量值为"Python"
# +     字符串连接   a+b输出结果：HelloPython
# *     重复输出字符串     a*2输出结果：HelloHello
# []    通过索引获取字符串中字符    a[1]输出结果
# [:]   截取字符串中的一部分，遵循左闭右开原则，str[0,2]是不包含第3个字符的。a[1:4]输出结果
# r/R   原始字符串-原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符
# print(r'\n')
# %     格式字符串

# 关于字符串的操作
str = 'python 蟒蛇'
print(dir(str))  # str中有哪些方法
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
  '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
  'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
   'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
   'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
    'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
     'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
      'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
      'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
      'translate', 'upper', 'zfill']
'''
print(str.count("l"))
print(str.find("o"))
print(str.capitalize())
print(str.encode("gb2312"))
print(str.find('n'))
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符（-1代表最后一个，左闭右开）
print(str[0])  # 输出字符串中第一个字符串
print(str[2:5])  # 输出从第三个开始到第四个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + 'TEST')  # 连接字符串
print(len(str))
print(str.startswith("python"))
b = "20"
print(b.isdecimal())
print(str.upper())
print(str.title())
str0 = 'python 蟒蛇'
print(str0.replace(str0[0:6], 'java'.upper()))
print(str * 4)


s1 = "-"
s2 = ""
seq = ("l", "i", "n", "d", "a")  # 字符串序列
print(s1.join(seq))
print(s2.join(seq))


str4 = "编号 标题 测试数据 测试结果"
(no, title, test_data, test_result) = str4.split(" ")
print(test_data)

# 格式输出
print('Hi,%s,you have $%d.'%('linda',1000000000))
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125)) #保留小数点后1位
print("{} {}".format("hello","world")) #不设置指定位置，按默认顺序