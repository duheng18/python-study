# 函数
# 函数的定义
# 函数是什么：
#   实现了某一功能，可被重复使用的代码段。
#   参数的意义是从外面与函数里面沟通，返回值的意义是里面与外面沟通。
# 定义一个函数：
#   def functionname(parameters):
#       #函数注释，功能说明
#       代码
#       return value
# 无返回，有返回，无参数，有参数，有多个参数...
# 不同类型参数
# 位置参数
#   调用函数时根据函数定义的参数位置来传递参数
# 关键字参数
#   用于函数调用，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
# 默认参数
#   用于定义函数，为参数提供默认值，调用函数时可传可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
# 不定长参数
#   定义函数时，有时候我们不确定调用的时候会传递多少个参数（不传参也可以）。此时可用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递，会显示非常方便。
# 解包参数
#   *和**，也可以在函数调用的时候使用，称之为解包（unpacking）
# 位置参数、默认参数，可变参数的混合使用
def hello_func(greeting, name='linda'):  # 位置参数、关键字参数、默认值
    return '{}{}你好.'.format(greeting, name)


print(hello_func('hi'))
print(hello_func('hi', 'tom'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['python', 'java']
info = {'name': 'linda', 'age': 18}
student_info(courses, info)
student_info(*courses,**info)


def foo(x, *args, a=4, **kwargs):  # 使用默认参数时，注意默认参数的位置在args之后kwargs之前
    print(x)
    print(a)
    print(args)
    print(kwargs)


foo(1, (5, 6, 7, 8), {"y": 2, "z": 3})  # 调用函数，不改默认参数
foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)  # 调用函数，不改默认参数

# 匿名函数
add = lambda x, y: x + y
add1 = lambda *args: sum(args)
print(add1(1, 56, 35))
