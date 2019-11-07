__metaclass__ = type


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)


r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
r.size = 150, 100
print(r.width)
# property() 函数的作用是在新式类中返回属性值。
# 以下是 property() 方法的语法:
# class property([fget[, fset[, fdel[, doc]]]])
# 参数
# fget -- 获取属性值的函数
# fset -- 设置属性值的函数
# fdel -- 删除属性值函数
# doc -- 属性描述信息
# 返回新式类属性。