# 函数定义时可以为某些参数指定默认值，构成可选参数
# def <函数名>(<非可选参数>,<可选参数>):
#     <函数体>
#     return <返回值>

# 计算n!//m
def fact(n, m=1):  # m=1 如果给出了第二个参数m，我们就用给的实际值。如果不给，我们就把m设为1，去进行下面的运算。
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m


print(fact(10))
print(fact(10, 5))
