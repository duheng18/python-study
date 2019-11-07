import pytest

data1 = ['linda', 'sevenruby']


@pytest.fixture()
def data(request):
    print("数据准备unpack") #解包
    return request.param


@pytest.mark.parametrize('data', data1,indirect=True)
def test_data(data):  # data参数名
    print(data)


if __name__ == '__main___':
    pytest.main(['-s', 'test_param_fixture.py'])
