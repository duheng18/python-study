# python流程控制语句
# pyhon条件语句
# if判断条件1：
#   执行语句1......
# elif判断条件2:
#   执行语句2......
# elif判断条件3:
#   执行语句3......
# else:
#   执行语句4......
print("请求输入数字:")
a = input()  # 从控制台输入内容到变量a
flag = int(a)  # 输入的内容默认是字符串的
if flag == 1:
    print("喝奶")
elif flag == 2:
    print("吃饭")
elif flag == 3:
    print("吃大餐")
else:
    print("不吃")
