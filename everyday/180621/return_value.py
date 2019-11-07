# 函数的返回值
# 函数可以返回0个或多个结果
# return保留字用来传递返回值
# 函数可以有返回值，也可以没有，可以用return，也可以没有
# return可以传递0个返回值，也可以传递任意多个返回值

# 函数可以返回0个或多个结果
def fact(n, m=1):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s // m, m, n


m = fact(10, 5)
# (725760, 5, 10)打印结果为元组类型
print(m)
a, b, c = fact(10, 5)
# 725760 5 10
print(a, b, c)
