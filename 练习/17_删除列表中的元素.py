#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 16:25
# @Author  : XiaomeiLu
# @FileName: 17_删除列表中的元素.py
# @Software: PyCharm

"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
lambda 匿名函数
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = filter(lambda x: x > 5, a)
print(list(b))

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i for i in a if i > 5]
print(b)