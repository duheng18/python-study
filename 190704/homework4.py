#!/usr/bin/env python
# coding=utf-8

dic = {"name": "xiaozhang", "sex": "male"}
def dicget(key):
    try:
        dic[key]
    except KeyError as e:
        print(e)
    else:
        print(dic[key])

dicget("name")
dicget("grade")