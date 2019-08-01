#!/usr/bin/env python
# coding=utf-8

def add_method(x, y):
    '''

    :param x:
    :param y:
    :return:
    '''
    try:
        return x + y
    except Exception as e:
        print(e)
        return None


print(add_method("a", 11))
