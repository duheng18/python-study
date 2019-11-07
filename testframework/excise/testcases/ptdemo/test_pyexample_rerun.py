#!/usr/bin/env python
# coding=utf-8

# Pytest-rerunfails
# 测试场景：
# 在web、APP自动化测试中，经常出现超时导致测试失败
# 加成等待时间or重新执行？

import random


def add(x, y):
    return x + y


def test_add2():
    random_value = random.randint(2, 4)
    print("random_vaule:" + str(random_value))
    assert random_value == 3

# pip install pytest-rerunfailures
# pytest --reruns  3 test_pyexample_rerun.py  重新跑失败的用例
# pytest -s --reruns 3 test_pyexample_rerun.py
