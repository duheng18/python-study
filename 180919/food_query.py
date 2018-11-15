# -*- coding:utf-8 -*-
import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()
a = sys.argv[1]
print(a)
query = 'SELECT * FROM food WHERE ' + a
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()
# 警告
# 这个程序从用户那里获取输入，并将其插入到SQL查询中。在你是用户而且不会输入太不可思议的内容时，这没有问题。然而，利用这种输入偷偷地插入
# 恶意的SQL代码以破坏数据库是一种常见的计算机攻击方式，称为SQL注入攻击。请不要让你的数据库(以及其他任何东西)暴露在原始用户输入的“火力范
# 围”内，除非你对这样做的后果心知肚明。
