# 规则1：局部变量和全局变量是不同变量
# -局部变量是函数内部的占位符，与全局变量可能重名但不同
# -函数运算结束后，局部变量被释放
# -可以使用global保留字在函数内部使用全局变量
n, s = 10, 100


def fact(n):
    global s            #fact()函数中使用global保留字声明此处s是全局变量s
    for i in range(1, n + 1):
        s *= i
    return s        #此处s指全局变量s


print(fact(n), s)   #此处全局变量s被函数修改
