#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 20:35
# @Author  : XiaomeiLu
# @FileName: 14_斐波那契数列.py
# @Software: PyCharm

"""
数列：1，1，2，3，5，8，13...从3开始的每一项都等于前两项的和
求100以内的所有数据
"""


def fbnq():
    a = 0
    b = 1
    while b < 100:
        print(b, end=",")
        a, b = b, a+b


if __name__ == '__main__':
    fbnq()
