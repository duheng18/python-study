# 从迭代器得到序列
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


t = TestIterator()
t1 = list(t)
print(t1)
