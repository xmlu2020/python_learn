#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 20:57
# @Author  : XiaomeiLu
# @FileName: 8_选择排序.py
# @Software: PyCharm


def SelectSort(arr):
    """从头至尾扫描序列，找出最小的一个元素，和第一个元素交换，接着从剩下的元素中继续这种选择和交换方式，最终得到一个有序序列
    数据规模越小越好,不占用额外内存空间
    时间复杂度:O(n²)
    空间复杂度：O(1)"""
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    arr = [1, 6, 3, 8, 2, 9, 25, 37]
    print(SelectSort(arr))