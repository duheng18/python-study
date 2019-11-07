# 多个超类
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


# 多重继承
class TalkerCauculator(Calculator, Talker):
    pass


tc = TalkerCauculator()
tc.calculate('1+2*3')
tc.talk()
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))

# hasattr() 函数用于判断对象是否包含对应的属性。
# hasattr 语法：hasattr(object, name)
# 参数
# object -- 对象。
# name -- 字符串，属性名。
# 返回值
# 如果对象有该属性返回 True，否则返回 False。
print(callable(getattr(tc, 'talk', None)))
# getattr() 函数用于返回一个对象属性值。
# getattr(object, name[, default])
# 参数
# object -- 对象。
# name -- 字符串，对象属性。
# default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

# callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，
# 调用对象ojbect绝对不会成功。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
# callable()方法语法： callable(object)
# 参数
# object -- 对象
# 返回值
# 可调用返回 True，否则返回 False。
print(callable(getattr(tc, 'fnord', None)))
setattr(tc, 'name', 'Mr. Gumby')
# setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
# setattr 语法：setattr(object, name, value)
# 参数
# object -- 对象。
# name -- 字符串，对象属性。
# value -- 属性值。
print(tc.name)
# 查看对象内所有存储的值
print(tc.__dict__)
# inspect模块
