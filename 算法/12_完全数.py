#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 19:58
# @Author  : XiaomeiLu
# @FileName: 12_完全数.py
# @Software: PyCharm


"""完全数=所有因子的和"""


def wanquanshu():
    a = []
    for i in range(1, 1000):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if i == s:
            print(i)
            a.append(i)
    print("100以内的完全数：%s" % a)


if __name__ == '__main__':
    wanquanshu()

