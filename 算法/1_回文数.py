#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 18:28
# @Author  : XiaomeiLu
# @FileName: 1_回文数.py
# @Software: PyCharm

"""思路
先判断是不是整型数字
是
再判断是大于0还是小于0
大于0
则将数字写入list，正向排列和取反相等，则是回文数

为否则直接返回False"""


def type(num):
    if not isinstance(num, int):
        return False
    if num < 0:
        return False
    elif num > 0:
        num = str(num)
        list1 = list(num)
        print(list1)
        list2 = list1[:]
        list2.reverse()
        print(list2)
        if list1 == list2:
            return num, "是回文数"
        else:
            return num, "不是回文数"


num = int(input("输入一个数"))
print(type(num))

