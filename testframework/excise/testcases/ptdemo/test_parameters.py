# coding=utf-8


# Pytest编写规范
# 编写规范：
#     测试文件以test_开头（以_test结尾也可以）
#     测试类以Test开头，并且不能带有__init__方法
#     测试函数以test_开头

# Pytest-参数化
# 测试场景：
# 测试登录成功,登录失败（账号错误，密码错误）
# 创建多种账号：中文账号，英文账号
# Copy多份代码or读入参数？
# 一次性执行多个输入参数
# pytest.mark.parametrize
import pytest


@pytest.mark.parametrize("x,y", [
    (3 + 5, 9),
    (2 + 4, 6),
    (6 * 9, 42),
    ("testerhome", "testerhome"),
])
def test_add(x, y):
    assert x == y


@pytest.mark.parametrize("x,y,z", [
    (3 + 5, 9, 8),
    (2 + 4, 6, 9),
    (6 * 9, 42, 9),
    ("testerhome", "testerhome", "new"),
])
def test_multiple_add(x, y, z):
    assert x == y + z


@pytest.mark.parametrize("x,y", [
    (9, 9),
    (2, 2),
    (42, 42),
    ("testerhome", "testerhome"),
])
def test_add2(x, y):
    assert x == y
