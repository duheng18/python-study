# 可变参数传递
# 函数定义时可以设计可变数量参数，既不确定参数总数量
# def <函数名>(<参数>,*b):
#     <函数体>
#     return <返回值>
def fact(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


a = fact(10, 3)
b = fact(10, 3, 5, 8)
print(a, b)
