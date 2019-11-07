import pytest
import time

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


@pytest.fixture(scope='session', autouse=True)
def timer_session_scope():
    start = time.time()
    # print(start) 1566812054.379041
    # print(time.localtime(start)) time.struct_time(tm_year=2019, tm_mon=8, tm_mday=26, tm_hour=17, tm_min=33, tm_sec=5, tm_wday=0, tm_yday=238, tm_isdst=0)
    print('\nstart:{}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print('finished:{}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print('Total time cost:{:.3f}s'.format(finished - start))


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print('Time cost:{:.3f}s'.format(time.time() - start))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(2)
