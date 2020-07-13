#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 18:46
# @Author  : XiaomeiLu
# @FileName: 3_2高级特性_迭代.py
# @Software: PyCharm

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

# from collections import Iterable
# isinstance('abc',Iterable)
#
# isinstance([1,2,3],Iterable)
#
# isinstance(123,Iterable)

'Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身'

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
