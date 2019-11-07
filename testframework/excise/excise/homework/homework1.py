# 1.利用pip,安装第三方模块requests，描述你用什么方法来确认安装是成功的。
# 安装pip install requests
# 确认安装是成功的（1）import requests（2）pip list (3)pip3 list |grep requests

# 2.把2.918转换为整形
# import math
#
# print(int(2.918))  # 2
# print(round(2.918))  # 3
# print(math.floor(2.918))  # 2
# print(math.ceil(2.918))  # 3
# print("%.0f" % (2.918))  # 3
# print("{0:.0f}".format(2.928))  # 3
#
#
# print(int(2.418))  # 2
# print(round(2.418))  # 2
# print(math.floor(2.418))  # 2
# print(math.ceil(2.418))  # 3
# print("%.0f" % (2.418))  # 2
# print("{0:.0f}".format(2.428))  # 2

print("%.*f" % (0,1.23))
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
# 格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
#
# %s    字符串 (采用str()的显示)
#
# %r    字符串 (采用repr()的显示)
#
# %c    单个字符
#
# %b    二进制整数
#
# %d    十进制整数
#
# %i    十进制整数
#
# %o    八进制整数
#
# %x    十六进制整数
#
# %e    指数 (基底写为e)  保留小数点后面六位有效数字，指数形式输出
#
# %E    指数 (基底写为E)
#
# %f    浮点数 保留小数点后面六位有效数字
#
# %F    浮点数，与上相同
#
# %g    指数(e)或浮点数 (根据显示长度) 在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
#
# %G    指数(E)或浮点数 (根据显示长度)
#
#
#
# %%    字符"%"
# 可以用如下的方式，对格式进行进一步的控制：
#
# %[(name)][flags][width].[precision]typecode
#
# (name)为命名
#
# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
#
# width表示显示宽度
#
# precision表示小数点后精度
# 上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：
#
# print("%.*f" % (4, 1.2))
# Python实际上用4来替换*。所以实际的模板为"%.4f"。
import math


def p_print(a):
    print(int(a))
    print(round(a))
    print(math.floor(a))
    print(math.ceil(a))
    print("%.0f" % (a))
    print("{0:.0f}".format(a))


# p_print(2.918)
# p_print(2.428)
# 3.把10进制数18转化为2进制数
a = 18
b = bin(a)
print(b)  # 0b10010
# 4.用java替换字符串：“Python is popular”里面的Python，并用java替换成JAVA
str = "Python is popular"
str_re = str.replace('Python', ('java').upper())
print(str_re)
# 5.把列表[1,2,3,4,5,6,7,8]里面的2,4,6,8打印出来
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for item in list1:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)
print('奇数：', even)
print('偶数：', odd)
# # 6.创建一个字典，字典的key分别是name,sex,province,修改原始province的值为新值“江苏”
dic = {'name': 'duheng', 'sex': 'female', 'province': '河南'}
dic['province'] = '江苏'
print(dic)
