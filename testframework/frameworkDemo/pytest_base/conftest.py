import pytest


def pytest_addoption(parser):
    parser.addoption('--host', action='store', help='host of db')
    parser.addoption('--port', action='store', default='8888', help='port of db')


@pytest.fixture()
def config(request):
    return request.config

@pytest.fixture(scope='module')
def my_tmpdir_factory(tmpdir_factory):
    a_dir=tmpdir_factory.mktemp('mytmpdir')
    a_file=a_dir.join('tmpfile.txt')
    a_file.write('hello,pytest!')
    return a_file