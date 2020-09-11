#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 21:13
# @Author  : XiaomeiLu
# @FileName: 6_x的平方根.py
# @Software: PyCharm


def mySqrt(x):
    # 首先，我们构造一个数组，数组中的每个值即为其所在位置（下标），数组范围是从0到x
    left, right = 0, x  # 初始化左指针和右指针为数组两端数字

    while left <= right:  # 要求左指针不大于又指针，当满足条件时执行
        # 求取中点位置（位置即为该位置的数），如果数组长度为偶数，取中间偏左的一个
        mid = left + (right - left) // 2

        if mid ** 2 > x:  # 如果中点的平方大于输入x
            right = mid - 1  # 抛弃数组右半部分
        elif mid ** 2 < x:  # 如果中点的平方小于输入x
            left = mid + 1  # 抛弃数组左半部分
        else:  # 如果中点的平方即为输入x
            return mid  # 直接返回中点即可

    return right

print(mySqrt(9))