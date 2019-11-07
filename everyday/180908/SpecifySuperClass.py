# 指定超类
# 将其他类名可以写在class语句后的圆括号内可以指定超类：
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    # 新定义的方法重写了Filter的init定义
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
# filter方法的定义是从Filter类中继承过来的。
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
# 已知类的基类
print(SPAMFilter.__bases__)
print(Filter.__bases__)
s = SPAMFilter()
# 使用isinstance()方法检查一个对象是否是一个类的实例
# s是SPAMFilter的直接实例
print(isinstance(s, SPAMFilter))
# s是Filter的间接实例
print(isinstance(s, Filter))
print(isinstance(s, str))
# 一个对象属于哪个类
print(s.__class__)
print(type(s))
