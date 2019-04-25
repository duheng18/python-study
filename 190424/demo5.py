# -*- coding:utf-8 -*-
def foo(x, *args, a=4, **kwargs):
    # 使用默认参数时，注意默认参数的位置要在args之后kwargs之前
    print(x)
    print(a)
    print(args)
    print(kwargs)


# foo(1,*(5,6,7,8),**{"y":2,"z":3})
foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)
