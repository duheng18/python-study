# 函数的参数传递
# 参数个数
# 函数可以有参数，也可以没有，但必须保留括号
# def <函数名>():
#     <函数体>
#     return <返回值>

def fact():
    print("我也是函数")


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


a = fact(10)
print(a)
