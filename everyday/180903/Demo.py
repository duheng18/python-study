

# fibs=[0,1]
# for i in range(8):
#     fibs.append(fibs[-2]+fibs[-1])
#     # print('fibs[-2]=%d,fibs[-1]=%d'%(fibs[-2],fibs[-1]))
#     print('fibs[-2]={},fibs[-1]={}'.format(fibs[-2],fibs[-1]))
# print(fibs)

# fibs0 = [0, 1]
# num = eval(input('How many Fibonacci numbers do you want?'))
# for i in range(num - 2):
#     fibs0.append(fibs0[-2] + fibs0[-1])
#     print(fibs0)
# print(fibs0)


def fib(num):
   result=[0,1]
   for i in  range(num-2):
        result.append(result[-2]+result[-1])
        print('result[-2]=%d,result[-1]=%d'%(result[-2],result[-1]))
   return result
num=eval(input('How many Fibonacci numbers do you want?'))
print(fib(num))
print(fib(4))

# 9*9乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{} * {} = {}\t'.format(i, j, i * j), end='')
#     print()


def hello(name):
    return 'Hello,'+name+'!'
print (hello('world'))
print(hello('Gumby'))

def square(x):
    'Calculates the square of the number x.'
    return x*x
print(square(12))
