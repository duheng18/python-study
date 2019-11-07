# -*- coding:utf-8 -*-
# 1. 打开远程文件
# 几乎可以像打开本地文件一样打开远程文件，差别是只能使用读取模式，以及使用模块 urllib.request中的函数urlopen，而不是open(或file)。
# from urllib.request import urlopen
# import re
# import ssl
#
# webpage = urlopen('http://www.python.org')
# # 注意 要在没有联网的情况下尝试使用模块urllib，可使用以file:打头的URL访问本地文件，如file:c:\text\somefile.txt(别忘了对反斜杠进行转义)。
# # urlopen返回的类似于文件的对象支持方法close、read、readline和readlines，还支持迭代等。
# text = webpage.read()
# m = re.search(b'<a href="([^"]+)".*?>about</a>', text, re.IGNORECASE)
# print(m.group(1))
from urllib import request

response = request.urlopen(
    r'http://python.org/')  # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
# 直接用urllib.request模块的urlopen（）获取页面，page的数据格式为bytes类型，需要decode（）解码，转换成str类型。
page = response.read()
page = page.decode('utf-8')
