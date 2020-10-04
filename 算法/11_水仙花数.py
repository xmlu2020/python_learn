#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 19:52
# @Author  : XiaomeiLu
# @FileName: 11_水仙花数.py
# @Software: PyCharm

def shuixianhua():
    sxh = []
    for i in range(100, 1000):
        s = 0
        m = list(str(i))
        for j in m:
            s += int(j)**len(m)
        if i == s:
            print(i)
            sxh.append(i)
    print("100到1000之间的水仙花数是：%s" % sxh)


if __name__ == '__main__':
    shuixianhua()
