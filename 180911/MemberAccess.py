# 基本的序列和映射规则
# __len__（self）:返回集合中所含项目的数量
# __getitem__(self,key):返回与所给键对应的值。
# __setitem__(self,key,value):按一定的方式存储和key相关的value.该值随后可使用__getitem__来获取。
# __delitem__(self,key):对一部分对象使用del语句时被调用，同时必须删除和键相关的键。
# 对于一个序列来说，如果键是负整数，那么要从末尾开始计数。即x[-n]和x[len(x)-n]是一样的。
# 如果键是不合适的类型，会引发一个TypeError异常。（对序列使用字符串作为键）
# 如果序列的索引是正确的类型，但超出了范围，应该引发一个IndexError异常。
def checkIndex(key):
    """所给的键是能接受的索引吗？
    为了能被接受，键应该是一个非负的整数。如果它不是一个整数，会引发TypeError;如果它是负数，则会引发IndexError
    (因为序列是无限长的。)
    """

    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化算术序列
        起始值-序列中的第一个值
        步长-两个相邻值之间的差别
        改变-用户修改的值的字典
        :param start:
        :param step:
        """
        self.start = start  # 保存开始值
        self.step = step  # 保存步长值
        self.changed = {}  # 没有项被修改

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        :param key:
        :return:
        """
        checkIndex(key)

        try:
            return self.changed[key]  # 修改了吗？
        except KeyError:  # 否则...
            return self.start + key * self.step  # ...计算值

    def __setitem__(self, key, value):
        """
        修改算术序列中的一个项
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key] = value  # 保存更改后的值
