#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 20:02
# @Author  : XiaomeiLu
# @FileName: 2_列表推导式提取大于10的数.py
# @Software: PyCharm


list = [1, 2, 3, 4, 5]


def fn(x):
    return x**2


res = map(fn, list)
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
res = [i for i in res if i > 10]
print(res)
