#! /usr/bin/env python
# coding=utf-8

from ptdemo.pytest_practice import bubble_sort


def test_bubble_sort():
    assert bubble_sort([13, 1, 2, 5, 8, 18]) == [1, 2, 5, 8, 13, 18]
