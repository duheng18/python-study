#  1/0
# ZeroDivisionError: division by zero

# raise Exception
#  raise Exception
# Exception

# raise Exception('hyperdrive overload')
# raise Exception('hyperdrive overload')
# Exception: hyperdrive overload

# import exceptions
# dir(exceptions)

# raise ArithmeticError
# raise ArithmeticError
# ArithmeticError

# class SomeCustomException(Exception): pass

# 不止一个except语句
# try:
#     x = eval(input("Enter the first number:"))
#     y = eval(input("Enter the second number:"))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")
# except TypeError:
#     print("That wasn't a number , was it?")

# 用muffled屏蔽ZeroDivisionError
# class MuffledCalculator:
#     muffled=False
#     def calc(self,expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
# calculator=MuffledCalculator()
# print(calculator.calc('10/2'))
# # print(calculator.calc('10/0'))
# calculator.muffled=True
# print(calculator.calc('10/0'))

# 用一个块捕捉多个异常
# try:
#     x = eval(input("Enter the first name:"))
#     y = eval(input("Enter the second name:"))
#     print(x / y)
# except(ZeroDivisionError, TypeError, NameError):
#     print('Your numbers were bogus...')

# 捕捉对象
# try:
#     x=eval(input('Enter the first number:'))
#     y=eval(input('Enter the second number:'))
# except(ZeroDivisionError,TypeError) as e:
#     print(e)

# 真正的全捕捉
# try:
#     x = eval(input('Enter the first name:'))
#     y = eval(input('Enter the second name:'))
#     print(x / y)
# except:
#     print('Something wrong happened...')

# try:
#     print('A simple task')
# except:
#     print('What? Something went wrong?')
# else:
#     print('Ah...It went as planned.')

# while True:
#     try:
#         x = eval(input('Enter the first name:'))
#         y = eval(input('Enter the second name:'))
#         value = x / y
#         print('x/y is', value)
#     except:
#         print('Invalid input.Please try again.')
#     else:
#         break
# 捕捉所有Exception类的异常
while True:
    try:
        x=eval(input('Enter the first name:'))
        y=eval(input('Enter the second name:'))
        value=x/y
        print('x/y is',value)
    except Exception as e:
            print('Invalid input:',e)
            print('Please try again')
    else:
        break
