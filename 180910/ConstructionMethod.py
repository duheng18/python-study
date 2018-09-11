# 第一个魔法方法：构造方法
class FooBar:
    def __init__(self):
        self.somevar = 42


f = FooBar()


# print(f.somevar)


class FooBar:
    def __init__(self, value=42):
        self.somevar = value


f = FooBar()
# print(f.somevar)
f = FooBar("This is a constructor argument")
print(f.somevar)
# __del__析构方法：它在对象就要被垃圾回收之前调用。因调用的时间不可知，尽量避免使用。
