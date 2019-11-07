# read(n)
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile1.txt')
print(f.read(7))
# Welcome
print(f.read(4))
# to
f.close()

# read()
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile1.txt')
print(f.read())
# Welcome to this file
# There is nothing here except
# This stupid haiku
f.close()

# readline()
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile1.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline(), end=' ')
#     0: Welcome to this file
#  1: There is nothing here except
#  2: This stupid haiku
# str() 函数将对象转化为适于人阅读的形式。
# 以下是 str() 方法的语法:
# class str(object='')
# 参数
# object -- 对象。
# 返回值
# 返回一个对象的string格式。
f.close()

# readlines()
import pprint

pprint.pprint(open(r'/Users/baidu/Downloads/dh/python/180917/somefile1.txt').readlines())
# ['Welcome to this file\n',
#  'There is nothing here except\n',
#  'This stupid haiku']

# write(string)
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile2.txt', 'w')
print(f.write('this\nis no\nhaiku'))
# 16
f.close()

# writelines(list):
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile2.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile2.txt', 'w')
f.writelines(lines)
# this
# isn't a
# haiku
f.close()
