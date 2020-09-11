#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 19:37
# @Author  : XiaomeiLu
# @FileName: 2_反转整数.py
# @Software: PyCharm

"""先判断传入值是否为负数，是的话直接乘以-1，在转成字符串翻转，最后在返回值得时候在乘-1
考虑溢出的情况下只需判断返回值的大小是否超出了给定的范围，超出的话返回0"""


def reverse(x):
    if x < 0:
        x = abs(x)
        a = str(x)[::-1]   #反转list
        b = int(a)*-1
    else:
        a = str(x)[::-1]
        b = int(a)
    if -2**31 < b < 2**31-1:
        return b
    else:
        return 0


print(reverse(123456789))