#!/usr/bin/env python
# coding=utf-8

# Pytest-assume
# 前面失败下面也会执行（一次性把错误都抛出来）
import pytest


def test_multiple_assert():
    pytest.assume(1 == 2)
    pytest.assume(2 == 2)
    pytest.assume(3 == 2)

    # assert 1 == 2
    # assert 2 == 2
