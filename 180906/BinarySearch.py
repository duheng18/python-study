# 二分查找法
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1

    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)

        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
# print(seq)
print(search(seq, 34))
print(search(seq, 100))

# 函数式编程
# map函数将序列中的元素全部传递给一个函数：
print(list(map(str, range(10))))
print([str(i) for i in range(10)])


# fiter函数可以基于一个返回布尔值的函数对元素进行过滤
def func(x):
    return x.isalnum()


seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))
print([x for x in seq if x.isalnum()])
# lambda
print(list(filter(lambda x: x.isalnum(), seq)))

# reduce
# 在python 3.0.0.0以后, reduce已经不在built-in function里了
from functools import reduce

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
print(reduce(lambda x, y: x + y, numbers))
