#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 19:24
# @Author  : XiaomeiLu
# @FileName: 5_最长公共前缀.py
# @Software: PyCharm


def longsetCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    commonPrefix = ""
    if not strs or len(strs) < 1:
        return commonPrefix
    minimum = min(strs, key=lambda x: len(x))
    # min([len(str1) for str1 in strs])
    # 找出字符串中长度最小的值
    # 冒号:之前的x表示是这个函数的参数,匿名函数不需要return来返回值，表达式本身结果就是返回值
    for idx, char in enumerate(minimum):
        # 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        for str in strs:
            if str[idx] != char:
                return commonPrefix
        commonPrefix += char
    return commonPrefix


strs = ["a", "ab", "abc"]
print(longsetCommonPrefix(strs))


