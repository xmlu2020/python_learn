#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 20:16
# @Author  : XiaomeiLu
# @FileName: 13_n的阶乘.py
# @Software: PyCharm


from functools import reduce
"""
3!=3*2*1
0!=1
"""


def jiecheng1():
    a = 1
    n = 5
    for i in range(1, n+1):
        a = a*i
    print(a)


def jiecheng2():
    n = 5
    b = reduce(lambda x, y: x*y, range(1, n+1))
    print(b)


def jiecheng3(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*jiecheng3(n-1))


if __name__ == '__main__':
    jiecheng1()
    jiecheng2()
    c = jiecheng3(10)
    print(c)