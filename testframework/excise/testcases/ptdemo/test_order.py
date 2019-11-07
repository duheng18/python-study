#!/usr/bin/env python
# coding=utf-8

# Pytest-ordering
# 测试场景：
    # 在web测试中，上下测试用例页面切换有依赖关系；
    # 在修改信息的页面中，依赖于前面用例已经创建好的信息，比如修改账号信息，依赖于已经创建好的数据
import time
import pytest

value = 0


@pytest.mark.run(order=2)
def test_add2():
    print("I am 2")
    time.sleep(2)
    assert value == 10


@pytest.mark.run(order=1)
def test_add():
    print("I am test add")
    global value
    value = 10
    assert value == 10
