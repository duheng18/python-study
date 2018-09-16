# 生成器是一种用普通的函数语法定义的迭代器。
# 创建生成器
nested = [[1, 2], [3, 4], [5, 6]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            # 任何包含yield语句的函数称为生成器
            # 它不像return那样返回值，而是每次产生多个值。每次产生一个值，函数就会被冻结：即函数停在那点等待被重新唤醒，函数被重新
            # 唤醒后就从停在的那点开始执行。
            yield element
nested=[[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)
print(list(flatten(nested)))

g=((i+2)**2 for i in range(2,27))
print(g.__next__())
m=sum(i**2 for i in range(10))
print(m)