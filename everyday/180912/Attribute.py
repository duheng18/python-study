# 访问器方法
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    # getSize setSize方法是名为size的假想特性的访问器方法
    def setSize(self, size):
        # size是由width,height构成的元组
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height


r = Rectangle()
r.width = 10
r.height = 5
print(r.getSize())
r.setSize((150, 100))
print(r.width)
