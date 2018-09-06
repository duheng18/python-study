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
    print(parameter+globals()['parameter'])
parameter='berry'
combine('Shrub')

print(globals())
print(locals())
print(vars())