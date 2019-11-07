#! /usr/bin/env python
# coding=utf-8

#     测试模块首先import unittest
#     测试类必须继承unittest.TestCase
#     测试方法必须以“test_”开头
#     模块名字，类名没有要求

import unittest


class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('\ntest_1st')
        self.assertEqual(self.foo.pop(), 9)

    def test_2nd(self):
        print('test_2nd')
        print('test_2nd:' + str(self.foo))
        self.assertEqual(self.foo.pop(), 9)

    @classmethod
    def tearDownClass(self):
        print("end class")

if __name__=='__main__':
    unittest.main()
