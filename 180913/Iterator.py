# 迭代器
# __iter__方法会返回一个迭代器（iterator），所谓的迭代器就是具有next方法（这个方法在调用时不需要任何参数）的对象。在调用
# next方法时，迭代器会返回它的下一个值。如果next方法被调用，但迭代器没有值可以返回，就会引发一个StopIteration的异常。
# 使用迭代器的好处：更通用、更简单、更优雅
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


# 迭代器实现了__iter__方法，这个方法实际上返回迭代器本身。在很多情况下，__iter__会放到其他的会在for循环中使用的对象中。
# 正式的说法是，一个实现了__iter__方法的对象是可迭代的，一个实现了next方法的对象则是迭代器。

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

# 内建函数iter可以从可迭代的对象中获得迭代器。
it=iter([1,2,3])
print(it.__next__())
print(it.__next__())
