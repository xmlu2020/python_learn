#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 20:56
# @Author  : XiaomeiLu
# @FileName: 15_幂的递归.py
# @Software: PyCharm


"""
计算x的n次方，如 3^4 = 3*3*3*3 = 81
"""


def mi(x, n):
    if n == 0:
        return 1
    else:
        return x*mi(x, n-1)


if __name__ == '__main__':
    print(mi(2, 3))