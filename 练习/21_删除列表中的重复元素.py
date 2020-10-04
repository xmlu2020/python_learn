#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 20:56
# @Author  : XiaomeiLu
# @FileName: 21_删除列表中的重复元素.py
# @Software: PyCharm


def distFunc1(a):
    """使用集合去重"""
    a = list(set(a))
    print(a)


def distFunc2(a):
    """将一个列表中的数据取出放在另一个列表里，中间判断"""

    list = []
    for i in a:
        if i not in list:
            list.append(i)
    list.sort()
    print(list)


def distFunc3(a):
    """使用字典"""

    b = {}
    b = b.fromkeys(a)  #以a中的元素作为b的key,value为初始值none
    c = list(b.keys())
    c.sort()
    print(c)


if __name__ == '__main__':
    a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    distFunc1(a)
    distFunc2(a)
    distFunc3(a)