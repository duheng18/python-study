# 随机存取
# 在本章中，我将文件都视为流，只能按顺序从头到尾读取。实际上，可在文件中移动，只访问感兴趣的部分(称为随机存取)。为此，可使用文件对象的两个方法:
# seek 和 tell。方法 seek(offset[, whence])将当前位置(执行读取或写入的位置)移到offset和whence指定的地方。参数offset指定了字节(字符)数，
# 而参数 whence 默认为 io.SEEK_SET (0)，这意味着偏移量是相对于文件开头的(偏移量不能为负数)。参数 whence 还可设置 为 io.SEEK_CUR(1)或
# io.SEEK_END(2)，其中前者表示相对于当前位置进行移动(偏移量可以为负)，而后者表示相对于文件末尾进行移动。
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile.txt', 'w')
print(f.write('01234567890123456789'))
# 20
print(f.seek(5))
# 5
print(f.write('Hello, World!'))
# 13
f.close()
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile.txt')
print(f.read())
# 01234Hello, World!89
# 方法 tell()返回当前位于文件的什么位置，如下例所示:
f = open(r'/Users/baidu/Downloads/dh/python/180917/somefile.txt')
print(f.read(2))
# 01
print(f.read(3))
# 234
print(f.tell())
# 5
