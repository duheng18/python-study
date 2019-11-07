# 例子
def story(**kwds):
    return 'Once upon a time, there was a' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:  # 如果没有为stop指定值.....
        start, stop = 0, start  # 指定参数 start=0 stop=start
        print('start%d' % start)
        print('stop%d' % stop)
    result = []
    i = start  # 计算start索引
    while i < stop:  # 直到计算到stop的索引
        result.append(i)  # 将索引添加到result内
        print(result)
        i += step  # 用step>0增加索引i
        print('step%d' % step)
    return result


# print(story(job='King', name='Gumby'))
# params=(5,)*2
# print(params)
# print(interval(10))
# print(interval(1, 5))
# print(interval(3,12,4))
print(power(*interval(3, 7)))
