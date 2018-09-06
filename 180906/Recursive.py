# 递归
# 计算n!
# 第一种非递归
def factor(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factor(4))


# 递归
def factor(n):
    # 1的阶乘是1
    if n == 1:
        return 1
    else:
        # 大于1的数n的阶乘是n乘n-1的阶乘
        return n * factor(n - 1)


print(factor(5))


# x的n次幂
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


print(power(3, 4))


def power(x, n):
    # 对于任意数字x来说，power(x,0)是1
    if n == 0:
        return 1
    else:
        # 对于任意大于0的数来说，power(x,n)是x乘以（想，n-1）的结果
        return x * power(x, n - 1)


print(power(4, 3))
