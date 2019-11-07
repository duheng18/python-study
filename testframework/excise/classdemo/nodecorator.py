#! /usr/bin/env python
# coding=utf-8
import time, random


def loop_time(x, y):
    time_flag = time.time()
    result = 0
    for i in range(x, y):
        time.sleep(random.choice((0.1, 0.2, 0.3)))
        result = x + y
    print("time cost:", time.time() - time_flag)
    return result


print(loop_time(1, 4))
