import pytest

# 在整个模块(文件)只做一次的事类似setupClass，范围是模块级别的。
# yield是调用第一次返回结果，第二次执行它下面的语句返回。
'''
fixture的自动应用
场景：不想原测试方法有任何改动，或全部都自动实现自动应用，没特例，也都不需要返回值时可以选择自动应用
解决：使用fixture中参数autouse=True实现
步骤：在方法上面加@pytest.fixture(autouse=True)
     使用@pytest.mark.usefixtures
步骤：在测试方法上加@pytest.mark.usefixtures("start")
'''

@pytest.fixture()
def open_browser():
    print("\n打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')

@pytest.mark.usefixtures('open_browser')
def test_soso():
    print('case1:登录后执行搜索')

def test_cakan():
    print('case2:不登录就看')

@pytest.mark.usefixtures('open_browser')
def test_cart():
    print('case3:登录，加购物车')

if __name__=='__main__':
    pytest.main(['-s','test_fixture01.py'])