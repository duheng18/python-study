# 参数传递的两种方式
# 函数调用时，参数可以按照位置或名称方式传递
def fact(n, m=1):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m


# 10,5位置传递
a = fact(10, 5)
# m=5,n=10 名称传递
b = fact(m=5, n=10)
