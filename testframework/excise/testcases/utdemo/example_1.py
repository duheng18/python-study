#! /usr/bin/env python
# coding=utf-8

#     测试模块首先import unittest
#     测试类必须继承unittest.TestCase
#     测试方法必须以“test_”开头
#     模块名字，类名没有要求

import unittest


class simple_test(unittest.TestCase):
    def setUp(self):
        print("init")
        self.foo = list(range(10))
        # print(self.foo)
        print(str(self.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo.pop(), 10)

    # def test_2nd(self):
    #     print('test_2nd')
    #     self.assertEqual(self.foo.pop(), 9)

    def tearDown(self):
        print("end method")

if __name__=='__main__':
    unittest.main()