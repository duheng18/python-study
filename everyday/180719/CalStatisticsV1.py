# 基本统计值计算
# 问题分析
# 需求：给出一组数据，对它们有个概要理解
# 如：总个数、求和、平均值、方差、中位数...
# 基本统计值 ：
# (1)总个数：len()
# (2)求和：for...in
# (3)平均值：求和/总个数
# (4)方差：各数据与平均数差的平方和的平均数
# (5)中位数：排序，然后...奇数找中间1个，偶数找中间2个取平均。
# 技术能力扩展 (1)获取多个数据：从控制台获取多个不确定数据的方法  (2)分隔多个函数：模块化设计方法  (3)充分利用python提供的内置函数
# 集合类型、序列类型、字典类型是组合数据类型的三种表达形式



def getNum():  # 获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)


def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getNum()
m = mean(n)
print("平均值:{},方差:{},中位数:{}.".format(m, dev(n, m), median(n)))
