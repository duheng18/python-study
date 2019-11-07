# 封装（Encapsulation）：对外部世界隐藏对象的工作细节
# 封装是可以不用关心对象是如何构建的而直接进行使用。
# 多态
class OpenObject:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


o = OpenObject()
o.setName('Sir Lancelot')
print(o.getName())
# o1 = OpenObject()
# o2 = OpenObject()
# o1.setName('Robin Hood')
# print(o2.getName())

# 创建自己的类
__metaclass__ = type


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello,world!I'm %s." % self.name)


# foo = Person()
# bar = Person()
# foo.setName('Luke Skywalker')
# bar.setName('Snakin Skywalker')
# foo.greet()
# Person.greet(foo)
# bar.greet()
# print(foo.name)
# bar.name = 'Yoda'
# bar.greet()


# 绑定方法将他们的第一个参数绑定到所属的实例上，因此无需显示提供该参数。
# 当然也可以将特性绑定到一个普通函数上，这样就不会有特殊的self参数了。
class Class:
    def method(self):
        print('I have a self!')


def function():
    print("I don't ....")


#
# instance = Class()
# instance.method()
# instance.method = method
# instance.method()

# self参数并不依赖于调用方法的方式，使用instance.method(实例.方法)的形式，可以随意使用其他变量引用同一个方法：
class Bird:
    song = 'Squaawk!'

    def sing(self):
        print(self.song)

#
# bird = Bird()
# bird.sing()
# birdsong = bird.sing  # 变量
# birdsong()
#
