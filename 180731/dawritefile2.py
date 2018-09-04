fo = open("output.txt", "w+", encoding="UTF-8")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)  # 写入一个字符串列表
fo.close()
