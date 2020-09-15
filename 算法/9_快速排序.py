#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 14:43
# @Author  : XiaomeiLu
# @FileName: 9_快速排序.py
# @Software: PyCharm


def QuickSort(arr: list, left: int, right: int) -> None:
    """快速排序
    最优时间复杂度：O(nlogn)
    最坏时间复杂度：O(n2)
    空间复杂度：O(logn)
    稳定性：不稳定"""
    
    if left >= right:  # 递归的退出条件
        return
    base = arr[left]  # 设定起始的基准元素
    i, j = left, right  # i为序列左边在开始位置的由左向右移动的游标，j为序列右边末尾位置的由右向左移动的游标

    while i < j:
        # 如果i与j未重合，j(右边)指向的元素大于等于基准元素，则j向左移动
        while i < j and arr[j] >= base:
            j = j - 1
        arr[i] = arr[j]
        # 走到此位置时j指向一个比基准元素小的元素,将j指向的元素放到i的位置上,此时j指向的位置空着,
        # 接下来移动i找到符合条件的元素放在此处
        # 如果i与j未重合，i指向的元素比基准元素小，则i向右移动
        while i < j and arr[i] < base:
            i = i + 1
        arr[j] = arr[i]
        # 此时i指向一个比基准元素大的元素,将i指向的元素放到j空着的位置上,此时i指向的位置空着,
        # 之后进行下一次循环,将j找到符合条件的元素填到此处
    # 退出循环后，i与j重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    arr[i] = base
    # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    QuickSort(arr, left, i - 1)
    # 对基准元素右边的子序列进行快速排序
    QuickSort(arr, i + 1, right)


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)
