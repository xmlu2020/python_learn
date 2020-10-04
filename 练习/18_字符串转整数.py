#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 17:04
# @Author  : XiaomeiLu
# @FileName: 18_字符串转整数.py
# @Software: PyCharm

"""
字符串'123'转换成123，不使用内置api，例如int()
"""


def atoi(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num


if __name__ == '__main__':
    s = "12345"
    print(atoi(s))