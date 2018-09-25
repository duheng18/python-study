# 问题：假设你有无限数量的邮票,面值分别为6角，7角，8角,请问你最大的不可支付邮资是多少元？

# 假设6、7、8角各有50张（50张够了），先计算出所有的可能组合
# coding:utf-8
a = 6
b = 7
c = 8
t = 5  # 票的张数
s = []  # 排列组合全部放到这里
# 生成的组合
for i in range(t + 1):
    s1 = a * i
    s.append(s1)
    for j in range(t + 1):
        s2 = a * i + b * j
        s.append(s2)
        for k in range(t + 1):
            s3 = a * i + b * j + c * k
            s.append(s3)
# 先对组合就行排序，从小到大的顺序，排队站好，这里用到sort()函数（要是你用冒泡排序，那你就out啦！）
# sort函数只是对list序列排序，并没有返回值。排序完成后，接下来就是去掉重复的数据
# 排序
s.sort()
# 去掉重复
news = []
for i in s:
    if i not in news:
        news.append(i)
print(news)
print("组合生成的最大数%s" % news[-1])

# 提取不在列表列表中的数字
r = []
for i in range(6 * t):
    if i in news:
        pass
    else:
        r.append(i)
print("组合不能生成的数字%s" % r)
print("不能生成的最大数字为%s" % r[-1])
