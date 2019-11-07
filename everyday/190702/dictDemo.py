my_dic = {"name": "xiaozhang", "company": "baidu", "grade": "T7"}
print(help('dict'))
# 合并多个字典
dic2 = {"name2": "hanmeimei", "company2": "taobao", "grade2": "P7"}
my_dic.update(dic2)
print(my_dic)
# 嵌套字典

# 通过key来访问value
print(my_dic["company"])
print(my_dic.get("grade"))
# 插入key
my_dic["Sex"] = "male"
print(my_dic)
# 更新已有key的value
my_dic["grade"] = "P9"
print(my_dic)
# 任意对象作为key和value

# 删除一个key
del my_dic["name"]
print(my_dic)
print(my_dic.items())
