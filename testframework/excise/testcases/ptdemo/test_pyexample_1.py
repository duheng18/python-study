#! /usr/bin/env python
# coding=utf-8


# Pytest编写规范
# 编写规范：
#     测试文件以test_开头（以_test结尾也可以）
#     测试类以Test开头，并且不能带有__init__方法
#     测试函数以test_开头

# Pytest-多个Assert
#测试场景：
    #一个测试用例中有多个数据需要比较；
    #一个个比较or放到一个数据结构里面全量比较？
        #全量比较，无法找到哪个值不对
        #一个个比较数值，第一个失败就退出
import time


def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3


def test_add2():
    print("I am 2")
    time.sleep(3)
    assert add(1, 2, 3.1) == 5.3
    assert add(1, 2) == 3
