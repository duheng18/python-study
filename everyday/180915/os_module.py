# os模块提供了访问多个操作系统服务的功能。os和它的子模块os.path还包括一些用于检查、构造、删除目录和文件的函数，以及一些处理路径的函数。
# os模块中一些重要函数和变量
# os.environ 对环境变量进行映射
# import os
#
# print(os.environ['PYTHONPATH']  # 映射也可以用来更改系统环境变量，并非所有系统都支持。

# os.system(command)函数用于运行外部程序。也有一些函数可以执行外部程序。subprocess模块包括os.system、execv、popen函数
# os.sep模块变量是用于路径名中的分隔符。unix标准分隔符"/",Windows中是“\\”,Mac OS用“::”
# os.pathsep组织路径 pathsep用于分割路径名：UNIX使用“:”,Windows使用“:”,Mac OS使用“::”
# os.linesep用于文本文件的字符串分隔符。UNIX中为一个换行符（\n）,Mac OS中为单个回车符（\r）,Windows则是两者的组合（\r\n）.
# os.urandom(n)返回n字节的加密强随机数据。

# 启动网络浏览器
# 注意：在Windows中os.system(或者os.startfile)启动了外部程序之后，Python程序仍然会继续运行。而在UNIX中，程序则会中止，
# 等待os.system命令完成。

# webbrowser模块包括open函数，自动启动Web浏览器访问给定的URL.
import webbrowser

webbrowser.open('http://www.python.org')
