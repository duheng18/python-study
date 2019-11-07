# 1.Test_str="Python was created in 1989,Python is using in AI,big data,IOT."
# 按下列要求对上面文字做出处理。
st_str="Python was created in 1989,Python is using in AI,big data,IOT."
# 把上面文字中的所有大写转化为小写
st_lower=st_str.lower()
print(st_lower)
# 把这段话每个短词放到列表里面，不能包含空格.
test_str=st_str.replace(',',' ').replace('.',' ')
test_list=test_str.split()
# print(test_list)

import re

print(re.split('[,.\000]', st_str))
# # 把列表最中间的一个单词打印出来。
mid=int(len(test_list)/2)
# print(test_list[mid])
# 2.List1=["python",5,6,8],list2=["python","5",6,8,10],
# 对list1和list2做出如下处理：
# 把上面2个list的内容合并成一个利用set里面的方法，对合并后的list，去除重复元素。
# 最后输出还是list=["python",5,6,8,"5",10](顺序可以不一样)
list1=["python",5,6,8]
list2=["python","5",6,8,10]
list1.extend(list2)
# print(list1)
set1=set(list1)
# print(set1)
list3=list(set1)
print(list3)
