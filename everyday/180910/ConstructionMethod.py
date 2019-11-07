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
# print(f.somevar)


# __del__析构方法：它在对象就要被垃圾回收之前调用。因调用的时间不可知，尽量避免使用。

class A:
    def hello(self):
        print("Hello,I'm A.")


class B(A):
    pass


a = A()
b = B()
# a.hello()
# b.hello()
class B(A):
    def hello(self):
        print("Hello,I'm B.")
b=B()
# b.hello()

class Bird:
    def __init__(self):
        self.hurry=True
    def eat(self):
        if self.hurry:
            print('Aaaah...')
            self.hurry=False
        else:
            print('No,thanks!')
b=Bird()
b.eat()
b.eat()
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound='Squawk!'
    def sing(self):
        print(self.sound)
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()