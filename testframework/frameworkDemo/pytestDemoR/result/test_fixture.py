'''
例子1：前端自动化中应用
场景：测试用例执行时，有的用例需要登录才能执行，有些用例不需要登录。setup和teardown无法满足。fixture
可以。默认scope(范围) function
步骤：
1.导入pytest
2.在登录的函数上面加@pytest.fixture()
3.在要使用的测试方法中传入（登录函数名称），就先登录
4.不传入的就不登录直接执行测试方法。
'''
import pytest

def test_soso(login):
    print('case1:登录后执行搜索')

def test_cakan():
    print('case2:不登录就看')

def test_cart(login):
    print('case3:登录，加购物车')

if __name__=='__main__':
    pytest.main(['-s','test_fixture.py'])