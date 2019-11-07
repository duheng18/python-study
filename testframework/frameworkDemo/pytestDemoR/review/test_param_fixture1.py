import pytest

data1 = ['linda', 'sevenruby']


@pytest.mark.parametrize('data', data1)
def test_data(data):
    print(data)


if __name__ == '__main__':
    pytest.main()
