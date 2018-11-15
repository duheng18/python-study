# -*- coding:utf-8 -*-
# 1. 打开远程文件
# 几乎可以像打开本地文件一样打开远程文件，差别是只能使用读取模式，以及使用模块 urllib.request中的函数urlopen，而不是open(或file)。
from urllib.request import urlopen
import re

webpage = urlopen('http://www.python.org')
# 注意 要在没有联网的情况下尝试使用模块urllib，可使用以file:打头的URL访问本地文件，如file:c:\text\somefile.txt(别忘了对反斜杠进行转义)。
# urlopen返回的类似于文件的对象支持方法close、read、readline和readlines，还支持迭代等。
text = webpage.read()
m = re.search(b'<a href="([^"]+)".*?>about</a>', text, re.IGNORECASE)
print(m.group(1))
