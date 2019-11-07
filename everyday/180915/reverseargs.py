# coding:utf-8

# 标准库
# sys模块 这个模块让你能够访问与Python解释器联系紧密的变量和函数。
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


# 反序打印命令行参数
# reverseargs.py
import sys

args = sys.argv[1:]
args.reverse()
print(args)
# print(''.join(args))
print(' '.join(reversed(sys.argv[1:])))

# python reverseargs.py this is a test
# test a is this
# 命令行参数 参数个数：len(sys.argv) 脚本名：sys.argv[0] 参数1：sys.argv[1] sys.argv[2]
