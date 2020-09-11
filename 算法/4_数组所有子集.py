#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 18:41
# @Author  : XiaomeiLu
# @FileName: 4_数组所有子集.py
# @Software: PyCharm


def getArraySubSet(originArray):
    """
       :type originArray:list
       :rtype :listlist
    """
    result = [[]]
    for i in range(len(originArray)):
        for j in range(len(result)):
            result.append(result[j] + [originArray[i]])  # 现有每个子集中添加新元素，作为新子集加入结果集中
    return result

# 测试
originArray = [1, 2, 3, 4]
subset = getArraySubSet(originArray)
print(subset)