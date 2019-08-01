def flattern(nested):
    try:
        for sublist in nested:
            for element in flattern(sublist):
                yield element
    except TypeError:
        yield nested


# print(list(flattern([[[[1], 2]], 3, 4, [5, [6, 7]], 8])))
def flattern(nested):
    try:
        # 不要迭代类似字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield nested


# print(list(flattern(['foo', ['bar', ['baz']]])))
# ['f', 'o', 'o', 'bar', ['baz']]

# 通用生成器
# 生成器由两部分组成：生成器的函数和生成器的迭代器。生成器的函数是用def语句定义的，
# 包含yield的部分，生成器的迭代器是这个函数返回的部分。
def simple_generator():
    yield 1


# print(simple_generator())  # <generator object simple_generator at 0x10418feb8>
# print(simple_generator)  # <method simple_generator at 0x101bcfe18>

# 生成器方法
# 1.外部作用域访问生成器的send方法，就像访问next方法一样，只不过前者使用一个参数（要发送的“消息”--任意对象）
# 2.在内部则挂起生成器，yield现在作为表达式而不是语句使用。即当生成器重新运行的时候，
# yield方法返回一个值，也就是外部通过send方法发送的值。如果next方法被使用，那么yield方法返回None。
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new


r = repeater(42)


# print(r.__next__())
# print(r.send("Hello,world!"))

# 模拟生成器
# flatten生成器用普通的函数重写的版本
def flatten(nested):
    result = []
    try:
        # 不要迭代类似字符串的对象：
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flattern(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
