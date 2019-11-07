#! /usr/bin/env python
# coding=utf-8

#     测试模块首先import unittest
#     测试类必须继承unittest.TestCase
#     测试方法必须以“test_”开头
#     模块名字，类名没有要求

import unittest
import logging


def setUpMoudle():
    print("setup method\n")
    global foo
    foo = list(range(10))


class simple_test(unittest.TestCase):

    def test_1st(self):
        logging.info('info')
        logging.error('error')
        print('simple_test1_1' + str(foo))
        self.assertEqual(foo.pop(), 9)

    def test_2nd(self):
        print('simple_test1_2' + str(foo))
        self.assertEqual(foo.pop(), 8)


class simple_test2(unittest.TestCase):

    def test_1st(self):
        print('simple_test2_1' + str(foo))
        self.assertEqual(foo.pop(), 7)

    def test_2nd(self):
        print('simple_test2_2' + str(foo))
        self.assertEqual(foo.pop(), 6)


def tearDownModule():
    print("end method")


if __name__ == '__main__':
    unittest.main()
