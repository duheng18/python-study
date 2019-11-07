'''

例子3: 前端自动化中应用-yield
场景：你已经可以将测试方法前要执行的或依赖的解决掉了，测试方法后销毁清除数据的要如何进行呢？
     范围是模块级别的。类似setupClass
解决：通过在同一模块中加入yield关键字，yield是调用第一次返回结果，第二次执行它下面的语句返回。
步骤：在@pytest.fixture(scope=module)
     在登录的方法中加yield，之后加销毁清除的步骤
'''
import pytest

# 在整个模块(文件)只做一次的事类似setupClass，范围是模块级别的。
# yield是调用第一次返回结果，第二次执行它下面的语句返回。


@pytest.fixture(scope="module",autouse=True)
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')

def test_soso(login):
    print('case1:登录后执行搜索')

def test_cakan():
    print('case2:不登录就看')

def test_cart(login):
    print('case3:登录，加购物车')

if __name__=='__main__':
    pytest.main(['-s','test_fixture2.py'])