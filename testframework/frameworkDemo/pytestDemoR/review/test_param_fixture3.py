import pytest

data1 = ['linda', 'sevenruby']


@pytest.fixture(params=data1)
def data2(request):
    print("数据准备unpack")  # 解包
    # return request.param
    a = request.param
    print(a)
    return a


# @pytest.mark.parametrize('data2',data1)
def test_data(data2):
    print(data2)


if __name__ == '__main__':
    pytest.main(
        ['-s', '/Users/duheng/Documents/project/testframework/frameworkDemo/pytestDemoR/review/test_param_fixture3.py'])
