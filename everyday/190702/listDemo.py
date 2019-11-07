my_list = ["python", 12, 2.3, 9.7, 10, 9, 19, 60]
list2 = [3, 4, 5]
print(help("list"))
# 串联多个列表
print(my_list + list2)
# 快速复制多个列表
print(list2 * 3)
# #嵌套列表
lang = [["python", 0.4], ["java", 0.5]]
# print(lang)
# #索引访问列表元素
print(my_list[1])
print(my_list[1:3])
print(my_list[-4:-2])
print(my_list[::2])
# #分片获取列表元素
# #增加列表元素
my_list.append("java")
print(my_list)

# 删除列表中的元素
print(id(my_list))
del my_list[0]
print(my_list)
print(id(my_list))
my_list2 = my_list[0:]
print(my_list2)
print(id(my_list2))
my_list.extend(list2)
print(my_list)

my_list.pop()
print(my_list)

my_list.reverse()
print(my_list)

multiple_list = [[1, 2], ["a", "b"], [1, 2, 4, 5]]
print(len(multiple_list))
