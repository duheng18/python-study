# 1.将模块放置在正确位置。只需要找出Python解析器从哪里查找模块，然后将自己的文件放置在那里即可。
import sys, pprint

# 搜索路径的目录列表可以在sys模块中的path变量中找到。
# pprint.pprint(sys.path)
# 将模块放入类似site-packages这样的目录中，所有程序就都能将其导入了。
# 2.告诉编译器去哪里找
# 1的解决方案对于以下几种情况可能并不适用：（1）不希望将自己的模块填满Python解释器的目录；（2）没有在python解释器目录中存储文件的权限；
# （3）想将模块放在其他地方。
# 使用环境变量
# 3.命令模块
import copy

print(dir(copy))

# 列表推导式是个包含dir(copy)中所有不以下划线开头的名字的列表。
# import copy
# [n for n in dir(copy) if not n.startswith('_')]
# ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']
