# 1.懒惰即美 2.抽象和结构 3.创建函数
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
#     print(fibs[-1])
#     print(fibs[-2])
print(fibs)


#
# fibs0=[0,1]
# num=eval(input('How many Fibonacci numbers do you want?'))
# for i in range(num-2):
#     fibs.append(fibs0[-2]+fibs0[-1])
# print(fibs0)
#
# def result(num):
#     result=[0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result
# print(result(10))


# 修改参数
# storage = {}
# storage['first'] = {}
# storage['middle'] = {}
# storage['last'] = {}
# me = 'Magnus Lie Hetland'
# storage['first']['Magnus'] = [me]
# storage['middle']['Lie'] = [me]
# storage['last']['Hetland'] = [me]
# print(storage['middle']['Lie'])
# print(storage)
# my_sister = 'Anne Lie Hetland'
# storage['first'].setdefault('Anne', []).append(my_sister)
# storage['middle'].setdefault('Lie', []).append(my_sister)
# storage['last'].setdefault('Hetland', []).append(my_sister)
# print(storage['middle']['Lie'])
# print(storage)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


storage = {}
init(storage)


# print(storage)


def lookup(data, label, name):
    return data[label].get(name)


print(lookup(storage, 'middle', 'Lei'))


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames = {}
init(MyNames)
# print(MyNames)
store(MyNames, 'Magnus Lie Hetland')
# print(lookup(MyNames, 'middle', 'Lie'))
# print(MyNames)
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print(MyNames)
print(lookup(MyNames, 'first', 'Robin'))
store(MyNames, 'Mr. Gumby')
print(lookup(MyNames, 'middle', ''))


# 参数不可变
def inc(x):
    return x + 1


foo = 10
foo = inc(foo)
print(foo)


def inc(x):
    x[0] = x[0] + 1


foo = [10]
inc(foo)
print(foo)


# 关键字参数和默认值
def hello_1(greeting, name):
    print('%s,%s!' % (greeting, name))


def hello_2(name, greeting):
    print('%s,%s!' % (name, greeting))


hello_1('Hello', 'world')
hello_2('Hello', 'world')
hello_1(greeting='Hello', name='world')
hello_1(name='world', greeting='Hello')
hello_2(greeting='Hello', name='world')


def hello_3(greeting='Hello', name='world'):
    print('%s,%s!' % (greeting, name))


hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')
hello_3(name='Gumby')


def hello_4(name, greeting='Hello', punctuation='!'):
    print('%s,%s%s' % (name, greeting, punctuation))


hello_4('Mars')
hello_4('mars', 'Howdy')
hello_4('mars', 'Howdy', '...')
hello_4('Mars', 'punctuation=''.')
hello_4('Mars', greeting='Top of the morning to ya')


# 1. 收集参数
def print_params_1(*params):
    print(*params)


print_params_1('Testing')
print_params_1(1, 2, 3)


def print_params_2(title, *params):
    print_params_1(title)
    print_params_1(*params)


print_params_2('Params:', 1, 2, 3)
print_params_2('Nothing:')


def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


# 参数收集的逆过程
def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)


def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')


args = {'name': 'Mr. Gumby', 'age': 42}
with_stars(**args)
without_stars(args)


# 拼接操作符“传递”参数
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)


def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)
