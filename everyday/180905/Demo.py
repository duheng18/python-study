# 作用域：局部变量、全局变量
x = 1
scope = vars()
print(scope)
print(scope['x'])
scope['x'] += 1
print(x)
print(scope)


def foo():
    x = 42


print(foo())
print(x)


def output(x):
    print(x)


x = 1
y = 2
output(y)


# 函数内部访问全局变量
def combine(parameter):
    print(parameter + external)


external = 'berry'
combine('Shrub')


# 函数内使用全局变量加globals()
def combine(parameter):
    print(parameter + globals()['parameter'])


parameter = 'berry'
combine('Shrub')

print(globals())
print(locals())
print(vars())


# 嵌套作用域
# 一个函数放在里面
def foo():
    def bar():
        print("Hello world!")

    bar()


# 用一个函数创建另一个
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


double = multiplier(2)
print(double(5))

triple = multiplier(3)
print(triple(3))

print(multiplier(5)(4))
