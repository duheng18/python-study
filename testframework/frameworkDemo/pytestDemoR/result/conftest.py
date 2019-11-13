'''
例子2: 前端自动化中应用-conftest
场景：你与其他测试工程师合作一曲开发时，公共的模块要在不同文件中，要在大家都访问到的地方。
解决：使用conftest.py这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用。
前提：conftest文件名是不能换的，放在项目下是全局的数据共享的地方，全局的配置和前期工作都可以
     写在这里，放在某个包下，就是这个包数据共享的地方。
执行：系统执行到参数login时先从本文件中查找是否有这个名字的变量什么的，之后在conftest.py中找到是否有。
步骤：将登陆模块带@pytest.fixture写在conftest.oy
'''
import pytest

@pytest.fixture() #本质上都是装饰器
def login():
    print('\n登录了...')