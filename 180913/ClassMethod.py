__metaclass__ = type


class MyClass:
    def smeth(self):
        print('This is a static method')
        smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of'.cls)
        cmeth = classmethod(cmeth)
#使用装饰器
__metaclass__=type
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
MyClass.smeth()
MyClass.cmeth()