fo = open("output.txt", "w+", encoding="UTF-8")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
for line in fo:
    print(line)  # 写入一个字符串列表
fo.close()
# 没有任何输出
