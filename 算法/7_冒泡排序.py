#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 21:54
# @Author  : XiaomeiLu
# @FileName: 7_冒泡排序.py
# @Software: PyCharm


def BubbleSort(lst):
    """
    比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    时间复杂度O(n^2)，
    空间复杂度O(1),稳定
    额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)
    """
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


if __name__ == '__main__':
    lst = [1, 6, 3, 8, 2, 9, 25, 37]
    print(BubbleSort(lst))
