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
# /Library/Frameworks/Python.framework/Versions/3.6/lib/excise.6/copy.py


