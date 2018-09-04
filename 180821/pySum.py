#对两个一维数组进行运算
def pySum():
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
        print(c)
    return c


print(pySum())
