'''
1.创建 Regex 对象的函数是什么?
2.在创建 Regex 对象时，为什么常用原始字符串?
3.search()方法返回什么?
4.通过 Match 对象，如何得到匹配该模式的实际字符串?
5.用 r'(\d\d\d)-(\d\d\d-\d\d\d\d)'创建的正则表达式中，分组 0 表示什么?分组 1呢?分组 2 呢?
6.括号和句点在正则表达式语法中有特殊的含义。如何指定正则表达式匹配真正的括号和句点字符?
7.findall()方法返回一个字符串的列表，或字符串元组的列表。是什么决定它提供哪种返回?
8.在正则表达式中，|字符表示什么意思?
9.在正则表达式中，?字符有哪两种含义?
10.在正则表达式中，+和*字符之间的区别是什么?
11.在正则表达式中，{3}和{3,5}之间的区别是什么?
12.在正则表达式中，\d、\w 和\s 缩写字符类是什么意思?
13.在正则表达式中，\D、\W 和\S 缩写字符类是什么意思?
14.如何让正则表达式不区分大小写?
15.字符.通常匹配什么?如果 re.DOTALL 作为第二个参数传递给 re.compile()，它会匹配什么?
16..*和*?之间的区别是什么?
17.匹配所有数字和小写字母的字符分类语法是什么?
18.如果 numRegex = re.compile(r'\d+')，那么 numRegex.sub('X', '12 drummers, 11
pipers, five rings, 3 hens')返回什么?
19.将 re.VERBOSE 作为第二个参数传递给 re.compile()，让你能做什么?
20.如何写一个正则表达式，匹配每 3 位就有一个逗号的数字?它必须匹配以
下数字:
 '42'
 '1,234'
 '6,368,745'
但不会匹配:
 '12,34,567' (逗号之间只有两位数字)  '1234' (缺少逗号)
21.如何写一个正则表达式，匹配姓 Nakamoto 的完整姓名?你可以假定名字 总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配:
 'Satoshi Nakamoto'
 'Alice Nakamoto'
 'RoboCop Nakamoto
但不匹配:
 'satoshi Nakamoto'(名字没有大写首字母)
 'Mr. Nakamoto'(前面的单词包含非字母字符)
 'Nakamoto' (没有名字)
 'Satoshi nakamoto'(姓没有首字母大写)
22.如何编写一个正则表达式匹配一个句子，它的第一个词是 Alice、Bob 或Carol，第二个词是 eats、pets 或 throws，第三个词是 apples、cats 或 baseballs。该句 子以句点结束。这个正则表达式应该不区分大小写。它必须匹配:
 'Alice eats apples.'
 'Bob pets cats.'
 'Carol throws baseballs.'
 'Alice throws Apples.'
 'BOB EATS CATS.'
但不匹配:
 'RoboCop eats apples.'
 'ALICE THROWS FOOTBALLS.'
 'Carol eats 7 cats.'


7.18.1 强口令检测
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的 定义是:长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。你可 能需要用多个正则表达式来测试该字符串，以保证它的强度。
7.18.2 strip()的正则表达式版本
写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。如果只 传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否 则，函数第二个参数指定的字符将从该字符串中去除。
'''
# 1.创建 Regex 对象的函数是什么?
# 1.re.compile() 函数返回 Regex 对象。
# 2.在创建 Regex 对象时，为什么常用原始字符串?
# 2.使用原始字符串是为了让反斜杠不必转义。
# 3.search()方法返回什么?
# 3.search() 方法返回 Match 对象。
# 4.通过 Match 对象，如何得到匹配该模式的实际字符串?
# 4.group() 方法返回匹配文本的字符串。
# 5.用 r'(\d\d\d)-(\d\d\d-\d\d\d\d)'创建的正则表达式中，分组 0 表示什么?分组 1呢?分组 2 呢?
# 5.分组 0 是整个匹配，分组 1 包含第一组括号，分组 2 包含第二组括号。
# 6.括号和句点在正则表达式语法中有特殊的含义。如何指定正则表达式匹配真正的括号和句点字符?
# 6.句号和括号可以用反斜杠转义:\.、\(和\)。
# 7.findall()方法返回一个字符串的列表，或字符串元组的列表。是什么决定它提供哪种返回?
# 7.如果正则表达式没有分组，就返回字符串的列表。如果正则表达式有分组，就返回字符串的元组的列表。
# 8.在正则表达式中，|字符表示什么意思?
# 8.| 字符表示匹配两个组中的“任何一个”。
# 9.在正则表达式中，?字符有哪两种含义?
# 9.? 字符可以表示“匹配前面分组 0 次或 1 次”，或用于表示非贪心匹配。
# 10.在正则表达式中，+和*字符之间的区别是什么?
# 10.+匹配 1 次或多次。*匹配 0 次或多次。
# 11.在正则表达式中，{3}和{3,5}之间的区别是什么?
# 11.{3}匹配前面分组的精确 3 次实例。{3, 5} 匹配 3 至 5 次实例。
# 12.在正则表达式中，\d、\w 和\s 缩写字符类是什么意思?
# 12.缩写字符分类\d、\w 和\s 分别匹配一个数字、单词或空白字符。
# 13.在正则表达式中，\D、\W 和\S 缩写字符类是什么意思?
# 13.缩写字符分类\D、\W 和\S 分别匹配一个字符，它不是数字、单词或空白字符。
# 14.如何让正则表达式不区分大小写?
# 14.将 re.I 或 re.IGNORECASE 作为第二个参数传入 re.compile()，让匹配不区分大小写。
# 15.字符.通常匹配什么?如果 re.DOTALL 作为第二个参数传递给 re.compile()，它会匹配什么?
# 15.字符.通常匹配任何字符，换行符除外。如果将 re.DOTALL 作为第二个参数传入 re.compile()，那么点也会匹配换行符。
# 16..*和*?之间的区别是什么?
# 16..*执行贪心匹配，.*?执行非贪心匹配。
# 17.匹配所有数字和小写字母的字符分类语法是什么?
# 17.[0-9a-z]或[a-z0-9]
# 18.如果 numRegex = re.compile(r'\d+')，那么 numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')返回什么?
# 18.'X drummers, X pipers, five rings, X hens'
# 19.将 re.VERBOSE 作为第二个参数传递给 re.compile()，让你能做什么?
# 19.re.VERBOSE 参数允许为传入 re.compile() 的字符串添加空格和注释。
# 20.如何写一个正则表达式,匹配每3位就有一个逗号的数字?它必须匹配以下数字:
#  '42'
#  '1,234'
#  '6,368,745'
# 但不会匹配:
#  '12,34,567' (逗号之间只有两位数字)
#  '1234' (缺少逗号)
import re

