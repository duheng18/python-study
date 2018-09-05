# 作用域
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
x=1
y=2
print(output(y))