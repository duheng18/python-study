# #遍历全文本：方法一
# #特点：一次读入，统一处理
# fname=input("请输入要打开的文件名称：")
# fo=open(fname,"r",encoding="UTF-8")
# txt=fo.read()
# print(txt)
# #对全文txt进行处理
# fo.close()

# 遍历全文本：方法二
# 特点：按数量读入，逐步处理
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r", encoding="UTF-8")
txt = fo.read(2)
while txt != "":
    # 对txt进行处理
    txt = fo.read(2)
fo.seek(0)
print(fo.read())
fo.close()
