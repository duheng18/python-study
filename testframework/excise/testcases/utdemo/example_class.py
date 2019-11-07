#!/usr/bin/env python
# coding=utf-8

#     测试模块首先import unittest
#     测试类必须继承unittest.TestCase
#     测试方法必须以“test_”开头
#     模块名字，类名没有要求

import unittest


class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("init class\n")
        simple_test.foo = list(range(10))
        print(str(simple_test.fo))

    def test_1st(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 9)

    def test_2nd(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 8)

    @classmethod
    def tearDownClass(cls):
        print("end class")


if __name__ == '__main__':
    unittest.main()
