#!/usr/bin/env python
# encoding=utf-8

import unittest


class MyClass(object):
    def __init__(self, num):
        self.num = num

    def printNum(self):
        return self.num


class TestMyClass(unittest.TestCase):
    def test_printNum(self):
        value = MyClass(6)
        # 当assertEquals失败时，会把第一个和第二个参数的值打印出来
        self.assertEqual(7, value.printNum())
        # assertFalse和assertTrue不会打印值
        self.assertFalse(value.printNum() == 6)


if __name__=='__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
    unittest.TextTestRunner(verbosity=2).run(suite)