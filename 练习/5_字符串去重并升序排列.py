#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 20:39
# @Author  : XiaomeiLu
# @FileName: 5_字符串去重并升序排列.py
# @Software: PyCharm

s = "ajldjlajfdljfddd"
s = set(s)
print(s)
s = list(s)
print(s)
s.sort(reverse=False)
res = "".join(s)
print(res)