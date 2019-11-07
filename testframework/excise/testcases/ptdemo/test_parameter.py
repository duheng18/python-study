# coding=utf-8


# Pytest编写规范
# 编写规范：
#     测试文件以test_开头（以_test结尾也可以）
#     测试类以Test开头，并且不能带有__init__方法
#     测试函数以test_开头

import pytest
import random


@pytest.mark.parametrize("x", [(1),(2),(6)])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 7)
