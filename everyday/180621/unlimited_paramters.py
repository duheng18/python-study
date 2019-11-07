#函数实现传入的参数相乘，不限参数个数
def fact(n,*b):
    s = n
    for item in b:
        s *= item
    return s


a = fact(1, 3,10,2)
print(a)
