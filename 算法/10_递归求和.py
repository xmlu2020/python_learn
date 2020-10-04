#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 21:13
# @Author  : XiaomeiLu
# @FileName: 10_递归求和.py
# @Software: PyCharm


def get_sum(num):
    if num >= 2:
        res = num+get_sum(num-1)
    else:
        res = 0
    return res


res = get_sum(10)
print(res)

