import pytest


def test_option1(pytestconfig):
    print('host:%s' % pytestconfig.getoption('host'))
    print('port:%s' % pytestconfig.getoption('port'))


def test_option2(config):
    print('host:%s' % config.getoption('host'))
    print('port:%s' % config.getoption('port'))

def test_tmpdir(tmpdir):
    a_dir=tmpdir.mkdir('mytmpdir')
    a_file=a_dir.join('tmpfile.txt')

    a_file.write('hello,pytest!')

    assert a_file.read()=='hello,pytest!'