# 3.1基本字符串操作
# 索引、分片、乘法、判断成员资格、求长度、取最小值和最大值
# 字符串是不可变的
# website='http://www.python.org'
# #分片赋值不合法
# website[-3:]='com'
# print(website)
# TypeError: 'str' object does not support item assignment
# 3.2字符串格式化：精简版
# 字符串格式化操作符%
# 在%的左侧放置一个字符串（格式化字符串），而右侧则放置希望被格式化的值。可以使用一个值，如一个字符串或数字，也
# 可以使用多个值的元组或字典。一般情况下使用元组。
format = "Hello,%s.%s enough for ya?"
values = ('world', 'Hot')
print(format % values)  # Hello,world.Hot enough for ya?
# 如果要在格式化字符串里面包含百分号，那么必须使用%%
format = "Pi with three decimals:%.3f"
from math import pi

print(format % pi)  # Pi with three decimals:3.142

# 模版字符串
# String模式提供另外一种格式化值的方法：模版字符串。类似shell里的变量替换。substitute这个模版方法会用传递进来
# 的关键字参数foo替换字符串中的$foo
from string import Template

s = Template('$x,glorious $x!')
print(s.substitute(x='slurm'))
# 如果替换字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾：
s = Template("It's ${x}tasitc!")
print(s.substitute(x='slurm'))
# 可以使用$$插入美元符号：
s = Template("Make $$ selling $x!")
print(s.substitute(x='slurm'))
# 除了关键字参数外，可以使用字典变量提供值/名称对。
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))

# 3.3字符串格式化完整版
# 右操作数是元组的话，每个元素都会被单独格式化。
print('%s plus %s equals %s' % (1, 1, 2))
# （1）%标记转换说明符的开始
# （2）转换标志：-表示左对齐；+表示在转换值之前要加上正负号；" "（空白字符）表示正数之前保留空格。0表示
# 转换值若位数不够则用0填充。
# （3）最小字段宽度：转换后的字符串至少应该具有该值指定的宽度，如果是*，宽度会从值元组中读出。
# （4）点后跟精度值：如果转换为实数，精度值就表示出现在小数点后的位数。如果转换的是字符串，那么该数字就表示最大
# 字段宽度。如果是*，精度从元组中读取。
# 带符号的十进制整数
print('Price of eggs:$%d' % 42)
# 不带符号的十六进制小写
print('Hexadecimal Price of eggs:%x' % 42)

from math import pi

# 十进制浮点数
print('Pi:%f...' % pi)
# 字符宽10
print('%10f' % pi)
# 字符宽10，精度2
print('%10.2f' % pi)
# 精度2
print('%2f' % pi)
# s字符串取前5位
print('%.5s' % 'Guido van Rossum')
# 使用*作为字段宽度或者精度，数值会从元组参数中读取。
print('%.*s' % (5, 'Guido van Rossum'))
# 3.3.3符号、对齐和用0填充
# 字段宽度为10，用0填充空位
print('%010.2f' % pi)
# -左对齐数值
print('%-10.2f' % pi)

# 对齐时有用
# " "在正数前加上空格
print(('% 5d' %10) + '\n' + ('% 5d' %(-10)))
# '+'不管是正数还是负数都标出符号
print(('%+5d' %10) + '\n' + ('+5d' %(-10)))
