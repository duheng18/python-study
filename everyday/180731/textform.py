# -*- coding: utf-8 -*-
# 文本形式打开文件
tf = open("f.txt", 'rt', encoding="UTF-8")
print(tf.readline())
tf.close()
