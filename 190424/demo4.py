# -*- coding:utf-8 -*-
# 字典

# 把key循环出来
D = {'name': 'zhangsan', 'age': 18, 'tel': 1881, 'height': 1.76, 'weight': 75}
for key in D:
    print(key, '=>', D[key])

# 只循环value
for value in D.values():
    print(value)

# 把key和value都循环出来
for key,value in D.items():
    print(key,":",value)
    # assert D[key]==value

