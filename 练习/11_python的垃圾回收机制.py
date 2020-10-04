#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 16:11
# @Author  : XiaomeiLu
# @FileName: 11_python的垃圾回收机制.py
# @Software: PyCharm

"""
python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除
和分代回收主要是为了处理循环引用的难题

引用计数算法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果独享的引用计数不为1，比如3，那么此时只会让这个引用计数
减1，即变为2，当再次调用del时，变为1，如果在调用1次del，此时会真的把对象进行删除
"""


def __del__(self):
    print("__del__方法被调用")
    print("%s对象马上被干掉了..." % self.__name)


cat = "波斯猫"
cat2 = cat
cat3 = cat
print(id(cat), id(cat2), id(cat3))
print("---马上 删除cat对象")
del cat

print(id(cat2), id(cat3))
print("---马上 删除cat2对象")
del cat2

print(id(cat3))
print("---马上 删除cat3对象")
del cat3
