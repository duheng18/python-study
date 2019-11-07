# __getattribute__(self,name):当特性name被访问时自动被调用。
# __getattr__(self,name):当特性name被访问且对象没有相应的特性是被自动调用。
# __setattr__(self,name,value):当试图给特性name赋值时会被自动调用。
# __delattr__(self,name):当试图删除特性name时被自动调用。

class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, name, value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value
    def __getattr__(self, name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError