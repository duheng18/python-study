import pytest

@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass

@pytest.mark.skipif(conn.__version__<'0.2.0',
                    reason='not supported until v0.2.0')
def test_api():
    pass