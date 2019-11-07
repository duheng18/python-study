# 元组类型及操作
# 元组是序列类型中的一种扩展，元组一旦创建就不能修改
# 使用小括号()或者tuple()创建，元素间用逗号,分隔
# 元组类型继承了序列类型的全部通用操作
# 元组因为创建后不能修改，因此没有特殊操作

# 可以使用或不使用小括号如下所示：
# 1,2本身就是一个元组类型
def func():
    return 1, 2


creature = "cat", "dog", "tiger", "human"
color = (0x001100, "blue", creature)
print(color)
print(creature)

# 切片形式对元组类型的元素进行提取，提取之后生成新的元组，不改变原有元组值，生成一个新的元组
print(creature[::-1])

print(color[-1][2])
