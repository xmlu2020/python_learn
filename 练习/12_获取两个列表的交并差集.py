#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 16:33
# @Author  : XiaomeiLu
# @FileName: 12_获取两个列表的交并差集.py
# @Software: PyCharm


a = [1, 2, 3, 4]
b = [4, 3, 5, 6]
jj1 = [i for i in a if i in b]
print("交集", jj1)
jj2 = list(set(a).intersection(set(b)))
print("交集", jj2)

bj1 = list(set(a).union(set(b)))
print("并集", bj1)

cj1 = list(set(b).difference(set(a)))  # b中有而a中没有
print("差集", cj1)
cj2 = list(set(a).difference(set(b)))  # a中有而b中没有
print("差集", cj2)
