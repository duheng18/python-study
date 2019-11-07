# -*- coding:utf-8 -*-
import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()

fhandle = open('1.html', 'wb')
fhandle.write(data)
fhandle.close()