regex = re.compile(r'^\d{1,3}(\,\d{3})*$')
mo1 = regex.search('42')
mo2 = regex.search('1,234')
mo3 = regex.search('6,368,745')
mo4 = regex.search('12,34,567')
mo5 = regex.search('1234')
print(mo1.group())
print(mo2.group())
print(mo3.group())
# print(mo4.group())
# print(mo5.group())
# 21.如何写一个正则表达式，匹配姓 Nakamoto 的完整姓名?你可以假定名字 总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配:
#  'Satoshi Nakamoto'
#  'Alice Nakamoto'
#  'RoboCop Nakamoto'
# 但不匹配:
#  'satoshi Nakamoto'(名字没有大写首字母)
#  'Mr. Nakamoto'(前面的单词包含非字母字符)
#  'Nakamoto' (没有名字)
#  'Satoshi nakamoto'(姓没有首字母大写)
regex = re.compile(r'[A-Z][a-z]*\sNakamoto')
mo6 = regex.search('Satoshi Nakamoto')
mo7 = regex.search('Alice Nakamoto')
mo8 = regex.search('RoboCop Nakamoto')
mo9 = regex.search('satoshi Nakamoto')
mo10 = regex.search('Mr. Nakamoto')
mo11 = regex.search('Nakamoto')
mo12 = regex.search('Satoshi nakamoto')
print(mo6.group())
print(mo7.group())
print(mo8.group())
# print(mo9.group())

# 22.如何编写一个正则表达式匹配一个句子，它的第一个词是 Alice、Bob 或Carol，第二个词是 eats、pets 或 throws，
# 第三个词是 apples、cats 或 baseballs。该句 子以句点结束。这个正则表达式应该不区分大小写。它必须匹配:
#  'Alice eats apples.'
#  'Bob pets cats.'
#  'Carol throws baseballs.'
#  'Alice throws Apples.'
#  'BOB EATS CATS.'
# 但不匹配:
#  'RoboCop eats apples.'
#  'ALICE THROWS FOOTBALLS.'
#  'Carol eats 7 cats.'
regex=re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.IGNORECASE)
mo13=regex.search('Alice eats apples.')
mo14=regex.search('Bob pets cats.')
mo15=regex.search('Carol throws baseballs.')
mo16=regex.search('Alice throws Apples.')
mo17=regex.search('BOB EATS CATS.')
print(mo13.group())
print(mo14.group())
print(mo15.group())
print(mo16.group())
print(mo17.group())
