import pytest


@pytest.mark.parametrize('data', [1, 2, 3])
def test_data(data):
    print(data)
