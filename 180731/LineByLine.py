# #文件的逐行操作
# #逐行遍历文件：方法一
# #获得文件名称
# fname=input("请输入要打开的文件名称：")
# #将文件以只读方式打开，赋给文件句柄fo
# fo=open(fname,"r",encoding="UTF-8")
# #使用for in遍历循环对文件fo的所有行以及fo.readlines(),将fo中所有的信息文本以行的方式形成一个列表，每行是一个列表元素
# for line in fo.readlines():  #一次读入分行处理
#     print(line)
# fo.close()

# 逐行遍历文件：方法二
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r", encoding="UTF-8")
for line in fo:
    print(line)
fo.close()
