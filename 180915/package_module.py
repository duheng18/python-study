# 包->探究模块
# 模块中有什么
# 1.使用dir
import copy

print(dir(copy))

# 列表推导式是个包含dir(copy)中所有不以下划线开头的名字的列表。
# import copy
# [n for n in dir(copy) if not n.startswith('_')]
# ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']

# 2.__all__变量
print(copy.__all__)

# 用help获取帮助
# copy带有一个参数x，并且是“浅复制操作”
help(copy.copy)
# 直接检查文档字符串
print(copy.copy.__doc__)

# 文档
print(range.__doc__)

# 使用源代码
print(copy.__file__)
# /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/copy.py

# 标准库
# sys模块
import sys

# 变量sys.argv包含传递到Python解释器的参数，包括脚本名称。
print(sys.argv)

# 可以退出当前程序。
print(sys.exit)

# 将模块名映射到实际存在的模块上，它只应用于目前导入的模块。
print(sys.modules)

# 它是一个字符串列表，其中的每个字符串都是一个目录名，在import语句执行时，解释器就会从这些目录中查找模块。
print(sys.path)

# sys.platform模块变量是解释器正在其上运行的“平台”名称。
print(sys.platform)

# sys.stdin、sys.stdout和sys.stdout模块变量是类文件流对象。
