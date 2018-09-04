# 字符串方法
# 字符串从String模块中继承了很多方法
# string.digits:包含0-9的字符串
# string.letters:包含所有字母（大小写）的字符串
# string.lowercase:包含所有小写字母的字符串
# string.printable:包含所有可打印字符的字符串
# string.punctuation:包含所有标点的字符串
# string.uppercase:包含所有大写字母的字符串
# 3.4.1find
# find可以在一个较长的字符串中查找子串。它返回子串所在位置的最左端索引。如果没有找到则返回-1。
# print('With a moo-moo here,and a moo-moo there.'.find('moo'))
# title="Monty Python's Flying Circus"
# print(title.find('Monty'))
# print(title.find('Flying'))
# print(title.find('Python'))
# print(title.find('Zirquss'))
subject = '$$$ Get rich now!!!$$$'
print(len(subject))
print(subject.find('$$$'))
print(subject.find('$$$', 1))
print(subject.find('!!!'))
# 提供起始点和结束点
print(subject.find('!!!', 0, 23))
print(subject.find('!!!', 0, 16))
# rfind  Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
# find()方法语法：
# str.rfind(str, beg=0 end=len(string))
# 参数
# str -- 查找的字符串
# beg -- 开始查找的位置，默认为 0
# end -- 结束查找位置，默认为字符串的长度。
# 返回值
# 返回字符串最后一次出现的位置，如果没有匹配项则返回-1

# #index Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# 语法
# index()方法语法：
# str.index(str, beg=0, end=len(string))
# 参数
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。

# rindex Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，
# 你可以指定可选参数[beg:end]设置查找的区间。
# 语法
# rindex()方法语法：
# str.rindex(str, beg=0 end=len(string))
# 参数
# str -- 查找的字符串
# beg -- 开始查找的位置，默认为0
# end -- 结束查找位置，默认为字符串的长度。

# count Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# 语法
# count()方法语法：
# str.count(sub, start= 0,end=len(string))
# 参数
# sub -- 搜索的子字符串
# start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
# end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

# startswith Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
# 如果参数 beg 和 end 指定值，则在指定范围内检查。
# 语法
# startswith()方法语法：
# str.startswith(str, beg=0,end=len(string));
# 参数
# str -- 检测的字符串。
# strbeg -- 可选参数用于设置字符串检测的起始位置。
# strend -- 可选参数用于设置字符串检测的结束位置。

# endswith Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
# 可选参数"start"与"end"为检索字符串的开始与结束位置。
# 语法
# endswith()方法语法：
# str.endswith(suffix[, start[, end]])
# 参数
# suffix -- 该参数可以是一个字符串或者是一个元素。
# start -- 字符串中的开始位置。
# end -- 字符中结束位置。
# 3.4.2
# join join方法是非常重要的字符串方法，它是split方法的逆方法，用来连接序列中的元素：

seq = ['1', '2', '3', '4', '5']
# 需要被连接的序列元素都必须是字符串。
print('+'.join(seq))
dir = '', 'usr', 'bin', 'env'
print('/'.join(dir))
# split Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
# 语法
# split() 方法语法：
#
# str.split(str="", num=string.count(str)).
# 参数
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。

# 3.4.3 lower 返回字符串的小写字母版
print('Trondhe in Hammer Dance'.lower())
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names:
    print('Fount it!')
# translate Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
# 语法
# translate()方法语法：
# str.translate(table[, deletechars]);
# 参数
# table -- 翻译表，翻译表是通过maketrans方法转换而来。
# deletechars -- 字符串中要过滤的字符列表。
# islower Python islower() 方法检测字符串是否由小写字母组成。
# 语法
# islower()方法语法：
# str.islower()
# capitalize Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
# 语法
# capitalize()方法语法：
# str.capitalize()
# swapcase Python swapcase() 方法用于对字符串的大小写字母进行转换。
# 语法
# swapcase()方法语法：
# str.swapcase();
# title Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
# 语法
# title()方法语法：
# str.title();
print("that's all,folks".title())
import string

print(string.capwords("that's all,folks"))
# istitle Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
# 语法
# istitle()方法语法：
# str.istitle()
# upper Python upper() 方法将字符串中的小写字母转为大写字母。
# 语法
# upper()方法语法：
# str.upper()
# isupper Python isupper() 方法检测字符串中所有的字母是否都为大写。
# 语法
# isupper()方法语法：
# str.isupper()

# 3.4.4replace 返回某字符串的所有匹配项均被替换之后得到字符串
print('This is a test'.replace('is', 'eez'))

# 3.4.5split join方法的逆方法，用来将字符串分隔成序列。
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
print('Using the default'.split())
# 如果不提供任何分隔符，程序会把所有空格作为分隔符（空格、制表、换行等）
#  splitlines Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
# 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
#
# 语法
# splitlines()方法语法：
#
# str.splitlines([keepends])
# 参数
# keepends -- 在输出结果里是否保留换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
# 3.4.6strip返回去除两侧（不包括内部）空格的字符串：
print('             internal whitespace is kept    '.strip())
names = ['gumby', 'smith', 'jones']
name = 'gumby'
if name in names:
    print('Found it!')
if name.strip() in names:
    print('Found it!')
# 也可以指定需要去除两侧的字符
print('***SPAM*for*everyone!!!***'.strip('*!'))
# lstrip Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
# 语法
# lstrip()方法语法：
# str.lstrip([chars])
# 参数
# chars --指定截取的字符。
# 返回值
# 返回截掉字符串左边的空格或指定字符后生成的新字符串。
# rstrip Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
#
# 语法
# rstrip()方法语法：
#
# str.rstrip([chars])
# 参数
# chars -- 指定删除的字符（默认为空格）
# 返回值
# 返回删除 string 字符串末尾的指定字符后生成的新字符串。

# 3.4.7translate 可以同时进行多个替换
# 举例：将纯正的英文文本转换为带有德国口音的版本。为此需要把字符串c替换为k把s替换为z.
from string import maketrans
str = "this is string example....wow!!!"
table=maketrans('cs','kz')
print(str.translate(table))