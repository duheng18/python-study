# -*- coding:utf-8 -*-
#查找列表中某个值是否再列表中
a='d'
b=['a','b','c','d']
for my in b:
    if a == my:
        print("找到它！")
        break
    else:
        print("没找到！")
