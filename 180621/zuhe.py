# 规则2：局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F", "f"]  # 通过使用[]真实创建了一个全局变量列表ls


def fuc(a):
    ls.append(a)  # 此处ls是列表类型，未真实创建则等同于全局变量
    return


fuc("c")  # 全局变量ls被修改
print(ls)
