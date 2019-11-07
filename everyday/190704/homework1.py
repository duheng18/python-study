#!/usr/bin/env python
# coding=utf-8

# 既能被7整除也能被5整除
result = []
for i in range(1000, 2501):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)


